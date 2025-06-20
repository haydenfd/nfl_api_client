from src.nfl_api_client.endpoints._base import BaseEndpoint
from src.nfl_api_client.lib.parameters import SeasonTypeID
from typing import Dict, Optional, Union
from nfl_api_client.lib.endpoint_registry import ENDPOINT_REGISTRY

ALLOWED_DAYS = {"sunday", "thursday", "monday"}
class SeasonScheduleWeekday(BaseEndpoint):
    BASE_URL = ENDPOINT_REGISTRY["SEASON_SCHEDULE_WEEKDAY"]

    def __init__(
            self, 
            season: int = 2024,
            day: str = "sunday",
            *,
            headers: Optional[Dict[str, str]] = None,
            proxy: Optional[str] = None,
            timeout: Optional[int] = None,      
    ):
        self.day = day.lower()

        if self.day not in ["sunday", "thursday", "monday"]:
            raise ValueError(f'{self.day} is not a valid day of week. Choose between Monday, Thursday, or Sunday.')

        # TODO: Add type validation for season_type
        url = self.BASE_URL.format(day=day, seson=season)
        super().__init__(
            url, 
            parser=None,
            headers=headers,
            proxy=proxy,
            timeout=timeout,
        )


        