# Team Depth Chart

Fetches a team's depth charts for a particular season and team ID. Returns 3 datasets: `OFFENSE`, `DEFENSE`, `SPECIAL_TEAMS`. 

## **Import** 

``` python
from nfl_api_client.endpoints.team_depth_chart import TeamDepthChart
```

## **Parameters**

| **Name**   | **Type** | **Description**                                                                | **Required** |
|:-----------|:--------:|:------------------------------------------------------------                   |:------------ |
| `team_id`  | `TeamID` or `int`  | ESPN Team ID        | Yes                   |   Yes |
| `season`   | `int`      | Season year in `YYYY` format. Default = `2025`        | No | 


## **Examples**

```python
from nfl_api_client.endpoints.team_depth_chart import TeamDepthChart
from nfl_api_client.lib.parameters import TeamID

# TeamDepthChart(team_id = 33, year = 2024) also works. BAL has ID = 33

ravens_depth_25 = TeamDepthChart(team_id = TeamID.BAL, year = 2024)

ravens_offense = ravens_depth_25.get_dataset("OFFENSE").get_dataframe()        
ravens_defense = ravens_depth_25.get_dataset("DEFENSE").get_dict()
ravens_special = ravens_depth_25.get_dataset("SPECIAL_TEAMS").get_dict()        
```

## **Datasets** 

```python
["OFFENSE", "DEFENSE", "SPECIAL_TEAMS"]
```


## **Data Fields**

All 3 of the above datasets return the same keys. 

```python
{
    "player_id": str    
    "player_name": str   
    "position_name": str
    "position_abbreviation": str
    "rank": int
}
```

!!! NOTE
    The `rank` data field indicates the player's position in the depth chart hierarchy for their role. `1` indicates starter/first choice. 

