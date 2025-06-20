from typing import Dict, List, Any

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
    
def parse_totals(names: List[str], totals: List[Any]) -> Dict[str, Any]:
    return {
        name: safe_cast_numeric(value)
        for name, value in zip(names, totals)
    }

def PlayerCareerStatsParser(data: Dict[str, Any]) -> Dict[str, List[Dict[str, Any]]]:
    """
    Parses the ESPN player career stats endpoint into a dictionary of stat categories.

    Each key corresponds to a stats category (e.g., "PASSING", "RUSHING"), and
    each value is a list of dictionaries: one for total stats, followed by season-wise stats.
    """
    parsed = {}
    categories_field = data.get("categories", [])

    for category in categories_field:
        category_name = category.get("name", "").upper()
        names = category.get("names", [])
        totals = category.get("totals", [])
        stats_by_season = category.get("statistics", [])

        data_set = []

        # Append career total if present
        if totals:
            data_set.append({
                "SEASON": "TOTAL",
                **parse_totals(names, totals)
            })

        # Append season-by-season stats
        for season_entry in stats_by_season:
            season_year = season_entry.get("season", {}).get("year")
            team_id = safe_cast_numeric(season_entry.get("teamId"))
            stats_values = season_entry.get("stats", [])

            if season_year:
                stat_row = {
                    "SEASON": season_year,
                    "TEAM_ID": team_id,
                    **parse_totals(names, stats_values)
                }
                data_set.append(stat_row)

        parsed[category_name] = data_set

    return parsed
