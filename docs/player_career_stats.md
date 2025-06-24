# Player Career Statistics (Basic)

Returns the players per-season career statistics given an ESPN player ID. Returns 5 datasets: `PASSING`, `RUSHING`, `RECEIVING`, `DEFENSE`, `SCORING`. 


## Import 

``` python
from nfl_api_client.endpoints.player_career_stats import PlayerCareerStats
```

## Parameters

| **Name**   | **Type** | **Description**                                                                | **Required** |
|:-----------|:--------:|:------------------------------------------------------------                   |:------------ |
| `player_id`  | `int`  | ESPN player ID        | Yes                   |

## Examples


## Datasets


### Datasets returned 

```python
[
  'PASSING_YARDS',
  'RUSHING_YARDS',
  'RECEIVING_YARDS',
  'TOTAL_TACKLES',
  'SACKS',
  'KICKOFF_YARDS',
  'INTERCEPTIONS',
  'PASSING_TOUCHDOWNS',
  'QUARTERBACK_RATING',
  'RUSHING_TOUCHDOWNS',
  'RECEPTIONS',
  'RECEIVING_TOUCHDOWNS',
  'TOTAL_POINTS',
  'TOTAL_TOUCHDOWNS',
  'PUNT_YARDS',
  'PASSES_DEFENDED'
]
```

### Data Headers

Each of the above datasets returns the following headers. 

```python
[
    "player_id"        
    "player_name"      
    "team_id"  
    "team_code" 
    "value"  
]
```