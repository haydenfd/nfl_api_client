from src.nfl_api_client.endpoints.player_stats import fetch_player_season_stats

if __name__ == "__main__":
    stats = fetch_player_season_stats(3139477, 2024, season_type=2)
    print(stats)