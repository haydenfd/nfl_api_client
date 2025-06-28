# Team Schedule 

Fetches the full season schedule for a given team, season, and season type. Returns one dataset: `TEAM_SCHEDULE`.


## **Import** 

``` python
from nfl_api_client.endpoints.team_schedule import TeamSchedule
```

## **Parameters**

| **Name**        | **Type**               | **Description**                                                                 | **Required** |
|-----------------|------------------------|---------------------------------------------------------------------------------|--------------|
| `team_id`       | `TeamID` or `int`      | ESPN ID of NFL team. Can use `TeamID` value or inject an `int`.   | Yes          |
| `season`        | `int`                  | Season year in `YYYY` format (e.g., `2024`). Default = `2025`.                  | No           |
| `season_type`   | `SeasonTypeID` or `int`| Season type (`PRE` = 1, `REG` = 2, `POST` = 3). Default = `SeasonTypeID.REG`.                   | No           |


## **Examples**

```python
from nfl_api_client.endpoints.team_schedule import TeamSchedule
from nfl_api_client.lib.parameters import TeamID, SeasonTypeID

# Can also do TeamSchedule(team_id = 4, year=2024, season_type = 2)

bengals_regular_season = TeamSchedule(
    team_id = TeamID.CIN, 
    year = 2024, 
    season_type = SeasonTypeID.REG
    )

# Can also do TeamSchedule(team_id = 1, year=2023, season_type = 3)


falcons_2022_post_season = TeamSchedule(
    team_id = TeamID.ATL,
    year = 2023, 
    season_type=SeasonTypeID.POST
    )

df = bengals_schedule.get_dataset("TEAM_SCHEDULE").get_dataframe()        

```


## **Datasets** 

```python
["TEAM_SCHEDULE"]
```


## **Data Headers/Keys**

### TEAM_SCHEDULE

```python
{
    "game_id": str,      
    "week_number": str,
    "season_type": str,
    "date": str,
    "game_title": str, 
    "home_team_id": str,
    "home_team_code": str,
    "away_team_id": str, 
    "away_team_code": str
}
```
