from typing import Dict, List
from nfl_api_client.lib.utils import format_utc_date_str
from nfl_api_client.lib.parameters import TeamID, SeasonTypeID

team_code_to_id_map = {team.name: team.value for team in TeamID}

def TeamScheduleParser(data: dict) -> Dict[str, List[Dict]]:
    """
    Parses ESPN team schedule data into a structured dictionary with one dataset: "TEAM_SCHEDULE".
    Uses `competitors.homeAway` to determine home and away teams.
    """
    parsed = []

    for event in data.get("events", []):
        game_id = event.get("id")
        title = event.get("shortName", "")
        week_number = event.get("week", {}).get("number")
        season_type = SeasonTypeID(event.get("seasonType", {}).get("type")).name
        date = event.get("date", "")

        home_team_code = away_team_code = "UNKNOWN"
        home_team_id = away_team_id = None

        competitors = event.get("competitions", [{}])[0].get("competitors", [])
        for team_entry in competitors:
            team_info = team_entry.get("team", {})
            team_code = team_info.get("abbreviation", "UNKNOWN")
            team_id = int(team_info.get("id"))

            if team_entry.get("homeAway") == "home":
                home_team_code = team_code
                home_team_id = team_id
            elif team_entry.get("homeAway") == "away":
                away_team_code = team_code
                away_team_id = team_id

        parsed.append({
            "game_id": game_id,
            "week_number": week_number,
            "season_type": season_type,
            "date": format_utc_date_str(date),
            "game_title": title,
            "home_team_id": home_team_id,
            "home_team_code": home_team_code,
            "away_team_id": away_team_id,
            "away_team_code": away_team_code,
        })

    return {"TEAM_SCHEDULE": parsed}


'''
    # Need to add (for past games, especially) - attendance, venue.city, away_team_score, home_team_score, status, game_winner
    # If upcoming schedule, then don't add the attendance, game info, obviously. 
    # Also, the date formatter needs to be fixed. I realize that it gives it in UTC timezone. Might be better to just convert to East Coast time and date, THEN format. 
'''