"""
Module for analyzing security-related patterns.
"""
from collections import Counter
from typing import List, Dict
from src.types.log_entry import LogEntry

class SecurityAnalyzer:
    """Analyzer for security-related patterns."""
    
    def __init__(self, failed_login_threshold: int = 10):
        self.failed_login_threshold = failed_login_threshold

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