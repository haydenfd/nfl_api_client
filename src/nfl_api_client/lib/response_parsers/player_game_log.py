# from typing import Dict, Any, List
# import re
# from datetime import datetime
# import json 


# PASSING_KEYS = [
#     "completions", "attempts","yards", "completion_percent", 
#     "avg_yards_per_attempt", "touchdowns", "interceptions", "longest_pass",
#     "sacks", "qb_rating", "adjusted_rating",
# ]

# RUSHING_KEYS = [
#     "rushing_attempts", "rushing_yards", "yards_per_rush_attempt",
#     "rushing_touchdowns", "long_rushing"
# ]

# RECEIVING_KEYS = [
#     "receptions", "receiving_targets", "receiving_yards",
#     "yards_per_reception", "receiving_touchdowns", "long_reception",
# ]

# # DEFENSE_KEYS = [
# #     "total_tackles", "solo_tackles", "assist_tackles", "sacks",
# #     "forced_fumbles", "fumbles_recovered", "fumbles_recovered_yards", "interceptions",
# #     "interception_yards", "average_interception_yards", "interception_touchdowns",
# #     "long_interception", "passes_defended", "stuffs", "stuff_yards", "kicks_blocked"
# # ]

# FUMBLES_KEYS = [
#     "fumbles", "fumbles_lost", "forced_fumbles", "kicks_blocked",
# ]

# TACKLES_KEYS = [
#     "total_tackles", 
#     "solo_tackles",
#     "assist_tackles",
#     "sacks",
#     "stuffs",
#     "stuff_yards",
# ]

# INTERCEPTIONS_KEYS = [
#     "interceptions",
#     "interception_yards",
#     "average_interception_yards",
#     "interception_touchdowns",
#     "long_interception",
#     "passes_defended",
# ]

# SCORING_KEYS = [
#     "passing_touchdowns", "rushing_touchdowns", "receiving_touchdowns",
#     "return_touchdowns", "total_touchdowns", "total_two_point_conversions",
#     "kick_extra_points", "field_goals", "total_points"
# ]

# CATEGORY_KEY_MAP = {
#     "passing": PASSING_KEYS,
#     "rushing": RUSHING_KEYS,
#     "receiving": RECEIVING_KEYS,
#     "interceptions": INTERCEPTIONS_KEYS,
#     "scoring": SCORING_KEYS
# }

# def split_by_category(event_stats: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
#     result = {
#         "passing": [],
#         "rushing": [],
#         "receiving": [],
#         "defense": [],
#         "scoring": []
#     }

#     for entry in event_stats:
#         common = {
#             "event_id": entry["event_id"],
#             "score": entry.get("score"),
#             "game_result": entry.get("game_result")
#         }

#         for category, keys in CATEGORY_KEY_MAP.items():
#             # Filter only keys that exist in entry (skip missing values safely)
#             category_stats = {
#                 k: entry[k] for k in keys if k in entry
#             }

#             if category_stats:
#                 result[category].append({
#                     **common,
#                     **category_stats
#                 })

#     return result


# def extract_event_stats(data):
#     result = []

#     season_types = data.get("seasonTypes", [])
#     for season in season_types:
#         categories = season.get("categories", [])
#         for category in categories:
#             events = category.get("events", [])
#             for event in events:
#                 result.append({
#                     "event_id": event.get("eventId"),
#                     "stats": event.get("stats", [])
#                 })

#     return result

# PASSING_KEYS = [
#     "completions", "attempts", "yards", "completion_percent", "yards_per_attempt",
#     "passing_touchdowns", "interceptions", "longest_pass", "sacks",
#     "qb_rating", "adjusted_qbr" 
# ]

# RUSHING_KEYS = [
#     "rushing_attempts", "rushing_yards", "yards_per_rush_attempt",
#     "rushing_touchdowns", "long_rush"
# ]

# def flatten_stats_dynamically(event_stats: List[Dict[str, Any]], data: Dict[str, Any]) -> List[Dict[str, Any]]:
#     categories_meta = data.get("categories", [])
#     result = []

#     # Build (category_name, count, key_list) in order
#     category_slices = []
#     for cat in categories_meta:
#         name = cat.get("name", "").lower()
#         count = cat.get("count", 0)
#         keys = CATEGORY_KEY_MAP.get(name)
#         if keys:
#             category_slices.append((name, count, keys))

#     for entry in event_stats:
#         full_stats = entry.get("stats", [])
#         stat_index = 0
#         merged = {
#             "event_id": entry["event_id"],
#             "score": entry.get("score"),
#             "game_result": entry.get("game_result")
#         }

#         for category_name, count, keys in category_slices:
#             # Slice the stats for this category
#             stat_slice = full_stats[stat_index: stat_index + count]
#             stat_index += count

#             # Only zip as many values as there are keys (ignore extra keys or extra values)
#             zipped = dict(zip(keys, stat_slice))
#             merged.update(zipped)

