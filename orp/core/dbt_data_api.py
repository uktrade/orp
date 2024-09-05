import logging

from typing import Any

import requests  # type: ignore

from requests.exceptions import RequestException  # type: ignore

from django.conf import settings


class DbtDataApi:
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)
        self.base_url = settings.DBT_DATA_API_URL
        self.logger.info(f"DBT Data API URL: {self.base_url}")
        self.headers = {
            "Content-Type": "application/json",
        }
            

    def _send_request(
        self, request_type: str, **params
    ) -> requests.Response:
        """Send search request."""

        url = f"{self.base_url}"
        self.logger.debug(f"Sending {request_type} request to {url}")
        return requests.request(
            method=request_type,
            url=url,
            headers=self.headers,
            params=params,
        )

    def search_regulations(
        self
    ) -> requests.Response:
        """Search for regulations."""
        
        params = {}
        return self._send_request("GET", "", **params)