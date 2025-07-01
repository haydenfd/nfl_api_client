import re
from typing import Optional 
from datetime import datetime
import pytz


def format_gamelog_date_str(date_str: str) -> str:
    utc_time = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f%z")
    eastern_zone = pytz.timezone("US/Eastern")
    eastern_time = utc_time.astimezone(eastern_zone)
    return eastern_time.strftime("%m-%d-%Y")

def format_utc_date_str(date_str: str) -> str:

    utc_time = datetime.strptime(date_str, "%Y-%m-%dT%H:%MZ")
    utc_zone = pytz.timezone("UTC")
    eastern_zone = pytz.timezone("US/Eastern")

    utc_aware = utc_zone.localize(utc_time)
    eastern_time = utc_aware.astimezone(eastern_zone)

    return eastern_time.strftime("%m-%d-%Y")

def format_date_str(date_str):
    return datetime.strptime(date_str, "%Y-%m-%dT%H:%MZ").strftime("%m-%d-%Y")


def extract_id_from_ref(ref_url: str, key: str) -> Optional[int]:
    """ 
    Receives a $ref url and a given key ("seasons", "teams", "athletes")
    Returns the corresponding id value for the key after parsing through the ref_url
    """
    pattern = rf"{re.escape(key)}/(\d+)"
    match = re.search(pattern, ref_url)
    return int(match.group(1)) if match else None

def camel_to_snake(name: str) -> str:
    overrides = {
        "QBRating": "qb_rating",
        "adjQBR": "adj_qbr",
    }
    if name in overrides:
        return overrides[name]
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()