#         result.append(merged)

#     return result


# def smart_cast(value: str):
#     if value is None:
#         return None
#     try:
#         if "." in value:
#             return float(value)
#         return int(value.replace(",", ""))
#     except (ValueError, TypeError):
#         return value


# def camel_to_snake(name: str) -> str:
#     return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()

# def merge_game_info(event_stats: List[Dict[str, Any]], data: Dict[str, Any]) -> List[Dict[str, Any]]:
#     events_mapping = data.get("events", {})

#     enriched = []
#     for entry in event_stats:
#         event_id = entry["event_id"]
#         game_info = events_mapping.get(event_id, {})

#         entry["score"] = game_info.get("score")
#         entry["game_result"] = game_info.get("gameResult")

#         enriched.append(entry)

#     return enriched


# def PlayerGameLogParser(data):
#     events_field = data.get("events", {})
#     res = []
#     for event_id, event_data in events_field.items():
#         res.append({
#             "game_id": event_id,
#             "team_result": event_data.get("gameResult", ""),
#             "opponent_team_id": event_data.get("opponent", {}).get("id"),
#             "week_number": event_data.get("week")
#         })
    
#     season_types_field = data.get("seasonTypes", [])

#     crap =[]
#     for season_type in season_types_field:
#         season_type_id = int(season_type.get("categories")[0].get('splitType'))
#         cat = season_type.get('categories')[0]

#         for event in cat.get("events", []):
#             crap.append(event.get('eventId'))
#             event_stats = event.get('stats')
#             passing_stats = dict(zip(PASSING_KEYS, event_stats[:11]))
#             rushing_stats = dict(zip(RUSHING_KEYS, event_stats[11:16]))

#     # print(crap)
#     event_stats = extract_event_stats(data)  # your existing function
#     enriched_stats = merge_game_info(event_stats, data)
#     flattened = flatten_stats_dynamically(enriched_stats, data)
#     final_split = split_by_category(flattened)
#     print(json.dumps(final_split, indent=3))



#     # print(json.dumps(res, indent=2))
#     return res



# # def PlayerGameLogParser(data: Dict[str, Any]) -> Dict[str, List[Dict[str, Any]]]:
# #     """
# #     Parses ESPN player game log response into per-category, per-game logs with metadata.
    
# #     Returns:
# #         {
# #             "passing": [ { game_1_pass_stats... }, { game_2_pass_stats... } ],
# #             "rushing": [ { game_1_rush_stats... }, ... ],
# #             ...
# #         }
# #     """
# #     events_lookup = data.get("events", {})
# #     season_types = data.get("seasonTypes", [])
# #     result = {}

# #     for season_type in season_types:
# #         season_display = season_type.get("displayName")
# #         categories = season_type.get("categories", [])

# #         for category in categories:
# #             category_name = category.get("name", "").lower()
# #             field_count = category.get("count", 0)
# #             events = category.get("events", [])

# #             if not events:
# #                 continue

# #             # Convert ESPN stat names to snake_case keys
# #             snake_keys = [camel_to_snake(n) for n in data["categories"] if n["name"] == category_name][0:field_count]
# #             logs = []

# #             for event in events:
# #                 event_id = event.get("eventId")
# #                 stat_values = event.get("stats", [])
# #                 mapped_stats = dict(zip(snake_keys, map(smart_cast, stat_values)))

# #                 # Enrich with event metadata
# #                 event_info = events_lookup.get(event_id, {})
# #                 game_date = event_info.get("gameDate")
# #                 opponent = event_info.get("opponent", {}).get("abbreviation")
# #                 result_code = event_info.get("gameResult")
# #                 score = event_info.get("score")
# #                 home_team_score = event_info.get("homeTeamScore")
# #                 away_team_score = event_info.get("awayTeamScore")
# #                 home_team = event_info.get("homeTeamId")
# #                 away_team = event_info.get("awayTeamId")
# #                 at_vs = event_info.get("atVs")

# #                 # Extract one useful game link (e.g. boxscore)
# #                 links = event_info.get("links", [])
# #                 boxscore_link = next((link["href"] for link in links if "boxscore" in link.get("rel", [])), None)

# #                 logs.append({
# #                     "season": season_display,
# #                     "event_id": event_id,
# #                     "game_date": game_date,
# #                     "opponent": opponent,
# #                     "result": result_code,
# #                     "score": score,
# #                     "home_team_id": home_team,
# #                     "away_team_id": away_team,
# #                     "home_team_score": smart_cast(home_team_score),
# #                     "away_team_score": smart_cast(away_team_score),
# #                     "at_vs": at_vs,
# #                     "boxscore_url": boxscore_link,
# #                     **mapped_stats
# #                 })

# #             if category_name not in result:
# #                 result[category_name] = []

# #             result[category_name].extend(logs)

# #     return result
