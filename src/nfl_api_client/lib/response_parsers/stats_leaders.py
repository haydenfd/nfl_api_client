import re
from typing import Dict, List
from nfl_api_client.lib.utils import extract_id_from_ref
from nfl_api_client.lib.data import players, player_id_idx, player_full_name_idx
from nfl_api_client.lib.parameters import TeamID


def StatsLeadersParser(response_json: dict) -> Dict[str, List[Dict]]:
    """
    Parses the ESPN stat leaders endpoint JSON into a dictionary of categories.

    Returns a dictionary where each key is the category name (uppercase) and
    each value is a list of stat leader dictionaries.
    """
    player_lookup = {
        player[player_id_idx]: player[player_full_name_idx]
        for player in players
    }

    categories = response_json.get("categories", [])
    parsed = {}

    for category in categories:
        name = category["name"].upper()
        leaders = []

        for leader in category.get("leaders", []):
            player_id = extract_id_from_ref(leader["athlete"]["$ref"], "athletes")
            team_id = extract_id_from_ref(leader["team"]["$ref"], "teams")
            value = leader.get("value")

            player_name = player_lookup.get(player_id, "Unknown")

            try:
                team_abbr = TeamID(team_id).name
            except ValueError:
                team_abbr = f"Team {team_id}"

            leaders.append({
                "PLAYER_ID": player_id,
                "PLAYER_NAME": player_name,
                "TEAM_ID": team_id,
                "TEAM_ABBREVIATION": team_abbr,
                "VALUE": value,
            })

        parsed[name] = leaders

    return parsed