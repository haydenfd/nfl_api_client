from datetime import datetime
import re
from typing import Optional 

'''
    Receives date_str in example format - "2023-12-30T21:15Z" (which is the format in which ESPN endpoints send dates)
    Returns str in MM/DD/YYY format - "12-30-2023"

'''
def format_date_str(date_str: str) -> str:
    return datetime.strptime(date_str, "%Y-%m-%dT%H:%MZ").strftime("%m-%d-%Y")

# '''
#     Receives a $ref url in example format - "http://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2023/types/2/athletes/3139477/statistics/0"
#     Returns int of the season/year if it can be extracted from the $ref. Otherwise, returns None. However, this should always return a value because we are passing valid URLs that contain a season.
# '''
# def extract_season_from_ref(ref_url: str) -> Optional[int]:
#     season_match = re.search(r"seasons/(\d{4})/", ref_url)
#     return int(season_match.group(1)) if season_match else None


# def extract_team_id_from_ref(ref_url: str) -> Optional[int]:
#     match = re.search(r"teams/(\d{1,2})(?:/|\?|$)", ref_url)
#     if match:
#         return int(match.group(1))
#     return None


def extract_id_from_ref(ref_url: str, key: str) -> Optional[int]:
    """ 
    Receives a $ref url and a given key ("seasons", "teams", "athletes")
    Returns the corresponding id value for the key after parsing through the ref_url
    """
    pattern = rf"{re.escape(key)}/(\d+)"
    match = re.search(pattern, ref_url)
    return int(match.group(1)) if match else None