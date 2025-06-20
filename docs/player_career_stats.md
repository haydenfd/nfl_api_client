# Player Career Statistics (Totals)

Fetches the datasets for a player's per-season statistics for 6 categories. 

!!! Note
    Endpoint returns 6 datasets - *PASSING*, *RECEIVING*, *RUSHING*, *KICKING*, *SCORING*, *DEFENSIVE*. <br><br>However, depending on the position of the player, some data sets might be empty. For example, a Wide Receiver may not have Kicking statistics. 

### Import 

``` python
from nfl_api_client.endpoints.player_career_stats import PlayerCareerStats
```

### Parameters

| **Name**   | **Type** | **Description**                                                                |
|:-----------|:--------:|:------------------------------------------------------------                   |
| `player_id`  | `int`   | ESPN Player ID        |
| `season_type`   | `SeasonTypeID` or `int`      |     Season type                           |

### Datasets 

#### RECEIVING

```
[
    "PLAYER_ID",
    "TEAM_ID"
    "GAMES_PLAYED",
    "RECEPTIONS",
    "RECEIVING_TARGETS",
    "RECEIVING_YARDS",
    "YARDS_PER_RECEPTION",
    "RECEIVING_TOUCHDOWNS",
    "LONG_RECEPTION",
    "RECEIVING_FIRST_DOWNS",
    "RECEIVING_FUMBLES",
    "RECEIVING_FUMBLES_LOST"
]
```

#### PASSING

```
[
  "PLAYER_ID",
  "TEAM_ID"
  "GAMES_PLAYED",
  "COMPLETIONS",
  "PASSING_ATTEMPTS",
  "COMPLETION_PCT",
  "PASSING_YARDS",
  "YARD_PER_PASS_ATTEMPT",
  "PASSING_TOUCHDOWNS",
  "INTERCEPTIONS",
  "LONG_PASSING",
  "SACKS",
  "QB_RATING",
]
```

#### KICKING

```
[
    "PLAYER_ID",
    "TEAM_ID",
    "GAMES_PLAYED", 
    "RUSHING_ATTEMPTS",
    "RUSHING_YARDS",  
    "YARDS_PER_RUSH_ATTEMPT",
    "RUSHING_TOUCHDOWNS",
    "LONG_RUSHING",
    "RUSHING_FIRST_DOWNS",
    "RUSHING_FUMBLES",
    "RUSHING_FUMBLES_LOST",
]
```

#### RUSHING

```
[
    "PLAYER_ID",
    "TEAM_ID",
    "GAMES_PLAYED", 
    "RUSHING_ATTEMPTS",
    "RUSHING_YARDS",  
    "YARDS_PER_RUSH_ATTEMPT",
    "RUSHING_TOUCHDOWNS",
    "LONG_RUSHING",
    "RUSHING_FIRST_DOWNS",
    "RUSHING_FUMBLES",
    "RUSHING_FUMBLES_LOST",
]
```

#### SCORING

```
[
    "PLAYER_ID",
    "TEAM_ID",
    "GAMES_PLAYED", 
    "PASSING_TOUCHDOWNS",
    "RUSHING_TOUCHDOWNS",  
    "RECEIVING_TOUCHDOWNS",
    "RETURN_TOUCHDOWNS",
    "TOTAL_TOUCHDOWNS",
    "TOTAL_TWO_POINT_CONVS",
    "KICK_XP",
    "FIELD_GOALS",
    "TOTAL_POINTS",
]
```

#### DEFENSIVE

```
[
    "PLAYER_ID",
    "TEAM_ID",
    "GAMES_PLAYED", 
    "RUSHING_ATTEMPTS",
    "RUSHING_YARDS",  
    "YARDS_PER_RUSH_ATTEMPT",
    "RUSHING_TOUCHDOWNS",
    "LONG_RUSHING",
    "RUSHING_FIRST_DOWNS",
    "RUSHING_FUMBLES",
    "RUSHING_FUMBLES_LOST",
]
```
### Examples

```python
from nfl_api_client.endpoints.team_depth_chart import TeamDepthChart
from nfl_api_client.lib.parameters import TeamID

# TeamDepthChart(team_id = 33, year=2024) also works. BAL has TEAM ID = 33
ravens_depth_25 = TeamDepthChart(team_id = TeamID.BAL, year = 2025)

ravens_offense_25 = ravens_depth_25.get_dataset("OFFENSE").get_data_frame()        
ravens_defense_25 = ravens_depth_25.get_dataset("DEFENSE").get_dict()
ravens_special_25 = ravens_depth_25.get_dataset("SPECIAL_TEAMS").get_dict()        

```
