# Given a year, type of season (regular season/post season but assume regular seaosn by default =2), and conference type = 8 or 9 (assume 8 for now) as params 
# Response object contains "standings" list. Each item in standings list is an object w/ "team", "records" fields. 
# team field contains an object to a ref like this  "http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2024/teams/2?lang=en&region=us". Can parse the team id from the url and fetch the team abbreviation from TeamId type by reversal
# "records" is a list of objects, but for now just focus on the first object. It has "displayValue" and "value", displayValue is string of overall record and "value" is float of winningPercent. Return back the displayValue as overall_record, and value as winning_percent w/ the float truncated to only have the 0.764 instead of 0.764705
import httpx
from nfl_api_client.lib.parameters import TeamID
from nfl_api_client.lib.endpoint_registry import ENDPOINT_REGISTRY
import pandas as pd

class SeasonStandings:
    BASE_URL = ENDPOINT_REGISTRY["SEASON_STANDINGS"]

    def __init__(self, year: int, season_type: int = 2, conference_type: int = 8):
        self.year = year
        self.season_type = season_type
        self.conference_type = conference_type
        self.standings_data = []
        self._fetch()

    def _fetch(self):
        url = self.BASE_URL.format(
            year=self.year,
            season_type=self.season_type,
            conference_type=self.conference_type,
        )
        response = httpx.get(url)
        response.raise_for_status()
        json_data = response.json()

        for team_entry in json_data.get("standings", []):
            team_ref_url = team_entry["team"]["$ref"]
            team_id = int(team_ref_url.split("/")[-1].split("?")[0])
            team_abbr = self._get_team_abbreviation(team_id)

            record_obj = team_entry.get("records", [])[0]
            overall_record = record_obj.get("displayValue")
            winning_percent = round(float(record_obj.get("value", 0)), 3)

            stats = {}
            for stat in record_obj.get("stats", []):
                name = stat.get("name")
                if name and not name.startswith("OT"):
                    stats[name] = stat.get("value")

            self.standings_data.append({
                "team_id": team_id,
                "team_abbr": team_abbr,
                "overall_record": overall_record,
                "winning_percent": winning_percent,
                **stats
            })

    def _get_team_abbreviation(self, team_id: int) -> str:
        for abbr, enum_val in TeamID.__members__.items():
            if enum_val.value == team_id:
                return abbr
        return f"UNKNOWN_{team_id}"

    def get_data(self):
        return self.standings_data

    def get_df(self):
        return pd.DataFrame(self.standings_data)