"""The Fireboard integration."""

from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import PLATFORMS

# Type alias for typed runtime_data — populated in Phase 3
# Will become ConfigEntry[FireboardCoordinator] later.
type FireboardConfigEntry = ConfigEntry


async def async_setup_entry(hass: HomeAssistant, entry: FireboardConfigEntry) -> bool:
    """Set up Fireboard from a config entry."""
    # Phase 3 will:
    # - construct FireboardClient + FireboardDataUpdateCoordinator
    # - call coordinator.async_config_entry_first_refresh()
    # - assign coordinator to entry.runtime_data
    # - forward to platforms
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: FireboardConfigEntry) -> bool:
    """Unload a config entry."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
