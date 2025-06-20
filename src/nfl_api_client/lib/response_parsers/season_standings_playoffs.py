from typing import Dict, List, Any

CLINCHER_MAP = {
    "e": "Eliminated from Playoff Contention",
    "y": "Clinched Wild Card",
    "*": "Clinched Division and Bye",
    "z": "Clinched Division"
}

def SeasonStandingsPlayoffsParser(data: Dict[str, Any]) -> Dict[str, List[Dict[str, Any]]]:
    datasets = {}
    groups = data.get("content", {}).get("standings", {}).get("groups", [])

    for group in groups:
        group_name = group.get("abbreviation") or group.get("name")
        entries = group.get("standings", {}).get("entries", [])
        parsed_entries = []

        for entry in entries:
            team = entry.get("team", {})
            stats = entry.get("stats", [])

            team_data = {
                "TEAM_ID": team.get("id"),
                "TEAM_NAME": team.get("displayName"),
                "TEAM_ABBREVIATION": team.get("abbreviation"),
                "SEED": team.get("seed"),
                "CLINCHER": CLINCHER_MAP.get(team.get("clincher"), team.get("clincher")),
            }

            for stat in stats:
                name = stat.get("shortDisplayName")
                value = stat.get("displayValue")
                if name and value is not None:
                    team_data[name.upper()] = value or None

            parsed_entries.append(team_data)

        datasets[group_name] = parsed_entries

    return datasets
