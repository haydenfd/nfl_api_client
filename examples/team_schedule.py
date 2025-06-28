from nfl_api_client.endpoints.team_schedule import TeamSchedule

schedule = TeamSchedule(team_id=12, season=2025)

print(schedule.get_url())
df = schedule.get_dataset("TEAM_SCHEDULE").get_dataframe()  

print(df)