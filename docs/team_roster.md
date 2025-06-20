# Team Roster 

Fetches a team's full roster for the current year. Returns a single dataset called `TEAM_ROSTER`.

!!! NOTE

    Support for previous year team rosters is still under development. 
### Import 

``` python
from nfl_api_client.endpoints.team_roster import TeamRoster
```

### Parameters

| **Name**   | **Type** | **Description**                                                                | **Required** |
|:-----------|:--------:|:------------------------------------------------------------                   |:------------ |
| `team_id`  | `TeamID` or `int`  | ESPN Team ID        | Yes                   |


### Example

```python
from nfl_api_client.endpoints.team_roster import TeamRoster
from nfl_api_client.lib.parameters import TeamID

# TeamRoster(team_id=12) also works here since Chiefs have ID = 12

chiefs_roster = TeamRoster(team_id=TeamID.KC) 

# Get the dataframe head and column data types

data_frame = chiefs_roster.get_dataset("TEAM_ROSTER").get_data_frame()
print(df.head())
print(df.dtypes)

# Inspect the headers/columns used in the "ROSTER" dataset

headers = chiefs_roster.get_dataset("TEAM_ROSTER").get_headers()
print(headers)
```

### Datasets 

#### TEAM_ROSTER

```
[
        "player_id"
        "first_name"
        "last_name"
        "full_name"
        "weight"
        "height"
        "age"
        "dob"
        "debut_year"
        "college"
        "jersey_number"
        "position_name"
        "position_abbreviation"
        "position_type"
        "experience"
        "image_url"
]
```
