"""
Type definitions for log entries.
"""
from dataclasses import dataclass
from typing import Optional

@dataclass
class LogEntry:
    """Represents a parsed log entry with relevant fields."""
    ip_address: str
    timestamp: str
    method: str
    endpoint: str
    status_code: int
    response_size: int
    error_message: Optional[str] = None