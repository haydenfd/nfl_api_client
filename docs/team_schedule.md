# Team Schedule 

Fetches the full regular season schedule for a given team and season.

### Import 

``` python
from nfl_api_client.endpoints.team_schedule import TeamSchedule
```

### Parameters

| **Name**   | **Type** | **Description**                                                                |
|:-----------|:--------:|:------------------------------------------------------------                   |
| `team_id`  | `TeamID`   | The ID of the NFL team. Can use a `TeamID` or directly inject `int`          |
| `season`   | `int`      | Season year in `YYYY` format (e.g., `2024`)                                  |

### Datasets 

#### TEAM_SCHEDULE

```
[
    "GAME_ID"        
    "WEEK_NUMBER"      
    "DATE"  
    "GAME_TITLE" 
    "HOME_TEAM"  
    "AWAY_TEAM"
]
```

### Examples

```python
from nfl_api_client.endpoints.team_schedule import TeamSchedule
from nfl_api_client.lib.parameters import TeamID

# Can also do TeamSchedule(team_id = 4, year=2024) since CIN has TEAM ID = 4
bengals_schedule = TeamSchedule(team_id = TeamID.CIN, year = 2024)

df = bengals_schedule.get_dataset("TEAM_SCHEDULE").get_data_frame()        

```

<!-- ::: nfl_api_client.endpoints.team_schedule.TeamSchedule
    options:
      show_source: false
      show_root_heading: false
      show_root_toc_entry: false       -->

