from typing import Dict, List, Any
from nfl_api_client.lib.parameters import TeamID

def smart_cast(value: str):
    if value is None:
        return None
    try:
        if "." in value:
            return float(value)
        return int(value.replace(",", ""))
    except (ValueError, TypeError):
        return value


PASSING_KEYS = [
    "games_played", "completions", "attempts", "completion_percent", "yards",
    "avg_yards_per_attempt", "touchdowns", "interceptions", "longest_pass",
    "sacks", "qb_rating"
]

RUSHING_KEYS = [
    "games_played", "rushing_attempts", "rushing_yards", "yards_per_rush_attempt",
    "rushing_touchdowns", "long_rushing", "rushing_first_downs",
    "rushing_fumbles", "rushing_fumbles_lost"
]

RECEIVING_KEYS = [
    "games_played", "receptions", "receiving_targets", "receiving_yards",
    "yards_per_reception", "receiving_touchdowns", "long_reception",
    "receiving_first_downs", "receiving_fumbles", "receiving_fumbles_lost"
]

DEFENSE_KEYS = [
    "games_played", "total_tackles", "solo_tackles", "assist_tackles", "sacks",
    "forced_fumbles", "fumbles_recovered", "fumbles_recovered_yards", "interceptions",
    "interception_yards", "average_interception_yards", "interception_touchdowns",
    "long_interception", "passes_defended", "stuffs", "stuff_yards", "kicks_blocked"
]

SCORING_KEYS = [
    "games_played", "passing_touchdowns", "rushing_touchdowns", "receiving_touchdowns",
    "return_touchdowns", "total_touchdowns", "total_two_point_conversions",
    "kick_extra_points", "field_goals", "total_points"
]

CATEGORY_KEY_MAP = {
    "passing": PASSING_KEYS,
    "rushing": RUSHING_KEYS,
    "receiving": RECEIVING_KEYS,
    "defense": DEFENSE_KEYS,
    "scoring": SCORING_KEYS
}

def PlayerCareerStatsParser(data: Dict[str, Any]) -> Dict[str, List[Dict[str, Any]]]:
    categories = data.get("categories", [])
    result = {}

    for category in categories:
        category_name = category.get("displayName", "").lower()
        stat_keys = CATEGORY_KEY_MAP.get(category_name)

        # if not stat_keys:
        #     continue 

        parsed_entries = []
        for entry in category.get("statistics", []):
            stats = entry.get("stats", [])
            season_year = entry.get("season", {}).get("year")
            team_id = int(entry.get("teamId")) if entry.get("teamId") else None
            position = entry.get("position")

            mapped_stats = dict(zip(stat_keys, stats))
            flattened = {
                "season_year": season_year,
                "team_id": team_id,
                "team_code": TeamID(team_id).name,
                "position": position,
                **{k: smart_cast(v) for k, v in mapped_stats.items()}
            }

            parsed_entries.append(flattened)

        result[category_name.upper()] = parsed_entries
    return result

