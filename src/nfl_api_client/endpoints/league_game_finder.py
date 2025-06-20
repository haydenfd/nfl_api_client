import httpx
from datetime import datetime
from nfl_api_client.lib.endpoint_registry import ENDPOINT_REGISTRY
import asyncio 
from nfl_api_client.lib.utils import format_date_str
import pandas as pd

class LeagueGameFinder:
    BASE_URL = ENDPOINT_REGISTRY["LEAGUE_GAME_FINDER"]

    def __init__(self, start_date: str, end_date: str, limit: int = 1000):
        self.start_date = self._validate_date(start_date)
        self.end_date = self._validate_date(end_date)
        self.limit = limit
        self._validate_range()
        self.url = self._build_url()
        print(self.url)
        self._games = []

    def _validate_date(self, date_str: str) -> str:
        if len(date_str) != 8 or not date_str.isdigit():
            raise ValueError(f"Invalid date format: {date_str}")
        year, month, day = int(date_str[:4]), int(date_str[4:6]), int(date_str[6:])
        datetime(year, month, day)  # will raise if invalid
        return date_str

    def _validate_range(self):
        d1 = datetime.strptime(self.start_date, "%Y%m%d")
        d2 = datetime.strptime(self.end_date, "%Y%m%d")
        if d2 < d1:
            raise ValueError("End date must not be earlier than start date")        
        if (d2 - d1).days > 366:
            raise ValueError("Date range must be <= 1 year")

    def _build_url(self) -> str:
        return f"{self.BASE_URL}?limit={self.limit}&dates={self.start_date}-{self.end_date}"

    async def fetch(self) -> list[dict]:
        async with httpx.AsyncClient() as client:
            response = await client.get(self.url)
            response.raise_for_status()
            events = response.json().get("events", [])
            self._games = [self._parse_event(event) for event in events if event]
            return self._games

    def _parse_event(self, event: dict) -> dict:
        comp = event.get("competitions", [])[0]
        competitors = comp.get("competitors", [])

        home = next((c for c in competitors if c.get("homeAway") == "home"), {})
        away = next((c for c in competitors if c.get("homeAway") == "away"), {})

        return {
            "game_id": event.get("id"),
            "season": event.get("season", {}).get("year"),
            "season_type": event.get("season", {}).get("type"),
            "date": format_date_str(event.get("date")),
            "week_number": event.get("week", {}).get("number"),
            "venue_full_name": comp.get("venue", {}).get("fullName"),
            "home_team": home.get("team", {}).get("abbreviation"),
            "away_team": away.get("team", {}).get("abbreviation"),
        }

    def to_dataframe(self) -> pd.DataFrame:
        return pd.DataFrame(self._games)
# --- Example usage ---
async def main():
    finder = LeagueGameFinder("20250901", "20260115")
    await finder.fetch()
    df = finder.to_dataframe()
    print(df.tail(20))

if __name__ == "__main__":
    asyncio.run(main())
