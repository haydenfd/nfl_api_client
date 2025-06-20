# Team Schedule 

Fetches the full season schedule for a given team, season, and season type. Returns one dataset: `TEAM_SCHEDULE`.


### Import 

``` python
from nfl_api_client.endpoints.team_schedule import TeamSchedule
```

### Parameters

| **Name**        | **Type**               | **Description**                                                                 | **Required** |
|-----------------|------------------------|---------------------------------------------------------------------------------|--------------|
| `team_id`       | `TeamID`/`int`      | The ID of the NFL team. Can use a `TeamID` enum or directly inject an `int`.   | Yes          |
| `season`        | `int`                  | Season year in `YYYY` format (e.g., `2024`). Default = `2025`.                  | No           |
| `season_type`   | `SeasonTypeID`/`int`| Season type (`Pre` = 1, `Regular` = 2, `Post` = 3). Default = `Regular`.                   | No           |


### Examples

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

df = bengals_schedule.get_dataset("TEAM_SCHEDULE").get_data_frame()        

```


### Datasets 

#### TEAM_SCHEDULE

```
[
    "game_id",        
    "week_number", 
    "season_type",     
    "date",
    "game_title",
    "home_team_id",  
    "home_team_code",
    "away_team_id", 
    "away_team_code",
]
```
