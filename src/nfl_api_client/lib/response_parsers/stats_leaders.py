import re
from typing import Dict, List
from nfl_api_client.lib.utils import extract_id_from_ref
from nfl_api_client.lib.data import players, player_id_idx, player_full_name_idx
from nfl_api_client.lib.parameters import TeamID

def to_snake_upper(name: str) -> str:
    return re.sub(r"(?<=[a-zA-Z])(?=[A-Z])", "_", name).upper()

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
        name = to_snake_upper(category["name"])
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
                "player_id": player_id,
                "player_name": player_name,
                "team_id": team_id,
                "team_code": team_abbr,
                "value": value,
            })

        parsed[name] = leaders

    return parsed