import requests

def fetch_team_roster(team_id: int):
    url = f"https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams/{team_id}/roster"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    all_players = []

    for group in data.get("athletes", []):
        position_type = group.get("position")  
        for player in group.get("items", []):
            player_id = player.get("id")
            player_name = player.get("fullName")

            position_info = player.get("position", {})
            actual_position = position_info.get("displayName")

            if player_id and player_name:
                all_players.append({
                    "id": player_id,
                    "name": player_name,
                    "position_type": position_type,
                    "position": actual_position
                })

    return all_players

# Example usage
team_id = 12  # Kansas City Chiefs
roster = fetch_team_roster(team_id)
for player in roster:
    print(player)
