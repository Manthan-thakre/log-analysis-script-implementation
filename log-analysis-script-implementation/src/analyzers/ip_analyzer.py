"""
Module for analyzing IP-related statistics.
"""
from collections import Counter
from typing import List, Dict
from src.types.log_entry import LogEntry

class IPAnalyzer:
    """Analyzer for IP-related statistics."""
    
    @staticmethod
    def count_requests_per_ip(entries: List[LogEntry]) -> Dict[str, int]:
        """Count the number of requests made by each IP address."""
        return dict(Counter(entry.ip_address for entry in entries))