from nfl_api_client.lib.utils import format_gamelog_date_str, camel_to_snake
from nfl_api_client.lib.parameters import TeamID

def get_team_code(team_id: int | str) -> str:
    try:
        return TeamID(int(team_id)).name
    except (ValueError, KeyError):
        return None


def enrich_gamelog_with_stats(data: dict, gamelog: list[dict]) -> list[dict]:
    stat_keys = data.get("names", [])
    snake_keys = [camel_to_snake(k) for k in stat_keys]
    gamelog_by_id = {entry["game_id"]: entry for entry in gamelog}

    for season_type in data.get("seasonTypes", []):
        for category in season_type.get("categories", []):
            split_type = category.get("splitType")
            for event in category.get("events", []):
                event_id = event.get("eventId")
                stat_values = event.get("stats", [])

                if event_id in gamelog_by_id:
                    gamelog_by_id[event_id]["season_type"] = "POST" if split_type == "3" else "REG"
                    stats_dict = dict(zip(snake_keys, stat_values))
                    gamelog_by_id[event_id].update(stats_dict)
    return list(gamelog_by_id.values())

def parse_player_gamelog_metadata(data: dict) -> list[dict]:
    events = data.get("events", {})
    gamelog = []

    for game_id, game_data in events.items():
        home_id = game_data.get("homeTeamId")
        away_id = game_data.get("awayTeamId")

        gamelog.append({
            "game_id": game_id,
            "week": game_data.get("week"),
            "game_date": format_gamelog_date_str(game_data.get("gameDate")),
            "home_team_id": home_id,
            "away_team_id": away_id,
            "home_team_code": get_team_code(home_id),
            "away_team_code": get_team_code(away_id),
            "score": game_data.get("score"),
            "home_team_score": game_data.get("homeTeamScore"),
            "away_team_score": game_data.get("awayTeamScore"),
            "game_result": game_data.get("gameResult"),
        })

    return gamelog


def PlayerGamelogParser(data: dict) -> dict:
    base_gamelog = parse_player_gamelog_metadata(data)
    full_gamelog = enrich_gamelog_with_stats(data, base_gamelog)
    return {
        "GAMELOG": full_gamelog
    }
