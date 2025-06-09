# import requests
# import time

# def fetch_player_season_stats(athlete_id, season, season_type=2):
#     url = f"https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/{season}/types/{season_type}/athletes/{athlete_id}/statistics"
#     response = requests.get(url, params={"lang": "en", "region": "us"})
#     response.raise_for_status()
#     return response.json()

# def extract_stats_by_category(json_data):
#     """
#     Extract stats organized by category name
#     Returns a nested dictionary: {category_name: {stat_name: value}}
#     """
#     stats_map = {}
    
#     # Access the splits object
#     splits = json_data['splits']
    
#     # Iterate through each category in splits
#     for category in splits['categories']:
#         category_name = category['name']  # Use the category name as key
#         stats_map[category_name] = {}
        
#         # Iterate through each stat in the category
#         for stat in category['stats']:
#             name = stat['name']
#             value = stat['value']
#             stats_map[category_name][name] = value
    
#     return stats_map


# if __name__ == "__main__":
#     start_time = time.time()
#     stats = fetch_player_season_stats(3139477, 2024, 2)
#     stats_2 = fetch_player_season_stats(3139477, 2023, 2)
#     stats_3 = fetch_player_season_stats(3139477, 2022, 2)
#     stats_4 = fetch_player_season_stats(3139477, 2021, 2)
#     stats_5 = fetch_player_season_stats(3139477, 2020, 2)
#     stats_6 = fetch_player_season_stats(3139477, 2019, 2)
#     stats_7 = fetch_player_season_stats(3139477, 2018, 2)
#     stats_8 = fetch_player_season_stats(3139477, 2017, 2)

#     x = extract_stats_by_category(stats)
#     y = extract_stats_by_category(stats_2)
#     z = extract_stats_by_category(stats_3)
#     w = extract_stats_by_category(stats_4)
#     t = extract_stats_by_category(stats_5)
#     p = extract_stats_by_category(stats_6)
#     i = extract_stats_by_category(stats_7)        
#     q = extract_stats_by_category(stats_8)            
#     end_time = time.time()
#     print(end_time - start_time)

import httpx
import asyncio
import time

async def fetch_player_season_stats(client, athlete_id, season, season_type=2):
    url = f"https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/{season}/types/{season_type}/athletes/{athlete_id}/statistics"
    print(url)
    response = await client.get(url, params={"lang": "en", "region": "us"})
    response.raise_for_status()
    return response.json()

def extract_stats_by_category(json_data):
    """
    Extract stats organized by category name
    Returns a nested dictionary: {category_name: {stat_name: value}}
    """
    stats_map = {}
    # Access the splits object
    splits = json_data['splits']
    # Iterate through each category in splits
    for category in splits['categories']:
        category_name = category['name']  # Use the category name as key
        stats_map[category_name] = {}
        # Iterate through each stat in the category
        for stat in category['stats']:
            name = stat['name']
            value = stat['value']
            stats_map[category_name][name] = value
    return stats_map

async def main():
    start_time = time.time()
    
    async with httpx.AsyncClient() as client:
        # Create all tasks
        tasks = [
            fetch_player_season_stats(client, 3139477, 2024, 2),
            fetch_player_season_stats(client, 3139477, 2023, 2),
            fetch_player_season_stats(client, 3139477, 2022, 2),
            fetch_player_season_stats(client, 3139477, 2021, 2),
            fetch_player_season_stats(client, 3139477, 2020, 2)
        ]
        
        # Execute all requests in parallel
        results = await asyncio.gather(*tasks)
    
    processed_stats = [extract_stats_by_category(stats) for stats in results]
    end_time = time.time()
    print("=" * 50)
    print("PLAYER SEASON STATS SUMMARY")
    print("=" * 50)
    
    seasons = [2024, 2023, 2022, 2021, 2020, 2019, 2018, 2017]
    for i, (season, stats) in enumerate(zip(seasons, processed_stats)):
        print(f"\n📅 Season {season}:")
        print("-" * 20)
        for category_name, category_stats in stats.items():
            print(f"  {category_name.title()}:")
            for stat_name, value in category_stats.items():
                # Format the stat name nicely
                formatted_name = stat_name.replace('_', ' ').title()
                print(f"    {formatted_name}: {value}")

    print(f"Parallel execution time: {end_time - start_time:.4f} seconds")
    
    return processed_stats

if __name__ == "__main__":
   asyncio.run(main())