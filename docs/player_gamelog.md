# Player Gamelog

Fetches game-by-game (regular + post season) statistics for an NFL player during a given season, given an ESPN player ID. Returns 1 dataset: `GAMELOG`.

This endpoint also aggregates both metadata (date, teams, result) for each game the player appeared in.

## **Import**

```python
from nfl_api_client.endpoints.player_gamelog import PlayerGamelog
```

## **Parameters**

| **Name** | **Type** | **Description**                                                                                    | **Required** |
| :------- | :------: | :------------------------------------------------------------------------------------------------- | :----------: |
| `player_id` |   `int`  | ESPN Player ID                                                 |      Yes      |
| `season`  |   `int`  | Season in YYYY format. Default = `2024`. |      No      |



## **Examples**

```python
from nfl_api_client.endpoints.player_gamelog import PlayerGamelog

gamelog = PlayerGamelog(player_id=3124005, season=2024)
df = gamelog.get_dataset("GAMELOG").get_dataframe()


print(df[["week", "game_date", "season_type", "game_result", "passing_yards", "rushing_yards"]])

```


## **Datasets**

```python
["GAMELOG"]
```


## **Data Fields**

### *Core Fields*

The following fields are always present in `GAMELOG`:

```python
{
    "game_id": str,
    "week": int,
    "game_date": str,
    "score": str,
    "home_team_id": int,
    "away_team_id": int,
    "home_team_code": str,
    "away_team_code": str,
    "home_team_score": int,
    "away_team_score": int,
    "game_result": str,     # W or L, result for the player's team
    "season_type": str      # "REG" or "POST"
}
```

### *Statistics Fields*

The remaining fields vary based on the player’s position and available stat types. For example, if the player is a QB with rushing stats, then his gamelog data will also include the fields listed under the `PASSING` and `RUSHING` sections below. 

#### **PASSING**


```python
[
    "completions",
    "passing_attempts",
    "passing_yards",
    "completion_pct",
    "yards_per_pass_attempt",
    "passing_touchdowns",
    "interceptions",
    "long_passing",
    "sacks",
    "qb_rating",
    "adj_qbr"
]
```


#### **RUSHING**


```python
[
    "rushing_attempts",
    "rushing_yards",
    "yards_per_rush_attempt",
    "rushing_touchdowns",
    "long_rushing"
]
```


#### **RECEIVING**

```python
[
    "receptions",
    "receiving_targets",
    "receiving_yards",
    "yards_per_reception",
    "receiving_touchdowns",
    "long_reception"
]

```

#### **TACKLES**

```python
[
    "total_tackles",
    "solo_tackles",
    "assist_tackles",
    "sacks",
    "stuffs",
    "stuff_yards"
]
```

#### **FUMBLES**

```python

[
    "fumbles",
    "fumbles_lost",
    "fumbles_forced",
    "fumbles_recovered",
    "kicks_blocked"
]

```


#### **INTERCEPTIONS**

```python
[
    "interceptions",
    "interception_yards",
    "avg_interception_yards",
    "interception_touchdowns",
    "long_interception",
    "passes_defended"
]
```