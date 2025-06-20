from nfl_api_client.endpoints._base import BaseEndpoint
from datetime import datetime
import httpx


def parse_scoreboard_response(resp_json: dict) -> list[dict]:
    def format_date_str(date_str: str) -> str:
        return datetime.strptime(date_str, "%Y-%m-%dT%H:%MZ").strftime("%m-%d-%Y")

    parsed_events = []
    for event in resp_json.get("events", []):
        competition = event.get("competitions", [])[0]  # always first item
        competitors = competition.get("competitors", [])

        home_team = next((team for team in competitors if team.get("homeAway") == "home"), {})
        away_team = next((team for team in competitors if team.get("homeAway") == "away"), {})

        home_abbr = home_team.get("team", {}).get("abbreviation", "")
        away_abbr = away_team.get("team", {}).get("abbreviation", "")
        home_score = int(home_team.get("score", 0))
        away_score = int(away_team.get("score", 0))

        winner_abbr = (
            home_abbr if home_team.get("winner") else
            away_abbr if away_team.get("winner") else None
        )

        parsed_events.append({
            "game_id": event.get("id"),
            "week_number": event.get("week", {}).get("number"),
            "short_name": event.get("shortName"),
            "season_type": event.get("season", {}).get("type"),
            "date": format_date_str(event.get("date", "")),
            "home_team_abbreviation": home_abbr,
            "away_team_abbreviation": away_abbr,
            "home_team_score": home_score,
            "away_team_score": away_score,
            "winner": winner_abbr,
        })

    return {"SEASON_SCHEDULE": parsed_events}

class SeasonSchedule(BaseEndpoint):
    REGULAR_SEASON_URL = "https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/{season_id}/types/2/weeks/1"
    POSTSEASON_URL = "https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/{season_id}/types/3/weeks/5"
    SCOREBOARD_BASE_URL = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard"

    def __init__(self, season: int = 2024):
        start = self.fetch_start_date(season)
        end = self.fetch_end_date(season)
        scoreboard_url = f"{self.SCOREBOARD_BASE_URL}?dates={start}-{end}&limit=300"

        super().__init__(
            url=scoreboard_url,
            parser=parse_scoreboard_response
        )

    def fetch_start_date(self, season: int) -> str:
        url = self.REGULAR_SEASON_URL.format(season_id=season)
        resp = httpx.get(url)
        resp.raise_for_status()
        return self.format_date(resp.json()["startDate"])

    def fetch_end_date(self, season: int) -> str:
        url = self.POSTSEASON_URL.format(season_id=season)
        resp = httpx.get(url)
        resp.raise_for_status()
        return self.format_date(resp.json()["endDate"])

    @staticmethod
    def format_date(date_str: str) -> str:
        return datetime.strptime(date_str, "%Y-%m-%dT%H:%MZ").strftime("%Y%m%d")


sched = SeasonSchedule(2024)
df = sched.get_dataset("SEASON_SCHEDULE").get_data_frame()
kc_games = df[
    (df["home_team_abbreviation"] == "KC") |
    (df["away_team_abbreviation"] == "KC")
]

print(kc_games)