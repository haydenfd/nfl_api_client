# import pytest
# from nfl_api_client.endpoints.season_standings import SeasonStandings
# from nfl_api_client.lib.response_parsers.season_standings import (
#     SeasonStandingsLeagueParser,
#     SeasonStandingsConferenceParser,
#     SeasonStandingsDivisionParser
# )
# from nfl_api_client.lib.response_parsers.season_standings import _extract_team_data

# # Sample mock entry with minimal fields for testing _extract_team_data
# MOCK_ENTRY = {
#     "team": {
#         "id": "1",
#         "displayName": "Kansas City Chiefs",
#         "abbreviation": "KC",
#         "seed": 1,
#         "clincher": "z"
#     },
#     "stats": [
#         {"shortDisplayName": "W", "displayValue": "13"},
#         {"shortDisplayName": "L", "displayValue": "4"},
#         {"shortDisplayName": "PCT", "displayValue": ".765"},
#         {"shortDisplayName": "PF", "displayValue": "450"},
#         {"shortDisplayName": "STRK", "displayValue": "W6"},
#     ]
# }

# @pytest.fixture
# def mock_league_response():
#     return {
#         "content": {
#             "standings": {
#                 "standings": {
#                     "entries": [MOCK_ENTRY]
#                 }
#             }
#         }
#     }

# @pytest.fixture
# def mock_conference_response():
#     return {
#         "content": {
#             "standings": {
#                 "groups": [
#                     {"abbreviation": "AFC", "standings": {"entries": [MOCK_ENTRY]}},
#                     {"abbreviation": "NFC", "standings": {"entries": [MOCK_ENTRY]}}
#                 ]
#             }
#         }
#     }

# @pytest.fixture
# def mock_division_response():
#     return {
#         "content": {
#             "standings": {
#                 "groups": [
#                     {
#                         "groups": [
#                             {"name": "AFC EAST", "standings": {"entries": [MOCK_ENTRY]}},
#                             {"name": "AFC WEST", "standings": {"entries": [MOCK_ENTRY]}}
#                         ]
#                     },
#                     {
#                         "groups": [
#                             {"name": "NFC EAST", "standings": {"entries": [MOCK_ENTRY]}},
#                             {"name": "NFC WEST", "standings": {"entries": [MOCK_ENTRY]}}
#                         ]
#                     }
#                 ]
#             }
#         }
#     }

# def test_extract_team_data_maps_keys_correctly():
#     result = _extract_team_data(MOCK_ENTRY)
#     assert result["team_id"] == "1"
#     assert result["team_name"] == "Kansas City Chiefs"
#     assert result["team_code"] == "KC"
#     assert result["seed"] == 1
#     assert result["clincher"] == "Clinched Division"
#     assert result["wins"] == "13"
#     assert result["losses"] == "4"
#     assert result["win_percent"] == ".765"
#     assert result["points_for"] == "450"
#     assert result["streak"] == "W6"

# def test_league_parser_returns_league(mock_league_response):
#     result = SeasonStandingsLeagueParser(mock_league_response)
#     assert "LEAGUE" in result
#     assert len(result["LEAGUE"]) == 1
#     assert result["LEAGUE"][0]["team_name"] == "Kansas City Chiefs"

# def test_conference_parser_returns_afc_nfc(mock_conference_response):
#     result = SeasonStandingsConferenceParser(mock_conference_response)
#     assert set(result.keys()) == {"AFC", "NFC"}
#     for conference in ["AFC", "NFC"]:
#         assert len(result[conference]) == 1
#         assert result[conference][0]["team_code"] == "KC"

# def test_division_parser_returns_all_divisions(mock_division_response):
#     result = SeasonStandingsDivisionParser(mock_division_response)
#     expected_divisions = {"AFC EAST", "AFC WEST", "NFC EAST", "NFC WEST"}
#     assert set(result.keys()) == expected_divisions
#     for division in expected_divisions:
#         assert len(result[division]) == 1
#         assert result[division][0]["team_code"] == "KC"

# def test_season_standings_invalid_group_raises():
#     with pytest.raises(ValueError):
#         SeasonStandings(group="invalid")

# def test_season_standings_parser_resolution():
#     assert SeasonStandings(group="league").parser == SeasonStandingsLeagueParser
#     assert SeasonStandings(group="conference").parser == SeasonStandingsConferenceParser
#     assert SeasonStandings(group="division").parser == SeasonStandingsDivisionParser
