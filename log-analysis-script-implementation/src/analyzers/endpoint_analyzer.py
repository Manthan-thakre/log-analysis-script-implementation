"""
Module for analyzing endpoint-related statistics.
"""
from collections import Counter
from typing import List, Tuple
from src.types.log_entry import LogEntry

class EndpointAnalyzer:
    """Analyzer for endpoint-related statistics."""
    
    @staticmethod
    def find_most_accessed_endpoint(entries: List[LogEntry]) -> Tuple[str, int]:
        """Find the most frequently accessed endpoint."""
        endpoint_counts = Counter(entry.endpoint for entry in entries)
        return endpoint_counts.most_common(1)[0]