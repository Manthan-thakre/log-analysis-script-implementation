"""
Module for analyzing log entries and generating statistics.
"""
from collections import Counter
from dataclasses import dataclass
from typing import List, Dict, Tuple
from log_parser import LogEntry

@dataclass
class AnalysisResults:
    """Container for analysis results."""
    requests_per_ip: Dict[str, int]
    most_accessed_endpoint: Tuple[str, int]
    suspicious_activity: Dict[str, int]

class LogAnalyzer:
    """Analyzer for processing log entries and generating statistics."""
    
    def __init__(self, failed_login_threshold: int = 10):
        self.failed_login_threshold = failed_login_threshold

    def count_requests_per_ip(self, entries: List[LogEntry]) -> Dict[str, int]:
        """Count the number of requests made by each IP address."""
        return dict(Counter(entry.ip_address for entry in entries))

    def find_most_accessed_endpoint(self, entries: List[LogEntry]) -> Tuple[str, int]:
        """Find the most frequently accessed endpoint."""
        endpoint_counts = Counter(entry.endpoint for entry in entries)
        return endpoint_counts.most_common(1)[0]

    def detect_suspicious_activity(self, entries: List[LogEntry]) -> Dict[str, int]:
        """Identify IP addresses with suspicious login activity."""
        failed_logins = Counter()
        
        for entry in entries:
            if (entry.endpoint == "/login" and 
                entry.status_code == 401 and 
                "Invalid credentials" in (entry.error_message or "")):
                failed_logins[entry.ip_address] += 1
        
        return {ip: count for ip, count in failed_logins.items() 
                if count >= self.failed_login_threshold}

    def analyze_logs(self, entries: List[LogEntry]) -> AnalysisResults:
        """Perform complete analysis of log entries."""
        return AnalysisResults(
            requests_per_ip=self.count_requests_per_ip(entries),
            most_accessed_endpoint=self.find_most_accessed_endpoint(entries),
            suspicious_activity=self.detect_suspicious_activity(entries)
        )