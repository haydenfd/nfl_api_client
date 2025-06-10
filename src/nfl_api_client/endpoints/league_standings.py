# '''
# This gives regular season standings for AFC in 2023 - https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2023/types/2/groups/8/standings/{type}
# {type} => 0, overall standings, 1, playoff standings, 2, expanded standings, 3, div standings. 
# The Site API version for standings is pretty much useless. 
# '''

# {
#     "$ref": "http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2023/types/2/groups/8/standings/0?lang=en&region=us",
#     "id": "0",
#     "name": "overall",
#     "displayName": "Standings",
#     "standings": [
#         {
#             "team": {
#                 "$ref": "http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2023/teams/2?lang=en&region=us"
#             },
#             "records": [
#                 {
#                     "$ref": "http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2023/types/2/groups/8/teams/2/records/0?lang=en&region=us",
#                     "id": "0",
#                     "name": "overall",
#                     "abbreviation": "Any",
#                     "type": "total",
#                     "summary": "11-6",
#                     "displayValue": "11-6",
#                     "value": 0.6470588235294118,
#                     "stats": [
#                         {
#                             "name": "OTLosses",
#                             "displayName": "Overtime Losses",
#                             "shortDisplayName": "OTL",
#                             "description": "Number of Overtime Losses",
#                             "abbreviation": "OTL",
#                             "type": "otlosses",
#                             "value": 2.0,
#                             "displayValue": "2"
#                         },
#                         {
#                             "name": "OTWins",
#                             "displayName": "Overtime Wins",
#                             "shortDisplayName": "OT Wins",
#                             "description": "Number of Overtime Wins",
#                             "abbreviation": "OTW",
#                             "type": "otwins",
#                             "value": 0.0,
#                             "displayValue": "0"
#                         },
#                         {
#                             "name": "avgPointsAgainst",
#                             "displayName": "Opponent Points Per Game",
#                             "shortDisplayName": "OPTS/G",
#                             "description": "Opponent Points Per Game",
#                             "abbreviation": "OPTS/G",
#                             "type": "avgpointsagainst",
#                             "value": 18.294117,
#                             "displayValue": "18.3"
#                         },
#                         {
#                             "name": "avgPointsFor",
#                             "displayName": "Points Per Game",
#                             "shortDisplayName": "PTS/G",
#                             "description": "Points Per Game",
#                             "abbreviation": "PTS/G",
#                             "type": "avgpointsfor",
#                             "value": 26.529411,
#                             "displayValue": "26.5"
#                         },
#                         {
#                             "name": "clincher",
#                             "displayName": "Clincher",
#                             "shortDisplayName": "CLINCH",
#                             "description": "Clinched Division",
#                             "abbreviation": "CLINCH",
#                             "type": "clincher",
#                             "value": 0.0,
#                             "displayValue": "z"
#                         },
#                         {
#                             "name": "differential",
#                             "displayName": "Point Differential",
#                             "shortDisplayName": "DIFF",
#                             "description": "Point Differential",
#                             "abbreviation": "DIFF",
#                             "type": "differential",
#                             "value": 140.0,
#                             "displayValue": "+140"
#                         },
#                         {
#                             "name": "divisionWinPercent",
#                             "displayName": "Division Win Percentage",
#                             "shortDisplayName": "DPCT",
#                             "description": "Division Winning Percentage",
#                             "abbreviation": "DPCT",
#                             "type": "divisionwinpercent",
#                             "value": 0.6666667,
#                             "displayValue": "0.667"
#                         },
#                         {
#                             "name": "gamesBehind",
#                             "displayName": "Games Back",
#                             "shortDisplayName": "GB",
#                             "description": "Games Back",
#                             "abbreviation": "GB",
#                             "type": "gamesbehind",
#                             "value": 2.0,
#                             "displayValue": "2"
#                         },
#                         {
#                             "name": "gamesPlayed",
#                             "displayName": "Games Played",
#                             "shortDisplayName": "GP",
#                             "description": "Games Played",
#                             "abbreviation": "GP",
#                             "type": "gamesplayed",
#                             "value": 17.0,
#                             "displayValue": "17"
#                         },
#                         {
#                             "name": "leagueWinPercent",
#                             "displayName": "League Win Percentage",
#                             "shortDisplayName": "LPCT",
#                             "description": "League Winning Percentage",
#                             "abbreviation": "LPCT",
#                             "type": "leaguewinpercent",
#                             "value": 0.5833333,
#                             "displayValue": "0.583"
#                         },
#                         {
#                             "name": "losses",
#                             "displayName": "Losses",
#                             "shortDisplayName": "L",
#                             "description": "Losses",
#                             "abbreviation": "L",
#                             "type": "losses",
#                             "value": 6.0,
#                             "displayValue": "6"
#                         },
#                         {
#                             "name": "playoffSeed",
#                             "displayName": "Position",
#                             "shortDisplayName": "POS",
#                             "description": "Playoff Seed",
#                             "abbreviation": "SEED",
#                             "type": "playoffseed",
#                             "value": 2.0,
#                             "displayValue": "2"
#                         },
#                         {
#                             "name": "pointDifferential",
#                             "displayName": "Point Differential",
#                             "shortDisplayName": "DIFF",
#                             "description": "Point Differential",
#                             "abbreviation": "DIFF",
#                             "type": "pointdifferential",
#                             "value": 140.0,
#                             "displayValue": "+140"
#                         },
#                         {
#                             "name": "points",
#                             "displayName": "Points",
#                             "shortDisplayName": "PTS",
#                             "description": "Total Points",
#                             "abbreviation": "PTS",
#                             "type": "points",
#                             "value": 2.5,
#                             "displayValue": "2.5"
#                         },
#                         {
#                             "name": "pointsAgainst",
#                             "displayName": "Points Against",
#                             "shortDisplayName": "PA",
#                             "description": "Total Points Against",
#                             "abbreviation": "PA",
#                             "type": "pointsagainst",
#                             "value": 311.0,
#                             "displayValue": "311"
#                         },
#                         {
#                             "name": "pointsFor",
#                             "displayName": "Points For",
#                             "shortDisplayName": "PF",
#                             "description": "Total Points For",
#                             "abbreviation": "PF",
#                             "type": "pointsfor",
#                             "value": 451.0,
#                             "displayValue": "451"
#                         },
#                         {
#                             "name": "streak",
#                             "displayName": "Streak",
#                             "shortDisplayName": "STRK",
#                             "description": "Current Streak",
#                             "abbreviation": "STRK",
#                             "type": "streak",
#                             "value": 5.0,
#                             "displayValue": "W5"
#                         },
#                         {
#                             "name": "ties",
#                             "displayName": "Ties",
#                             "shortDisplayName": "T",
#                             "description": "Ties",
#                             "abbreviation": "T",
#                             "type": "ties",
#                             "value": 0.0,
#                             "displayValue": "0"
#                         },
#                         {
#                             "name": "winPercent",
#                             "displayName": "Win Percentage",
#                             "shortDisplayName": "PCT",
#                             "description": "Winning Percentage",
#                             "abbreviation": "PCT",
#                             "type": "winpercent",
#                             "value": 0.64705884,
#                             "displayValue": ".647"
#                         },
#                         {
#                             "name": "wins",
#                             "displayName": "Wins",
#                             "shortDisplayName": "W",
#                             "description": "Wins",
#                             "abbreviation": "W",
#                             "type": "wins",
#                             "value": 11.0,
#                             "displayValue": "11"
#                         },
#                         {
#                             "name": "divisionLosses",
#                             "displayName": "Division Losses",
#                             "shortDisplayName": "DL",
#                             "description": "Division Losses",
#                             "abbreviation": "DL",
#                             "type": "divisionlosses",
#                             "value": 2.0,
#                             "displayValue": "2"
#                         },
#                         {
#                             "name": "divisionRecord",
#                             "displayName": "Division record",
#                             "shortDisplayName": "DIV",
#                             "description": "Division Record",
#                             "abbreviation": "DIV",
#                             "type": "divisionrecord",
#                             "value": 0.0,
#                             "displayValue": "4-2"
#                         },
#                         {
#                             "name": "divisionTies",
#                             "displayName": "Division Tie ",
#                             "shortDisplayName": "DT",
#                             "description": "Division Tie ",
#                             "abbreviation": "DT",
#                             "type": "divisionties",
#                             "value": 0.0,
#                             "displayValue": "0.000"
#                         },
#                         {
#                             "name": "divisionWins",
#                             "displayName": "Division Wins ",
#                             "shortDisplayName": "DW",
#                             "description": "Division Winning ",
#                             "abbreviation": "DW",
#                             "type": "divisionwins",
#                             "value": 4.0,
#                             "displayValue": "4.000"
#                         }
#                     ]
#                 },
#                 {
#                     "$ref": "http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2023/types/2/groups/8/teams/2/records/13?lang=en&region=us",
#                     "id": "13",
#                     "name": "Home",
#                     "displayName": "Home",
#                     "shortDisplayName": "HOME",
#                     "description": "Home Record",
#                     "type": "home",
#                     "summary": "7-2",
#                     "displayValue": "7-2",
#                     "value": 0.7777777777777778,
#                     "stats": [
#                         {
#                             "name": "wins",
#                             "displayName": "Wins",
#                             "shortDisplayName": "W",
#                             "description": "Wins",
#                             "abbreviation": "W",
#                             "type": "wins",
#                             "value": 7.0,
#                             "displayValue": "7"
#                         },
#                         {
#                             "name": "losses",
#                             "displayName": "Losses",
#                             "shortDisplayName": "L",
#                             "description": "Losses",
#                             "abbreviation": "L",
#                             "type": "losses",
#                             "value": 2.0,
#                             "displayValue": "2"
#                         },
#                         {
#                             "name": "ties",
#                             "displayName": "Ties",
#                             "shortDisplayName": "T",
#                             "description": "Ties",
#                             "abbreviation": "T",
#                             "type": "ties",
#                             "value": 0.0,
#                             "displayValue": "0"
#                         },
#                         {
#                             "name": "winPercent",
#                             "displayName": "Win Percentage",
#                             "shortDisplayName": "PCT",
#                             "description": "Winning Percentage",
#                             "abbreviation": "PCT",
#                             "type": "winpercent",
#                             "value": 0.7777777910232544,
#                             "displayValue": ".778"
#                         },
#                         {
#                             "name": "OTLosses",
#                             "displayName": "Overtime Losses",
#                             "shortDisplayName": "OTL",
#                             "description": "Number of Overtime Losses",
#                             "abbreviation": "OTL",
#                             "type": "otlosses",
#                             "value": 0.0,
#                             "displayValue": "0"
#                         }
#                     ]
#                 },
#                 {
#                     "$ref": "http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2023/types/2/groups/8/teams/2/records/14?lang=en&region=us",
#                     "id": "14",
#                     "name": "Road",
#                     "displayName": "Road",
#                     "shortDisplayName": "AWAY",
#                     "description": "Away Record",
#                     "type": "road",
#                     "summary": "4-4",
#                     "displayValue": "4-4",
#                     "value": 0.5,
#                     "stats": [
#                         {
#                             "name": "wins",
#                             "displayName": "Wins",
#                             "shortDisplayName": "W",
#                             "description": "Wins",
#                             "abbreviation": "W",
#                             "type": "wins",
#                             "value": 4.0,
#                             "displayValue": "4"
#                         },
#                         {
#                             "name": "losses",
#                             "displayName": "Losses",
#                             "shortDisplayName": "L",
#                             "description": "Losses",
#                             "abbreviation": "L",
#                             "type": "losses",
#                             "value": 4.0,
#                             "displayValue": "4"
#                         },
#                         {
#                             "name": "ties",
#                             "displayName": "Ties",
#                             "shortDisplayName": "T",
#                             "description": "Ties",
#                             "abbreviation": "T",
#                             "type": "ties",
#                             "value": 0.0,
#                             "displayValue": "0"
#                         },
#                         {
#                             "name": "winPercent",
#                             "displayName": "Win Percentage",
#                             "shortDisplayName": "PCT",
#                             "description": "Winning Percentage",
#                             "abbreviation": "PCT",
#                             "type": "winpercent",
#                             "value": 0.5,
#                             "displayValue": ".500"
#                         },
#                         {
#                             "name": "OTLosses",
#                             "displayName": "Overtime Losses",
#                             "shortDisplayName": "OTL",
#                             "description": "Number of Overtime Losses",
#                             "abbreviation": "OTL",
#                             "type": "otlosses",
#                             "value": 2.0,
#                             "displayValue": "2"
#                         }
#                     ]
#                 },
#                 {
#                     "$ref": "http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2023/types/2/groups/8/teams/2/records/17?lang=en&region=us",
#                     "id": "17",
#                     "name": "vs. Div.",
#                     "displayName": "DIV",
#                     "shortDisplayName": "DIV",
#                     "description": "Division Record",
#                     "type": "vsdiv",
#                     "summary": "4-2",
#                     "displayValue": "4-2",
#                     "value": 0.6666666666666666,
#                     "stats": [
#                         {
#                             "name": "divisionWins",
#                             "displayName": "Division Wins ",
#                             "shortDisplayName": "DW",
#                             "description": "Division Winning ",
#                             "abbreviation": "DW",
#                             "type": "divisionwins",
#                             "value": 4.0,
#                             "displayValue": "4.000"
#                         },
#                         {
#                             "name": "divisionLosses",
#                             "displayName": "Division Losses",
#                             "shortDisplayName": "DL",
#                             "description": "Division Losses",
#                             "abbreviation": "DL",
#                             "type": "divisionlosses",
#                             "value": 2.0,
#                             "displayValue": "2"
#                         },
#                         {
#                             "name": "divisionTies",
#                             "displayName": "Division Tie ",
#                             "shortDisplayName": "DT",
#                             "description": "Division Tie ",
#                             "abbreviation": "DT",
#                             "type": "divisionties",
#                             "value": 0.0,
#                             "displayValue": "0.000"
#                         },
#                         {
#                             "name": "divisionWinPercent",
#                             "displayName": "Division Win Percentage",
#                             "shortDisplayName": "DPCT",
#                             "description": "Division Winning Percentage",
#                             "abbreviation": "DPCT",
#                             "type": "divisionwinpercent",
#                             "value": 0.6666666865348816,
#                             "displayValue": "0.667"
#                         },
#                         {
#                             "name": "OTLosses",
#                             "displayName": "Overtime Losses",
#                             "shortDisplayName": "OTL",
#                             "description": "Number of Overtime Losses",
#                             "abbreviation": "OTL",
#                             "type": "otlosses",
#                             "value": 1.0,
#                             "displayValue": "1"
#                         }
#                     ]
#                 },
#                 {
#                     "$ref": "http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2023/types/2/groups/8/teams/2/records/906?lang=en&region=us",
#                     "id": "906",
#                     "name": "vs. Conf.",
#                     "displayName": "CONF",
#                     "shortDisplayName": "CONF",
#                     "description": "Conference Record",
#                     "type": "vsconf",
#                     "summary": "7-5",
#                     "displayValue": "7-5",
#                     "value": 0.5833333333333334,
#                     "stats": [
#                         {
#                             "name": "wins",
#                             "displayName": "Wins",
#                             "shortDisplayName": "W",
#                             "description": "Wins",
#                             "abbreviation": "W",
#                             "type": "wins",
#                             "value": 7.0,
#                             "displayValue": "7"
#                         },
#                         {
#                             "name": "losses",
#                             "displayName": "Losses",
#                             "shortDisplayName": "L",
#                             "description": "Losses",
#                             "abbreviation": "L",
#                             "type": "losses",
#                             "value": 5.0,
#                             "displayValue": "5"
#                         },
#                         {
#                             "name": "ties",
#                             "displayName": "Ties",
#                             "shortDisplayName": "T",
#                             "description": "Ties",
#                             "abbreviation": "T",
#                             "type": "ties",
#                             "value": 0.0,
#                             "displayValue": "0"
#                         },
#                         {
#                             "name": "leagueWinPercent",
#                             "displayName": "League Win Percentage",
#                             "shortDisplayName": "LPCT",
#                             "description": "League Winning Percentage",
#                             "abbreviation": "LPCT",
#                             "type": "leaguewinpercent",
#                             "value": 0.5833333134651184,
#                             "displayValue": "0.583"
#                         },
#                         {
#                             "name": "OTLosses",
#                             "displayName": "Overtime Losses",
#                             "shortDisplayName": "OTL",
#                             "description": "Number of Overtime Losses",
#                             "abbreviation": "OTL",
#                             "type": "otlosses",
#                             "value": 1.0,
#                             "displayValue": "1"
#                         }
#                     ]
#                 }
#             ]
#         },
#         {
#             "team": {
#                 "$ref": "http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2023/teams/12?lang=en&region=us"
#             },
#             "records": [
#                 {
#                     "$ref": "http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2023/types/2/groups/8/teams/12/records/0?lang=en&region=us",
#                     "id": "0",
#                     "name": "overall",
#                     "abbreviation": "Any",
#                     "type": "total",
#                     "summary": "11-6",
#                     "displayValue": "11-6",
#                     "value": 0.6470588235294118,
#                     "stats": [
#                         {
#                             "name": "OTLosses",
#                             "displayName": "Overtime Losses",
#                             "shortDisplayName": "OTL",
#                             "description": "Number of Overtime Losses",
#                             "abbreviation": "OTL",
#                             "type": "otlosses",
#                             "value": 0.0,
#                             "displayValue": "0"
#                         },
#                         {
#                             "name": "OTWins",
#                             "displayName": "Overtime Wins",
#                             "shortDisplayName": "OT Wins",
#                             "description": "Number of Overtime Wins",
#                             "abbreviation": "OTW",
#                             "type": "otwins",
#                             "value": 0.0,
#                             "displayValue": "0"
#                         },
#                         {
#                             "name": "avgPointsAgainst",
#                             "displayName": "Opponent Points Per Game",
#                             "shortDisplayName": "OPTS/G",
#                             "description": "Opponent Points Per Game",
#                             "abbreviation": "OPTS/G",
#                             "type": "avgpointsagainst",
#                             "value": 17.294117,
#                             "displayValue": "17.3"
#                         },
#                         {
#                             "name": "avgPointsFor",
#                             "displayName": "Points Per Game",
#                             "shortDisplayName": "PTS/G",
#                             "description": "Points Per Game",
#                             "abbreviation": "PTS/G",
#                             "type": "avgpointsfor",
#                             "value": 21.82353,
#                             "displayValue": "21.8"
#                         },
#                         {
#                             "name": "clincher",
#                             "displayName": "Clincher",
#                             "shortDisplayName": "CLINCH",
#                             "description": "Clinched Division",
#                             "abbreviation": "CLINCH",
#                             "type": "clincher",
#                             "value": 0.0,
#                             "displayValue": "z"
#                         },
#                         {
#                             "name": "differential",
#                             "displayName": "Point Differential",
#                             "shortDisplayName": "DIFF",
#                             "description": "Point Differential",
#                             "abbreviation": "DIFF",
#                             "type": "differential",
#                             "value": 77.0,
#                             "displayValue": "+77"
#                         },
#                         {
#                             "name": "divisionWinPercent",
#                             "displayName": "Division Win Percentage",
#                             "shortDisplayName": "DPCT",
#                             "description": "Division Winning Percentage",
#                             "abbreviation": "DPCT",
#                             "type": "divisionwinpercent",
#                             "value": 0.6666667,
#                             "displayValue": "0.667"
#                         },
#                         {
#                             "name": "gamesBehind",
#                             "displayName": "Games Back",
#                             "shortDisplayName": "GB",
#                             "description": "Games Back",
#                             "abbreviation": "GB",
#                             "type": "gamesbehind",
#                             "value": 2.0,
#                             "displayValue": "2"
#                         },
#                         {
#                             "name": "gamesPlayed",
#                             "displayName": "Games Played",
#                             "shortDisplayName": "GP",
#                             "description": "Games Played",
#                             "abbreviation": "GP",
#                             "type": "gamesplayed",
#                             "value": 17.0,
#                             "displayValue": "17"
#                         },
#                         {
#                             "name": "leagueWinPercent",
#                             "displayName": "League Win Percentage",
#                             "shortDisplayName": "LPCT",
#                             "description": "League Winning Percentage",
#                             "abbreviation": "LPCT",
#                             "type": "leaguewinpercent",
#                             "value": 0.75,
#                             "displayValue": "0.750"
#                         },
#                         {
#                             "name": "losses",
#                             "displayName": "Losses",
#                             "shortDisplayName": "L",
#                             "description": "Losses",
#                             "abbreviation": "L",
#                             "type": "losses",
#                             "value": 6.0,
#                             "displayValue": "6"
#                         },
#                         {
#                             "name": "playoffSeed",
#                             "displayName": "Position",
#                             "shortDisplayName": "POS",
#                             "description": "Playoff Seed",
#                             "abbreviation": "SEED",
#                             "type": "playoffseed",
#                             "value": 3.0,
#                             "displayValue": "3"
#                         },
#                         {
#                             "name": "pointDifferential",
#                             "displayName": "Point Differential",
#                             "shortDisplayName": "DIFF",
#                             "description": "Point Differential",
#                             "abbreviation": "DIFF",
#                             "type": "pointdifferential",
#                             "value": 77.0,
#                             "displayValue": "+77"
#                         },
#                         {
#                             "name": "points",
#                             "displayName": "Points",
#                             "shortDisplayName": "PTS",
#                             "description": "Total Points",
#                             "abbreviation": "PTS",
#                             "type": "points",
#                             "value": 2.5,
#                             "displayValue": "2.5"
#                         },
#                         {
#                             "name": "pointsAgainst",
#                             "displayName": "Points Against",
#                             "shortDisplayName": "PA",
#                             "description": "Total Points Against",
#                             "abbreviation": "PA",
#                             "type": "pointsagainst",
#                             "value": 294.0,
#                             "displayValue": "294"
#                         },
#                         {
#                             "name": "pointsFor",
#                             "displayName": "Points For",
#                             "shortDisplayName": "PF",
#                             "description": "Total Points For",
#                             "abbreviation": "PF",
#                             "type": "pointsfor",
#                             "value": 371.0,
#                             "displayValue": "371"
#                         },
#                         {
#                             "name": "streak",
#                             "displayName": "Streak",
#                             "shortDisplayName": "STRK",
#                             "description": "Current Streak",
#                             "abbreviation": "STRK",
#                             "type": "streak",
#                             "value": 2.0,
#                             "displayValue": "W2"
#                         },
#                         {
#                             "name": "ties",
#                             "displayName": "Ties",
#                             "shortDisplayName": "T",
#                             "description": "Ties",
#                             "abbreviation": "T",
#                             "type": "ties",
#                             "value": 0.0,
#                             "displayValue": "0"
#                         },
#                         {
#                             "name": "winPercent",
#                             "displayName": "Win Percentage",
#                             "shortDisplayName": "PCT",
#                             "description": "Winning Percentage",
#                             "abbreviation": "PCT",
#                             "type": "winpercent",
#                             "value": 0.64705884,
#                             "displayValue": ".647"
#                         },
#                         {
#                             "name": "wins",
#                             "displayName": "Wins",
#                             "shortDisplayName": "W",
#                             "description": "Wins",
#                             "abbreviation": "W",
#                             "type": "wins",
#                             "value": 11.0,
#                             "displayValue": "11"
#                         },
#                         {
#                             "name": "divisionLosses",
#                             "displayName": "Division Losses",
#                             "shortDisplayName": "DL",
#                             "description": "Division Losses",
#                             "abbreviation": "DL",
#                             "type": "divisionlosses",
#                             "value": 2.0,
#                             "displayValue": "2"
#                         },
#                         {
#                             "name": "divisionRecord",
#                             "displayName": "Division record",
#                             "shortDisplayName": "DIV",
#                             "description": "Division Record",
#                             "abbreviation": "DIV",
#                             "type": "divisionrecord",
#                             "value": 0.0,
#                             "displayValue": "4-2"
#                         },
#                         {
#                             "name": "divisionTies",
#                             "displayName": "Division Tie ",
#                             "shortDisplayName": "DT",
#                             "description": "Division Tie ",
#                             "abbreviation": "DT",
#                             "type": "divisionties",
#                             "value": 0.0,
#                             "displayValue": "0.000"
#                         },
#                         {
#                             "name": "divisionWins",
#                             "displayName": "Division Wins ",
#                             "shortDisplayName": "DW",
#                             "description": "Division Winning ",
#                             "abbreviation": "DW",
#                             "type": "divisionwins",
#                             "value": 4.0,
#                             "displayValue": "4.000"
#                         }
#                     ]
#                 },