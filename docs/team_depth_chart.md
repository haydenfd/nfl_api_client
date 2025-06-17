# Team Depth Chart

Fetches a team's depth charts for a particular season and team ID. 

### Import 

``` python
from nfl_api_client.endpoints.team_depth_chart import TeamDepthChart
```

### Parameters

| **Name**   | **Type** | **Description**                                                                |
|:-----------|:--------:|:------------------------------------------------------------                   |
| `team_id`  | `TeamID`   | The ID of the NFL team. Can use a `TeamID` or directly inject `int`          |
| `season`   | `int`      | Season year in `YYYY` format (e.g., `2024`)                                  |

### Datasets 

#### OFFENSE

```
[
    "PLAYER_ID"        
    "PLAYER_NAME"      
    "POSITION_NAME"  
    "POSITION_ABBREVIATION" 
    "RANK"  
]
```

#### DEFENSE

```
[
    "PLAYER_ID"        
    "PLAYER_NAME"      
    "POSITION_NAME"  
    "POSITION_ABBREVIATION" 
    "RANK"  
]
```

#### SPECIAL_TEAMS

```
[
    "PLAYER_ID"        
    "PLAYER_NAME"      
    "POSITION_NAME"  
    "POSITION_ABBREVIATION" 
    "RANK"  
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

<!-- ::: nfl_api_client.endpoints.team_depth_chart.TeamDepthChart
    options:
      show_source: false -->

