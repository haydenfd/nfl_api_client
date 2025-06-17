import re
from typing import Dict, List
from nfl_api_client.lib.utils import format_date_str

pattern = re.compile(r'([A-Z]{2,4})\s+[@V]{1,2}\s+([A-Z]{2,4})')

def TeamScheduleParser(data: dict) -> Dict[str, List[Dict]]:
    """
    Parses ESPN team schedule data into a structured dictionary with one dataset: "SCHEDULE".
    """
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
            "WEEK_NUMBER": week_number,
            "DATE": format_date_str(date),
            "GAME_ID": game_id,
            "GAME_TITLE": title,
            "HOME_TEAM": home_team,
            "AWAY_TEAM": away_team,
        })

    return {"TEAM_SCHEDULE": parsed}