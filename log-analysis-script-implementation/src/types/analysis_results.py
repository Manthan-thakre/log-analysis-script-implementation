"""
Type definitions for analysis results.
"""
from dataclasses import dataclass
from typing import Dict, Tuple

@dataclass
class AnalysisResults:
    """Container for analysis results."""
    requests_per_ip: Dict[str, int]
    most_accessed_endpoint: Tuple[str, int]
    suspicious_activity: Dict[str, int]