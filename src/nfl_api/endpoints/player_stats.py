import requests

def fetch_player_season_stats(athlete_id, season, season_type=2):
    url = f"https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/{season}/types/{season_type}/athletes/{athlete_id}/statistics"
    response = requests.get(url, params={"lang": "en", "region": "us"})
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    stats = fetch_player_season_stats(3139477, 2024, season_type=2)
    print(stats)
