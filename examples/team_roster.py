from nfl_api_client.endpoints.team_roster import TeamRoster
from nfl_api_client.lib.parameters import TeamID
if __name__ == "__main__":
    roster = TeamRoster(32)
    df = roster.get_dataset("TEAM_ROSTER").get_data_frame()
    print(df)