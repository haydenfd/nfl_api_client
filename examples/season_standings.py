from nfl_api.endpoints.season_standings import SeasonStandings

if __name__ == "__main__":
    standings = SeasonStandings(2024)
    print(standings.get_df())