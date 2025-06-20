from nfl_api_client.endpoints.stats_leaders import StatsLeaders

if __name__ == "__main__":
    team = StatsLeaders(2024, 3, 30)
    team.get_raw_json()