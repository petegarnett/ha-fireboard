"""Binary sensor platform for Fireboard.

Implementation lands in Phase 3 (task y1bQjmZE).
"""

from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Fireboard binary sensors from a config entry."""
    # Phase 3: read coordinator from entry.runtime_data and create entities.
    return
