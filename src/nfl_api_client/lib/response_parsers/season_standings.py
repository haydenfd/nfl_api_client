from typing import Dict, List, Any

CLINCHER_MAP = {
    "e": "Eliminated from Playoff Contention",
    "y": "Clinched Wild Card",
    "*": "Clinched Division and Bye",
    "z": "Clinched Division"
}


def _extract_team_data(entry: Dict[str, Any]) -> Dict[str, Any]:
    team = entry.get("team", {})
    stats = entry.get("stats", [])

    team_data = {
        "team_id": team.get("id"),
        "team_code": team.get("abbreviation"),
        "team_name": team.get("displayName"),
        "conference_seed": team.get("seed"),
        "clincher": CLINCHER_MAP.get(team.get("clincher"), team.get("clincher")),
    }

    for stat in stats:
        name = stat.get("abbreviation")
        value = stat.get("displayValue") or "0-0"
        if name and value is not None:
            team_data[name.lower()] = value

    return team_data


def SeasonStandingsLeagueParser(data: Dict[str, Any]) -> Dict[str, List[Dict[str, Any]]]:
    entries = data.get("content", {}).get("standings", {}).get("standings", {}).get("entries", [])
    return {"LEAGUE": [_extract_team_data(entry) for entry in entries]}


def SeasonStandingsConferenceParser(data: Dict[str, Any]) -> Dict[str, List[Dict[str, Any]]]:
    datasets = {}
    groups = data.get("content", {}).get("standings", {}).get("groups", [])

    for group in groups:
        group_name = group.get("abbreviation") or group.get("name")
        entries = group.get("standings", {}).get("entries", [])
        datasets[group_name.upper()] = [_extract_team_data(entry) for entry in entries]

    return datasets


def SeasonStandingsDivisionParser(data: Dict[str, Any]) -> Dict[str, List[Dict[str, Any]]]:
    datasets = {}
    conferences = data.get("content", {}).get("standings", {}).get("groups", [])

    for conference in conferences:
        divisions = conference.get("groups", [])
        for division in divisions:
            division_name = division.get("name")
            entries = division.get("standings", {}).get("entries", [])
            datasets[division_name.upper()] = [_extract_team_data(entry) for entry in entries]

    return datasets