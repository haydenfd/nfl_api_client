import re
from nfl_api_client.lib.data import players, player_id_idx, player_full_name_idx

pattern = re.compile(r'/athletes/(\d+)')

def TeamDepthChartParser(json_data):
    player_lookup = {
        player[player_id_idx]: player[player_full_name_idx]
        for player in players
    }

    depth_chart = []
    for item in json_data.get("items", []):
        positions = item.get("positions", {})
        for pos_key, pos_data in positions.items():
            pos_abbr = pos_data["position"]["abbreviation"]
            for athlete_entry in pos_data.get("athletes", []):
                ref = athlete_entry["athlete"]["$ref"]
                match = pattern.search(ref)
                if match:
                    player_id = int(match.group(1))
                    player_name = player_lookup.get(player_id, "Unknown")
                    rank = athlete_entry.get("rank")

                    depth_chart.append({
                        "player_id": player_id,
                        "player_name": player_name,
                        "position_abbreviation": pos_abbr,
                        "rank": rank
                    })
    return depth_chart