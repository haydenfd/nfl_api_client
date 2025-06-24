# Game Boxscore Statistics (Team)

Fetches each team's general statistics for a particular game. Returns 1 dataset: `TEAM_STATS`, which always contains 2 rows and 28 columns. 

## Import

```python
from nfl_api_client.endpoints.game_team_stats import GameTeamStats
```
## Datasets

### TEAM STATS

### Data returned

```python
[
'team_id', 
'team_code', 
'team_name', 
'home_or_away', 
'first_downs', 
'first_downs_passing', 
'first_downs_rushing',
'first_downs_penalty', 
'third_down_eff', 
'fourth_down_eff', 
'total_offensive_plays', 
'total_yards', 
'yards_per_play', 
'total_drives', 
'net_passing_yards',
'completion_attempts',
'yards_per_pass',
'interceptions',
'sacks_yards_lost',
'rushing_yards',
'rushing_attempts',
'yards_per_rush_attempt',
'red_zone_attempts',
'total_penalties_yards',
'turnovers',
'fumbles_lost',
'defensive_touchdowns',
'possession_time'
]
```