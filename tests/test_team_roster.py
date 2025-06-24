from nfl_api_client.endpoints.team_roster import TeamRoster
import pytest

def test_team_roster_fetch():
    roster = TeamRoster(team_id=12)
    df = roster.get_dataset("TEAM_ROSTER").get_dataframe()
    assert not df.empty
    assert "player_id" in df.columns
    assert len(df.columns) == 16

def test_team_roster_invalid_id():
    with pytest.raises(ValueError, match="team_id: 999 is not a valid ID."):
        TeamRoster(team_id=999)