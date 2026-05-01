"""Async client for the Fireboard Cloud REST API.

Implementation lands in Phase 1 (task ISWssIEb).
"""

from __future__ import annotations


class FireboardError(Exception):
    """Base exception for Fireboard API errors."""


class FireboardAuthError(FireboardError):
    """Authentication failed (invalid credentials or expired token)."""


class FireboardRateLimitError(FireboardError):
    """Rate limit exceeded — back off."""


class FireboardApiError(FireboardError):
    """Generic API/transport error."""
