from nfl_api.endpoints.team_roster import TeamRoster

if __name__ == "__main__":
    info = TeamRoster("12")
    x = info.get_df()
    print(x)