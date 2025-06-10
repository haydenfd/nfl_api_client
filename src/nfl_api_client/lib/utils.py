# src/nfl_api/lib/utils.py

from datetime import datetime

def format_date_str(date_str):
    return datetime.strptime(date_str, "%Y-%m-%dT%H:%MZ").strftime("%m-%d-%Y")