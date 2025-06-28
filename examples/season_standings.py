from nfl_api_client.endpoints.season_standings import SeasonStandings


standings_league_view = SeasonStandings(season=2024, group="league")

print(standings_league_view.get_dataset("LEAGUE").get_dataframe())

standings_conf_view = SeasonStandings(season=2023, group="conference")

print(standings_conf_view.get_all_dataset_names())

print(standings_conf_view.get_dataset("NFC").get_dataframe())

standings_div_view = SeasonStandings(season=2024, group="division")

print(standings_div_view.get_all_dataset_names())
