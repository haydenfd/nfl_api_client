import re
from nfl_api_client.lib.utils import format_date_str

pattern = re.compile(r'([A-Z]{2,4})\s+[@V]{1,2}\s+([A-Z]{2,4})')

def TeamScheduleParser(data):
    parsed = []
    for event in data.get("events", []):
        game_id = event.get("id")
        title = event.get("shortName")
        week_number = event.get("week", {}).get("number")
        date = event.get("date", {})
        match = pattern.search(title)

        home_team = away_team = "UNKNOWN"
        if match:
            team1, team2 = match.groups()
            if "@" in title:
                away_team, home_team = team1, team2
            else:
                home_team, away_team = team1, team2

        parsed.append({
            "game_id": game_id,
            "week_number": week_number,
            "name": title,
            "date": format_date_str(date),
            "home_team": home_team,
            "away_team": away_team
        })
    return parsed