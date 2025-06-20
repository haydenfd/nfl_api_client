SITE_URL = "https://site.api.espn.com/apis/site/v2/sports/football/nfl"
WEB_URL = "https://site.web.api.espn.com/apis/common/v3/sports/football/nfl"
CORE_URL = "https://sports.core.api.espn.com/v2/sports/football/leagues/nfl"
CDN_URL = "https://cdn.espn.com/core/nfl"

#fmt: off
ENDPOINT_REGISTRY = {
    "TEAM_SCHEDULE":                    f"{SITE_URL}/teams/{{team_id}}/schedule?season={{year}}",
    "TEAM_ROSTER":                      f"{SITE_URL}/teams/{{team_id}}/roster",
    # "SEASON_STANDINGS":                 f"{CORE_URL}/seasons/{{year}}/types/{{season_type}}/groups/{{conference_type}}/standings/0",
    "TEAM_DEPTH_CHART":                 f"{CORE_URL}/seasons/{{year}}/teams/{{team_id}}/depthcharts",
    "STATS_LEADERS":                     f"{CORE_URL}/seasons/{{year}}/types/{{season_type}}/leaders?limit={{limit}}",
    "PLAYER_CAREER_STATS":              f"{CORE_URL}/athletes/{{player_id}}/statisticslog",
    "PLAYER_CAREER_BASIC_STATS":        f"{WEB_URL}/athletes/{{player_id}}/stats?seasontype={{season_type}}",
    "LEAGUE_GAME_FINDER":               f"{SITE_URL}/scoreboard",
    "DRAFT_SUMMARY":                    f"{CORE_URL}/seasons/{{year}}/draft/rounds",
    "GAME_SUMMARY":                     f"{SITE_URL}/summary?event={{game_id}}",
    "SEASON_STANDINGS":                 f"{CDN_URL}/standings?xhr=1&season={{season}}&view={{view}}&group={{group}}",
    "SEASON_SCHEDULE_WEEKDAY":          f"https://site.api.espn.com/apis/site/v2/{{day}}nightfootball?season={{season}}",
}
# fmt: on
