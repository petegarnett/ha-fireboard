# Architecture

## Overview

This integration follows Home Assistant's canonical cloud-polling pattern:

```
┌──────────────────────────────────────────────────────────────┐
│                      Home Assistant                          │
│                                                              │
│  ┌────────────────────┐         ┌──────────────────────┐   │
│  │  Config Flow       │         │  Options Flow        │   │
│  │  (config_flow.py)  │         │  (config_flow.py)    │   │
│  └─────────┬──────────┘         └──────────┬───────────┘   │
│            │ creates                        │ updates       │
│            ▼                                ▼               │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  ConfigEntry (entry.runtime_data = coordinator)      │  │
│  └─────────┬────────────────────────────────────────────┘  │
│            │                                                │
│            ▼                                                │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  FireboardDataUpdateCoordinator (coordinator.py)     │  │
│  │  - Single instance per account                       │  │
│  │  - Polls every ~30s                                  │  │
│  │  - Holds: { devices, temps, drivelogs, sessions }    │  │
│  └─────────┬────────────────────────────────────────────┘  │
│            │ uses                                           │
│            ▼                                                │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  FireboardClient (api.py)                            │  │
│  │  - aiohttp wrapper                                   │  │
│  │  - Token-bucket rate limiter (17 / 5 min)            │  │
│  │  - Custom exceptions                                 │  │
│  └─────────┬────────────────────────────────────────────┘  │
│            │                                                │
│            │ HTTPS                                          │
│            ▼                                                │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  fireboard.io REST API                               │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Entity platforms (sensor.py, binary_sensor.py)      │  │
│  │  - CoordinatorEntity subclasses                      │  │
│  │  - Read from coordinator.data                        │  │
│  │  - One HA device per Fireboard, sensors grouped      │  │
│  └──────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────┘
```

## Key design decisions

### Single coordinator per account

We use **one** `DataUpdateCoordinator` for the whole account, not one per device. This is essential because the Fireboard API rate limit (17 calls / 5 min) is per-account, not per-device. A single coordinator can plan its calls globally and stay safely under the limit.

### Rate limit guard in the API client

The client maintains an internal token bucket: 17 tokens, replenished smoothly over a 300s window. When a call is requested with no tokens available, it either delays (if the wait is short) or raises `FireboardRateLimitError` (if it would block too long).

### Read-only in v1

The documented Fireboard API is GET-only. Until we verify undocumented write endpoints (planned for v1.1), we only expose sensor/binary_sensor entities. No `number` or `switch` entities.

### Modern HA patterns

- `entry.runtime_data` (not `hass.data[DOMAIN]`)
- `async_config_entry_first_refresh()` for fail-fast setup
- `ConfigEntryAuthFailed` from coordinator → automatic reauth flow
- `has_entity_name = True` + `translation_key` for entity naming
- `strings.json` as the single source of truth for UI text

## Phases

See [the project scope](https://github.com/petegarnett/ha-fireboard#wip) and the linked issues for phase-by-phase progress.
