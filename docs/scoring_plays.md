# Game Scoring Plays

Fetches all scoring plays for a game given a particular ESPN Game ID. Returns a singlular dataset: `SCORING_PLAYS`.

## **Import**

```python
from nfl_api_client.endpoints.game_scoring_plays import GameScoringPlays
```

## **Parameters**

| **Name** | **Type** | **Description**                                                                                    | **Required** |
| :------- | :------: | :------------------------------------------------------------------------------------------------- | :----------: |
| `game_id` |   `int`  | ESPN Game ID                                                    |      Yes      |


## **Examples**

```python

from nfl_api_client.endpoints.game_scoring_plays import GameScoringPlays

# Fetch scoring plays for a specific game
plays = GameScoringPlays(game_id=401671889)

# Get scoring plays as a DataFrame
df = plays.get_dataset("SCORING_PLAYS").get_dataframe()

# Preview top 5 scoring plays
print(df[["period", "clock", "description"]].head())

```


## **Datasets**

```python
["SCORING_PLAYS"]
```

## **Data Fields**

```python

{
    "drive_id": str,              # ESPN Drive ID
    "description": str,           
    "team_id": str,               
    "team_code": str,             
    "home_score": int,            # NOTE: Score AFTER the play      
    "away_score": int,            # NOTE: Score AFTER the play      
    "play_type": str,             
    "play_abbreviation": str,     # "TD" or "FG"
    "period": int,                
    "clock": str                  
}

```

