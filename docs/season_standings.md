# Season Standings

Fetches NFL season standings for a given year, grouped by league, conference, or division. The returned datasets vary depending on the selected grouping mode. For `group="conference"`, for example, this endpoint returns 2 datasets - `AFC` and `NFC`.

## **Import**

```python
from nfl_api_client.endpoints.season_standings import SeasonStandings
```

## **Parameters**

| **Name** | **Type** | **Description**                                                                                    | **Required** |
| :------- | :------: | :------------------------------------------------------------------------------------------------- | :----------: |
| `season` |   `int`  | Season year in `YYYY` format. Default = `2024`                                                     |      No      |
| `group`  |   `str`  | Grouping mode. Must be one of `"league"`, `"conference"`, or `"division"`. Default = `"league"` |      No      |


## **Examples**

```python

from nfl_api_client.endpoints.season_standings import SeasonStandings

# Fetch league-wide standings for 2024
standings = SeasonStandings(season=2024, group="league")

# Get the dataframe
df = standings.get_dataset("LEAGUE").get_dataframe()

# For conference-level grouping (AFC/NFC)
conf_standings = SeasonStandings(season=2024, group="conference")
afc_df = conf_standings.get_dataset("AFC").get_dataframe()
nfc_df = conf_standings.get_dataset("NFC").get_dataframe()

# For division-level grouping (e.g. AFC East, NFC North)
div_standings = SeasonStandings(season=2024, group="division")
east_df = div_standings.get_dataset("AFC EAST").get_dataframe()

```


## **Datasets**

Returned dataset names vary based on the group value. 


### group = "league"

```python
["LEAGUE"]
```

### group = "conference"

```python
["AFC", "NFC"]
```

### group = "division"

```python
[
    "AFC East",
    "AFC North",
    "AFC West",
    "AFC South",
    "NFC East",
    "NFC North", 
    "NFC West",
    "NFC South"
]
```


## **Data Fields**

All of the above datasets return the same fields. 

```python
{
    "team_id": str,
    "team_name": str,
    "team_code": str,
    "seed": int, # Always the conference seed
    "clincher": str,
    "wins": int,
    "losses": int,
    "ties": int,
    "win_percent": float,
    "home_record": str,        
    "away_record": str,
    "div_record": str,
    "conference_record": str,
    "points_for": int,
    "points_against": int,
    "point_differential": int,
    "streak": str   
}
```