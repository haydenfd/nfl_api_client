from nfl_api_client.endpoints.staging_standings import SeasonStandings

if __name__ == "__main__":
    standings = SeasonStandings(2024)
    print(standings.get_df())

