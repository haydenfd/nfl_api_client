import re
from typing import Dict, List
from nfl_api_client.lib.data import players, player_id_idx, player_full_name_idx

pattern = re.compile(r'/athletes/(\d+)')
player_lookup = {
    player[player_id_idx]: player[player_full_name_idx]
    for player in players
}

def TeamDepthChartParser(json_data) -> Dict[str, List[Dict]]:
    chart = {"OFFENSE": [], "DEFENSE": [], "SPECIAL_TEAMS": []}
    type_keys = ["DEFENSE", "SPECIAL_TEAMS", "OFFENSE"]

    for i, item in enumerate(json_data.get("items", [])):
        group_key = type_keys[i] if i < len(type_keys) else f"GROUP_{i}"
        positions = item.get("positions", {})

        for pos_data in positions.values():
            pos_info = pos_data.get("position", {})
            display_name = pos_info.get("displayName")
            abbreviation = pos_info.get("abbreviation")

            for athlete_entry in pos_data.get("athletes", []):
                ref = athlete_entry.get("athlete", {}).get("$ref", "")
                match = pattern.search(ref)
                athlete_id = int(match.group(1)) if match else None
                rank = athlete_entry.get("rank")
                player_name = player_lookup.get(athlete_id, "Unknown")

                if athlete_id:
                    chart[group_key].append({
                        "player_id": athlete_id,
                        "player_name": player_name,
                        "position_name": display_name,
                        "position_abbreviation": abbreviation,
                        "rank": rank,
                    })

    return chart