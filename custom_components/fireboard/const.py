"""Constants for the Fireboard integration."""

from __future__ import annotations

from datetime import timedelta
from typing import Final

DOMAIN: Final = "fireboard"

# API
API_BASE_URL: Final = "https://fireboard.io"
API_LOGIN_PATH: Final = "/api/rest-auth/login/"
API_DEVICES_PATH: Final = "/api/v1/devices.json"
API_DEVICE_PATH: Final = "/api/v1/devices/{uuid}.json"
API_TEMPS_PATH: Final = "/api/v1/devices/{uuid}/temps.json"
API_DRIVELOG_PATH: Final = "/api/v1/devices/{uuid}/drivelog.json"
API_SESSIONS_PATH: Final = "/api/v1/sessions.json"

# User-Agent — required by Fireboard API as of 2025-01-02
USER_AGENT: Final = "ha-fireboard/0.0.1 (+https://github.com/petegarnett/ha-fireboard)"

# Polling
DEFAULT_SCAN_INTERVAL: Final = timedelta(seconds=30)
MIN_SCAN_INTERVAL_SECONDS: Final = 30

# Rate limit: 17 calls per rolling 5-minute window
RATE_LIMIT_CALLS: Final = 17
RATE_LIMIT_WINDOW_SECONDS: Final = 300

# Config keys
CONF_TOKEN: Final = "token"
CONF_SCAN_INTERVAL: Final = "scan_interval"

# Platforms
PLATFORMS: Final = ["sensor", "binary_sensor"]
