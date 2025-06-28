# Game Officials

Returns the game officials given a game ID. Returns 1 dataset, `GAME_OFFICIALS`, which contains 1 row. 

## **Import** 

``` python
from nfl_api_client.endpoints.game_officials import GameOfficials
```

## **Parameters**

| **Name**   | **Type** | **Description**                                                                | **Required** |
|:-----------|:--------:|:------------------------------------------------------------                   |:------------ |
| `game_id`  | `int`  | ESPN Game ID             | Yes                   |

## **Examples**

```python

from nfl_api_client.endpoints.game_officials import GameOfficials

superbowl_25_game_officials = GameOfficials(game_id = 401671889)

print(game_officials.get_dataset("GAME_OFFICIALS").get_dataframe())

```

## **Datasets**

```python
["GAME_OFFICIALS"]
```


## **Dataset Keys**

```python 
{
    "game_id": str,
    "referee": str,
    "head_linesman": str, 
    "side_judge": str, 
    "back_judge": str, 
    "umpire": str, 
    "field_judge": str, 
    "line_judge": str,
}
```