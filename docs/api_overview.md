# ESPN API hidden endpoints overview

These are the notes I've compiled from various sources to build this client. 


There are four primary base URLs that are used for serving content, with a couple of them having some overlap in terms of data returned. These are => 

- `site.api.espn.com` (Site API)
- `sports.core.api.espn.com` (Core API)
- `cdn.espn.com` (CDN API)

On preliminary investigation, it seems as though `sports.core.api.espn.com` is significantly more useful for various data points. The Core and Site APIs have some overlap in specific endpoints. For example, one can fetch statistics leaders from both the Core and Site APIs, but the site API only display current data (As of writing this, it is the offseason. So, this path on Site API actually returns no data). Conversely, the Core API is configurable for season and season type, so it will always return something, on top of being more robust. 


## Useful endpoints

### Team statistics

`http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/{SEASON_YEAR}/types/{SEASON_TYPE}/teams/{TEAM_ID}/statistics`

Come back to this. This returns a lot of data.

### Player statistics



### 
