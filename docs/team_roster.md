# Team Roster 

Fetches a team's full roster for the current year. This includes players on IR, practice squads etc. Returns a single dataset called `TEAM_ROSTER`.

!!! NOTE

    Support for previous year team rosters is still under development. 

## **Import** 

``` python
from nfl_api_client.endpoints.team_roster import TeamRoster
```

## **Parameters**

| **Name**   | **Type** | **Description**                                                                | **Required** |
|:-----------|:--------:|:------------------------------------------------------------                   |:------------ |
| `team_id`  | `TeamID` or `int`  | ESPN Team ID        | Yes                   |


## **Examples**

```python
from nfl_api_client.endpoints.team_roster import TeamRoster
from nfl_api_client.lib.parameters import TeamID

# TeamRoster(team_id=12) also works here since Chiefs have ID = 12
chiefs_roster = TeamRoster(team_id=TeamID.KC) 

# Get the dataframe head and column data types

data_frame = chiefs_roster.get_dataset("TEAM_ROSTER").get_dataframe()
```

## **Datasets** 

```python
["TEAM_ROSTER"]
```

## **Dataset Keys**

### TEAM_ROSTER
 
!!! NOTE
    The fields for age and date of birth may be `None` for some rookies. This is because ESPN has not yet updated the respective players' information. 
```python
{
    "player_id": str,
    "first_name": str,
    "last_name": str,
    "full_name": str
    "weight": int,
    "height": int, # Listed in inches
    "age": int or None,
    "dob": str or None,
    "college": str,
    "jersey_number", int,
    "position_name": str: 
    "position_abbreviation": str,
    "experience": int, # How many years in league. Rookies have experience = 0
    "image_url": str,
}
```
