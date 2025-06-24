import re
def camel_to_snake_case(name: str) -> str:
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()

def GameTeamStatsParser(data):
    boxscore = data.get("boxscore", {})
    teams_data = boxscore.get("teams", [])

    parsed_teams = []

    for entry in teams_data:
        team_info = entry.get("team", {})
        home_away = entry.get("homeAway")
        stats_list = entry.get("statistics", [])

        stats_dict = {
            camel_to_snake_case(stat.get("name")): stat.get("displayValue")
            for stat in stats_list
        }

        parsed_teams.append({
            "team_id": team_info.get("id"),
            "team_code": team_info.get("abbreviation"),
            "team_name": team_info.get("displayName"),
            "home_or_away": home_away,
            **stats_dict
        })
    print(parsed_teams[0].keys())
    return {"TEAM_STATS": parsed_teams}