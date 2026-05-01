"""Config flow for the Fireboard integration.

Implementation lands in Phase 2 (task hHbF3Vv6).
"""

from __future__ import annotations

from homeassistant.config_entries import ConfigFlow

from .const import DOMAIN


class FireboardConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Fireboard."""

    VERSION = 1
