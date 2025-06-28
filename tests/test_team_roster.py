import pytest
from nfl_api_client.endpoints.team_roster import TeamRoster
from nfl_api_client.lib.parameters import TeamID

REQUIRED_COLUMNS = [
    "player_id",
    "first_name",
    "last_name",
    "full_name",
    "weight",
    "height",
    "age",
    "dob",
    "debut_year",
    "college",
    "jersey_number",
    "position_name",
    "position_abbreviation",
    "position_type",
    "experience",
    "image_url",
]


# def test_team_roster_valid_id():
#     roster = TeamRoster(team_id=12)
#     df = roster.get_dataset("TEAM_ROSTER").get_dataframe()
#     assert not df.empty
#     assert set(REQUIRED_COLUMNS) == set(df.columns)
#     assert df["player_id"].dtype.kind in {"i", "u"}

# def test_team_roster_enum_id():
#     roster = TeamRoster(team_id=TeamID.KC)
#     df = roster.get_dataset("TEAM_ROSTER").get_dataframe()
#     assert not df.empty
#     assert "full_name" in df.columns

# def test_team_roster_invalid_id():
#     with pytest.raises(ValueError, match="team_id: 999 is not a valid ID."):
#         TeamRoster(team_id=999)

# def test_team_roster_no_nulls():
#     df = TeamRoster(team_id=12).get_dataset("TEAM_ROSTER").get_dataframe()
#     assert not df.isnull().values.any()

# def test_team_roster_column_types():
#     df = TeamRoster(team_id=12).get_dataset("TEAM_ROSTER").get_dataframe()

#     assert df["player_id"].dtype.kind in {"i", "u"}
#     assert df["full_name"].dtype == "object"
#     assert df["experience"].dtype.kind in {"i", "u"}
#     assert df["dob"].dtype == "object"
