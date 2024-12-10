"""
Module for parsing log file entries and extracting relevant information.
"""
import re
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

class LogParser:
    """Parser for processing log file entries."""
    
    LOG_PATTERN = r'(\d+\.\d+\.\d+\.\d+).*\[(.*?)\]\s+"(\w+)\s+([^\s]+).*?"\s+(\d+)\s+(\d+)(?:\s+"([^"]*)")?'
    
    @staticmethod
    def parse_line(line: str) -> Optional[LogEntry]:
        """Parse a single log line and return a LogEntry object."""
        match = re.match(LogParser.LOG_PATTERN, line)
        if not match:
            return None
            
        return LogEntry(
            ip_address=match.group(1),
            timestamp=match.group(2),
            method=match.group(3),
            endpoint=match.group(4),
            status_code=int(match.group(5)),
            response_size=int(match.group(6)),
            error_message=match.group(7) if len(match.groups()) > 6 else None
        )

    @staticmethod
    def parse_file(filename: str) -> list[LogEntry]:
        """Parse the entire log file and return a list of LogEntry objects."""
        entries = []
        with open(filename, 'r') as file:
            for line in file:
                entry = LogParser.parse_line(line.strip())
                if entry:
                    entries.append(entry)
        return entries