"""
Module for coordinating log analysis.
"""
from typing import List
from src.types.log_entry import LogEntry
from src.types.analysis_results import AnalysisResults
from src.analyzers.ip_analyzer import IPAnalyzer
from src.analyzers.endpoint_analyzer import EndpointAnalyzer
from src.analyzers.security_analyzer import SecurityAnalyzer

class LogAnalyzer:
    """Coordinator for log analysis operations."""
    
    def __init__(self, failed_login_threshold: int = 10):
        self.security_analyzer = SecurityAnalyzer(failed_login_threshold)

    def analyze_logs(self, entries: List[LogEntry]) -> AnalysisResults:
        """Perform complete analysis of log entries."""
        return AnalysisResults(
            requests_per_ip=IPAnalyzer.count_requests_per_ip(entries),
            most_accessed_endpoint=EndpointAnalyzer.find_most_accessed_endpoint(entries),
            suspicious_activity=self.security_analyzer.detect_suspicious_activity(entries)
        )