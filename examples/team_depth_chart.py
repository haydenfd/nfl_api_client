from nfl_api.endpoints.team_depth_chart import TeamDepthChart
import re
from nfl_api.lib.data import players

pattern = re.compile(r'/athletes/(\d+)')

id_to_name = {entry[0]: entry[1] for entry in players}

def parse_depth_charts(data, resolve_names=True):
    items = data.get("items", [])
    result = {}

    for item in items:
        positions = item.get("positions", {})
        for pos_key, pos_data in positions.items():
            names_or_ids = []
            for entry in pos_data.get("athletes", []):
                ref_url = entry.get("athlete", {}).get("$ref", "")
                match = pattern.search(ref_url)
                if match:
                    player_id = int(match.group(1))
                    if resolve_names:
                        name = id_to_name.get(player_id, f"Unknown ({player_id})")
                        names_or_ids.append(name)
                    else:
                        names_or_ids.append(player_id)
            if names_or_ids:
                result[pos_key] = names_or_ids

    return result


def main():
    depth_chart = TeamDepthChart(team_id=12)
    data = depth_chart.get_dict()
    print(parse_depth_charts(data))


if __name__ == "__main__":
    main()