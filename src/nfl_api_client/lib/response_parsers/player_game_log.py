from typing import Dict, Any, List
import re
from datetime import datetime
import json 


PASSING_KEYS = [
    "completions", "attempts","yards", "completion_percent", 
    "avg_yards_per_attempt", "touchdowns", "interceptions", "longest_pass",
    "sacks", "qb_rating", "adjusted_rating",
]

RUSHING_KEYS = [
    "rushing_attempts", "rushing_yards", "yards_per_rush_attempt",
    "rushing_touchdowns", "long_rushing"
]


def PlayerGameLogParser(data):
    """
    Parse NFL game log data and aggregate by stat categories.
    
    Args:
        data: JSON data containing events and seasonTypes
    
    Returns:
        Dict with categories as keys and list of game dicts as values
    """
    # Define stat keys mapping
    stat_keys = {
        "passing": PASSING_KEYS,
        "rushing": RUSHING_KEYS
    }
    result = {}
    
    # Get the category definitions and their counts
    categories_info = data.get("categories", [])
    category_counts = {}
    for cat in categories_info:
        category_counts[cat["name"]] = cat["count"]
    
    # Process each season type
    for season_type in data.get("seasonTypes", []):
        for category in season_type.get("categories", []):
            
            # Process each game event in this category
            for event in category.get("events", []):
                event_id = event["eventId"]
                stats = event["stats"]
                
                # Get basic game info from events using event_id
                game_info = data.get("events", {}).get(event_id, {})
                
                # Create base game data
                base_game_data = {
                    "week": game_info.get("week"),
                    # "gameDate": game_info.get("gameDate"),
                    # "atVs": game_info.get("atVs"),
                    "game_result": game_info.get("gameResult"),
                    "homeTeamId": game_info.get("homeTeamId"),
                    "awayTeamId": game_info.get("awayTeamId"),
                    "homeTeamScore": game_info.get("homeTeamScore"),
                    "awayTeamScore": game_info.get("awayTeamScore"),
                    "opponent": game_info.get("opponent", {})
                }
                
                # Split stats according to category counts
                stat_index = 0
                for cat_name, count in category_counts.items():
                    if cat_name.upper() not in result:
                        result[cat_name.upper()] = []
                    
                    # Extract stats for this category
                    cat_stats = stats[stat_index:stat_index + count]
                    stat_index += count
                    
                    # Create game entry for this category
                    game_entry = base_game_data.copy()
                    
                    # Add category-specific stats
                    if cat_name in stat_keys:
                        stat_dict = dict(zip(stat_keys[cat_name], cat_stats))
                        game_entry.update(stat_dict)
                    
                    # Add season type info
                    # game_entry["seasonType"] = season_type.get("displayName")
                    # game_entry["category"] = cat_name
                    
                    result[cat_name.upper()].append(game_entry)
    # print(result)
    return result
