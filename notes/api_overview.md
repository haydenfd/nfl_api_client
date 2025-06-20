# ESPN API hidden endpoints overview

These are the notes I've compiled from various sources to build this client. 


There are four primary base URLs that are used for serving content, with a couple of them having some overlap in terms of data returned. These are => 

- `site.api.espn.com` (Site API)
- `sports.core.api.espn.com` (Core API)
- `cdn.espn.com` (CDN API)

On preliminary investigation, it seems as though `sports.core.api.espn.com` is significantly more useful for various data points. The Core and Site APIs have some overlap in specific endpoints. For example, one can fetch statistics leaders from both the Core and Site APIs, but the site API only display current data (As of writing this, it is the offseason. So, this path on Site API actually returns no data). Conversely, the Core API is configurable for season and season type, so it will always return something, on top of being more robust. 


## Useful endpoints

### Team statistics

`https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/{SEASON_YEAR}/types/{SEASON_TYPE}/teams/{TEAM_ID}/statistics`

Come back to this. This returns a lot of data.

### Player statistics

`https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/athletes/{ATHLETE_ID}/statisticslog`

The above returns JSON with fields `$ref` and `entries`.  
`entries` is a list of JSON objects, where each object contains `season`, `statistics`. 
`statistics[0].statistics.$ref` contains the link to the particular season. This ref contains the year info as well. 

**Sample response**

```
{
    "$ref": "http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/athletes/3139477/statisticslog?lang=en&region=us",
    "entries": [
        {
            "season": {
                "$ref": "http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2024?lang=en&region=us"
            },
            "statistics": [
                {
                    "type": "total",
                    "statistics": {
                        "$ref": "http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2024/types/2/athletes/3139477/statistics/0?lang=en&region=us"
                    }
                },
                {
                    "type": "team",
                    "team": {
                        "$ref": "http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2024/teams/12?lang=en&region=us"
                    },
                    "statistics": {
                        "$ref": "http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2024/types/2/teams/12/athletes/3139477/statistics?lang=en&region=us"
                    }
                }
            ]
        },
        ...
    ]
```
Once the initial response is fetched, will need to visit each individual season $ref to fetch each season stats. 

The JSON for an individual season stats contains a lot of fields, segmented by 6 categories -  **General**, **Passing**, **Rushing**, **Receiving**, **Defense**, **Defensive Interceptions**, **Scoring**

