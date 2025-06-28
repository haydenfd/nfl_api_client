from nfl_api_client.endpoints.team_roster import TeamRoster
from nfl_api_client.lib.parameters import TeamID


_roster = TeamRoster(team_id=12)
print(_roster.get_url())
chiefs_roster = _roster.get_dataset("TEAM_ROSTER").get_dataframe()
# print(chiefs_roster.get_dataset("TEAM_ROSTER").get_dataframe())
subset = chiefs_roster[["full_name", "college"]]

missing_info = subset

print(missing_info)

# debut year is useless. 
# Experience is for how many years since they've been in the league. 
# age needs to be typecast to int. Cannot be because of pandas quirk in dataframes
# age shows up as NaN and dob None for rookies
