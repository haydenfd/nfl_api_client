import pytest
from nfl_api_client.endpoints.team_depth_chart import TeamDepthChart
from nfl_api_client.lib.parameters import TeamID

REQUIRED_COLUMNS = [
    "player_id",
    "player_name",
    "position_name",
    "position_abbreviation",
    "rank",
]

@pytest.fixture
def chart():
    return TeamDepthChart(team_id=33, year=2024)

def test_datasets_present(chart):
    for dataset_name in ["OFFENSE", "DEFENSE", "SPECIAL_TEAMS"]:
        df = chart.get_dataset(dataset_name).get_dataframe()
        assert not df.empty, f"{dataset_name} dataset is empty or missing"


def test_dataset_shapes_and_columns(chart):
    for dataset_name in ["OFFENSE", "DEFENSE", "SPECIAL_TEAMS"]:
        df = chart.get_dataset(dataset_name).get_dataframe()
        assert not df.empty, f"{dataset_name} dataset is empty"
        assert list(df.columns) == REQUIRED_COLUMNS, f"{dataset_name} column mismatch"

def test_no_nulls(chart):
    for dataset_name in ["OFFENSE", "DEFENSE", "SPECIAL_TEAMS"]:
        df = chart.get_dataset(dataset_name).get_dataframe()
        assert not df.isnull().values.any(), f"{dataset_name} contains NaNs"

def test_column_types(chart):
    df = chart.get_dataset("OFFENSE").get_dataframe()
    assert df["player_id"].dtype.kind in {"i", "u"}, "player_id should be int"
    assert df["player_name"].dtype == "object"
    assert df["position_name"].dtype == "object"
    assert df["position_abbreviation"].dtype == "object"
    assert df["rank"].dtype.kind in {"i", "u"}, "rank should be int"

def test_valid_team_id_enum():
    chart = TeamDepthChart(team_id=TeamID.BAL, year=2024)
    df = chart.get_dataset("OFFENSE").get_dataframe()
    assert not df.empty

def test_invalid_team_id_raises():
    with pytest.raises(ValueError, match=r"team_id: .* is not a valid ID"):
        TeamDepthChart(team_id=9999, year=2024)