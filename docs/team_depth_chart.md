# Team Depth Chart

Fetches a team's depth charts for a particular season and team ID. Returns 3 datasets: `OFFENSE`, `DEFENSE`, `SPECIAL_TEAMS`. 

### Import 

``` python
from nfl_api_client.endpoints.team_depth_chart import TeamDepthChart
```

### Parameters

| **Name**   | **Type** | **Description**                                                                | **Required** |
|:-----------|:--------:|:------------------------------------------------------------                   |:------------ |
| `team_id`  | `TeamID` or `int`  | ESPN Team ID        | Yes                   |   Yes
| `season`   | `int`      | Season year in `YYYY` format. Default = `2025`        | No


### Examples

```python
from nfl_api_client.endpoints.team_depth_chart import TeamDepthChart
from nfl_api_client.lib.parameters import TeamID

# TeamDepthChart(team_id = 33, year = 2024) also works. BAL has TEAM ID = 33

ravens_depth_25 = TeamDepthChart(team_id = TeamID.BAL, year = 2024)

ravens_offense_25 = ravens_depth_25.get_dataset("OFFENSE").get_dataframe()        
ravens_defense_25 = ravens_depth_25.get_dataset("DEFENSE").get_dict()
ravens_special_25 = ravens_depth_25.get_dataset("SPECIAL_TEAMS").get_dict()        

```

### Datasets 

- `rank` is the player's rank in the pecking order for the particular position. `1` signifies first option. 


#### OFFENSE

```python
[
    "player_id"        
    "player_name"      
    "position_name"  
    "position_abbreviation" 
    "rank"  
]
```

#### DEFENSE

```python
[
    "player_id"        
    "player_name"      
    "position_name"  
    "position_abbreviation" 
    "rank"  
]
```

#### SPECIAL_TEAMS

```python
[
    "player_id"        
    "player_name"      
    "position_name"  
    "position_abbreviation" 
    "rank"  
]
```
