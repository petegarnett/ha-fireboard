# Fireboard for Home Assistant

[![HACS Validate](https://github.com/petegarnett/ha-fireboard/actions/workflows/validate.yml/badge.svg)](https://github.com/petegarnett/ha-fireboard/actions/workflows/validate.yml)
[![Lint & Test](https://github.com/petegarnett/ha-fireboard/actions/workflows/lint-test.yml/badge.svg)](https://github.com/petegarnett/ha-fireboard/actions/workflows/lint-test.yml)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)

A native [Home Assistant](https://www.home-assistant.io/) integration for [Fireboard](https://www.fireboardlabs.com/) wireless BBQ thermometers, built to Home Assistant's modern integration standards.

> 🚧 **Work in progress.** This integration is under active development. Watch the repo for the v1.0 release.

## Why this integration?

This is the first Fireboard integration for Home Assistant built to the **Silver quality scale**, using HA's canonical patterns:

- ✅ UI-based config flow (no YAML)
- ✅ `DataUpdateCoordinator` with rate-limit-aware polling
- ✅ Reauth flow + options flow
- ✅ Modern entity translations (`has_entity_name`, `translation_key`)
- ✅ Device registry — one HA device per Fireboard, sensors grouped
- ✅ Brand assets submitted to home-assistant/brands
- ✅ HACS-ready, with hassfest + HACS Action validation in CI
- ✅ Targets Apache-2.0 license to match Home Assistant Core

## Supported hardware

- Fireboard 2 Drive

Other Fireboard models (FBX2, Spark, Pellet Drive) are likely to work but are untested in v1. Open an issue if you'd like to help validate.

## What it does

For each Fireboard on your account, this integration creates one Home Assistant device with the following entities:

| Entity | Description |
|---|---|
| `sensor.<device>_probe_<n>_temperature` | Per-channel probe temperature |
| `sensor.<device>_battery` | Battery level (where reported) |
| `sensor.<device>_signal_strength` | RSSI / signal strength |
| `sensor.<device>_drive_percent` | Fan speed % (Drive units only) |
| `sensor.<device>_drive_setpoint` | Read-only target setpoint (Drive units only) |
| `binary_sensor.<device>_online` | Connectivity (based on freshness of last reading) |
| `binary_sensor.<device>_session_active` | True when an open cook session exists |

**v1 is read-only.** The Fireboard public REST API does not expose write endpoints for setpoints, fan speed, or alerts. Setpoint control via undocumented endpoints is being investigated for v1.1.

## Installation

### HACS (recommended, once published)

1. Open HACS in Home Assistant
2. Click "Integrations"
3. Click the three dots → "Custom repositories"
4. Add `https://github.com/petegarnett/ha-fireboard` as an Integration
5. Install "Fireboard"
6. Restart Home Assistant
7. Go to **Settings → Devices & Services → Add Integration → Fireboard**

### Manual

1. Copy `custom_components/fireboard/` into your Home Assistant `config/custom_components/` directory
2. Restart Home Assistant
3. Go to **Settings → Devices & Services → Add Integration → Fireboard**

## Configuration

You'll be prompted for your Fireboard account credentials (username + password). These are exchanged for an API token, and only the token is stored. Your password is never persisted.

### Options

After setup, click "Configure" on the integration card to adjust:

- **Polling interval** (default: 30 seconds; minimum: 30s to respect Fireboard's 17-calls-per-5-min rate limit)
- **Temperature unit** (defaults to your Home Assistant unit system)

## Rate limits

Fireboard's Cloud API allows **17 API calls per rolling 5-minute window**. This integration uses a single account-level coordinator and an internal token-bucket rate limiter to stay safely under that limit. With one device the typical load is ~13 calls per 5 minutes; with multiple devices the integration scales the polling interval up automatically.

## Troubleshooting

- **"Invalid authentication"** — Double-check your Fireboard username and password by signing in at [fireboard.io](https://fireboard.io). If that works but the integration still fails, please open an issue.
- **Entities show "unavailable"** — The Fireboard cloud or your device is offline. The `binary_sensor.online` entity reflects this.
- **Rate limit errors** — Should not happen during normal operation. If you see them in logs, please open an issue with diagnostics.

## Diagnostics

From the integration card, click "Download diagnostics" to get a redacted dump of API responses and integration state. Attach this to bug reports.

## Contributing

Contributions are welcome. Please:

1. Open an issue first to discuss significant changes
2. Run `ruff check .` and `pytest` before submitting
3. Add tests for any new behaviour

See [docs/architecture.md](docs/architecture.md) for an overview of how the integration is structured.

## License

Apache-2.0 — see [LICENSE](LICENSE).

## Acknowledgements

- The Home Assistant developer team for excellent integration documentation
- Fireboard Labs for documenting their [Cloud API](https://docs.fireboard.io/app/app-api/)
- Prior community efforts (`fireboard2mqtt`, `mbettersworth/ha-fireboard`, `GarthDB/ha-fireboard`, `johnpdowling/ha-fireboard-sensors`) for proving the territory

This integration is not affiliated with or endorsed by Fireboard Labs, Inc.
