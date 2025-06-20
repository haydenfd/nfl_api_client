# Statistics Leaders

Fetches the statistics leaders for a given year and given season type (Preseason, Regular Season, Post season).
Returns 1 dataset for each of the 16 categories. 
## Import 

``` python
from nfl_api_client.endpoints.stats_leaders import StatsLeaders
```

## Parameters

| **Name**   | **Type** | **Description**                                                                | **Required** |
|:-----------|:--------:|:------------------------------------------------------------                   |:------------ |
| `season`  | `int`  | Season year in `YYYY` format Default = `2024`.              | No                   |
| `season_type`  | `SeasonTypeID` or `int`  | Season type (Pre, Regular, Post)              | No                   |
| `limit`  | `int`  | No. of results per category. Default = `10`              | No                   |

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