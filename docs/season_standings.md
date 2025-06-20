# Season Standings (Basic)

Fetches the basic standings for a given season. 

Depending on the `group` parameter, it returns a variable number of datasets. This parameter is used to segment the standings based on groups - league, conference, or division. 

`"conference"` returns 2 datasets: 1 each for AFC, NFC. 

`"league"` returns one consolidated dataset for whole league rankings. 

`"division"` returns one data set each for North, East, West, South in both AFC and NFC conferences (8 datasets total).


### Import 

``` python
from nfl_api_client.endpoints.season_standings import SeasonStandings
```

### Parameters

| **Name**        | **Type**               | **Description**                                                                 | **Required** |
|-----------------|------------------------|---------------------------------------------------------------------------------|--------------|
| `season`        | `int`                  | Season year in `YYYY` format Default = `2024`.                  | No           |
| `group`   | `"league"`, `"conference"`, `division`           | Grouping for standings. Default = `league`.                   | No           |


### Examples
