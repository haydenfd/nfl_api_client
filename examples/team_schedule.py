from nfl_api.endpoints.team_schedule import TeamSchedule

if __name__ == "__main__":
    team = TeamSchedule(12, 2025)
    print(team.get_df())
    print(team.get_url())