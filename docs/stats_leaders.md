# Statistics Leaders

Fetches the statistics leaders for a given year and given season type (Preseason, Regular Season, Post season).
Returns 1 dataset for each of the 16 categories. 

## **Import** 

``` python
from nfl_api_client.endpoints.stats_leaders import StatsLeaders
```

## **Parameters**

| **Name**   | **Type** | **Description**                                                                | **Required** |
|:-----------|:--------:|:------------------------------------------------------------                   |:------------ |
| `season`  | `int`  | Season year in `YYYY` format Default = `2024`            | No                   |
| `season_type`  | `SeasonTypeID` or `int`  | Season type (Pre, Regular, Post)              | No                   |
| `limit`  | `int`  | No. of results per category. Default = `10`              | No                   |

## **Examples**

```python
from nfl_api_client.endpoints.stats_leaders import StatsLeaders
from nfl_api_client.lib.parameters import SeasonTypeID

# Fetch default stats leaders for 2024 regular season
leaders = StatsLeaders(season=2024, season_type=SeasonTypeID.REGULAR)

# View the passing yards leaders
passing_df = leaders.get_dataset("PASSING_YARDS").get_dataframe()
print(passing_df[["player_name", "value"]].head())

# Get top 5 leaders in interceptions
leaders_top5 = StatsLeaders(season=2024, season_type=SeasonTypeID.REG, limit=5)
interceptions_df = leaders_top5.get_dataset("INTERCEPTIONS").get_dataframe()

# Print player names and interceptions
print(interceptions_df[["player_name", "value"]])

```

## **Datasets**


There are 16 datasets returned by this endpoint. 

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

### **Data Fields**

Each of the above datasets returns the following columns/fields. 

```python
{
    "player_id": str,        
    "player_name": str,      
    "team_id": int,  
    "team_code": str,
    "value": int  
}
```