import httpx
import asyncio 
from nfl_api_client.lib.endpoint_registry import ENDPOINT_REGISTRY
import json
import pandas as pd
from typing import Optional

def safe_cast_numeric(value):
    if value in ("", "-", None):
        return None
    try:
        cleaned = str(value).replace(",", "")
        if "." in cleaned:
            return float(cleaned)
        return int(cleaned)
    except ValueError:
        return None

def parse_totals(names, totals):
    return {
        name: safe_cast_numeric(value)
        for name, value in zip(names, totals)
    }
# class PlayerCareerBasicStats:
    # BASE_URL = ENDPOINT_REGISTRY["PLAYER_CAREER_BASIC_STATS"]

#     def __init__(self, player_id: int):
        # self.url = self.BASE_URL.format(player_id=player_id)
#         self.data = None
#         self.start_time, self.process_time = None, None

    # async def _fetch(self):
    #     async with httpx.AsyncClient() as client:
    #             response = await client.get(self.url)
    #             response.raise_for_status()
    #             self.data = response.json()
    
#     async def process(self):
#         urls_to_visit = []
#         result = []

#         available_szns_filter = self.data.get("filters", [])[1]
#         available_szns_options = available_szns_filter.get("options", [])

#         url_with_query = f"{self.url}?season="
#         for opt in available_szns_options:
#             season = opt.get("value", "")
#             full_url = f"{url_with_query}{season}"
#             urls_to_visit.append((season, full_url))

#         async with httpx.AsyncClient() as client:
#             async def fetch_season(season, url):
#                 try:
#                     resp = await client.get(url)
#                     resp.raise_for_status()
#                     data = resp.json()

#                     names = data.get("names", [])
#                     seasonTypes = data.get("seasonTypes", [])
#                     regularSeason = seasonTypes[1] if len(seasonTypes) > 1 else {}

#                     categories = regularSeason.get("categories", [])
#                     totals = categories[0].get("totals", []) if categories else []

#                     if names and totals:
#                         stats = map_stats_to_values(names, totals)
#                         stats["season"] = int(season)
#                         return stats
#                 except Exception as e:
#                     print(f"Error fetching season {season}: {e}")
#                 return None
            
#             tasks = [fetch_season(season, url) for season, url in urls_to_visit]
#             self.start_time = time.time()
#             results = await asyncio.gather(*tasks)
#             print(f"Execution time {time.time() - self.start_time:.4f} seconds")

#         return [stats for stats in results if stats]

#     async def process2(self):
#         urls_to_visit = []
#         result = []

#         available_szns_filter = self.data.get("filters", [])[1]
#         available_szns_options = available_szns_filter.get("options", [])

#         url_with_query = f"{self.url}?season="
#         for opt in available_szns_options:
#             season = opt.get("value", "")
#             full_url = f"{url_with_query}{season}"
#             urls_to_visit.append((season, full_url))

#         async with httpx.AsyncClient() as client:
#             self.start_time = time.time()

#             for season, url in urls_to_visit:
#                 try:
#                     resp = await client.get(url)
#                     resp.raise_for_status()
#                     data = resp.json()

#                     names = data.get("names", [])
#                     seasonTypes = data.get("seasonTypes", [])
#                     regularSeason = seasonTypes[1] if len(seasonTypes) > 1 else {}

#                     categories = regularSeason.get("categories", [])
#                     totals = categories[0].get("totals", []) if categories else []

#                     if names and totals:
#                         stats = map_stats_to_values(names, totals)
#                         stats["season"] = int(season)
#                         result.append(stats)
#                 except Exception as e:
#                     print(f"Error fetching season {season}: {e}")

#             print(f"Sequential execution time {time.time() - self.start_time:.4f} seconds")

#         return result


class PlayerCareerBasicStats:

    BASE_URL = ENDPOINT_REGISTRY["PLAYER_CAREER_BASIC_STATS"]

    def __init__(self, player_id: int, season_type: Optional[int] = 2):
        self.url = self.BASE_URL.format(player_id=player_id, season_type=season_type)
        self.data = None
        print(self.url)

    async def _fetch(self):
        async with httpx.AsyncClient() as client:
                response = await client.get(self.url)
                response.raise_for_status()
                self.data = response.json()

    async def process(self):
        categories_field = self.data.get('categories', [])
        result = {}

        for category in categories_field:
            category_name = category.get("name", "")
            names = category.get("names", [])
            totals = category.get("totals", [])
            stats_by_season = category.get("statistics", [])

            category_result = {
                "TOT": parse_totals(names, totals)
            }

            for season_entry in stats_by_season:
                season_year = season_entry.get("season", {}).get("year")
                team_id = safe_cast_numeric(season_entry.get("teamId"))
                stats_values = season_entry.get("stats", [])

                if season_year:
                    category_result[season_year] = {
                        "team_id": team_id,
                        "stats": parse_totals(names, stats_values)
                    }

            result[category_name] = category_result

        self.data = result
        return result

    def get_data(self):
        return self.data
    
    def get_passing(self) -> dict:
        return self.data.get("passing")

    def get_rushing(self) -> dict:
        return self.data.get("rushing")

    def get_receiving(self) -> dict:
        return self.data.get("receiving")

    def get_scoring(self) -> dict:
        return self.data.get("scoring")
    
if __name__ == "__main__":
    async def main():
        stats = PlayerCareerBasicStats(4262921)
        await stats._fetch()
        await stats.process()
        print(json.dumps(stats.get_passing(), indent=2))
        # urls = await stats.process2()
        
        # print(pd.DataFrame(urls))

    asyncio.run(main())
     
