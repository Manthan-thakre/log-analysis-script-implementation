"""
Module for displaying analysis results in the terminal.
"""
from src.types.analysis_results import AnalysisResults

class TerminalReporter:
    """Reporter for terminal output."""

    @staticmethod
    def display_results(results: AnalysisResults) -> None:
        """Display analysis results in the terminal."""
        print("\n=== Requests per IP Address ===")
        print("IP Address           Request Count")
        print("-" * 35)
        for ip, count in sorted(results.requests_per_ip.items(), 
                              key=lambda x: x[1], reverse=True):
            print(f"{ip:<20} {count}")

        print("\n=== Most Frequently Accessed Endpoint ===")
        endpoint, count = results.most_accessed_endpoint
        print(f"{endpoint} (Accessed {count} times)")

        print("\n=== Suspicious Activity Detected ===")
        if results.suspicious_activity:
            print("IP Address           Failed Login Attempts")
            print("-" * 45)
            for ip, count in sorted(results.suspicious_activity.items(), 
                                  key=lambda x: x[1], reverse=True):
                print(f"{ip:<20} {count}")
        else:
            print("No suspicious activity detected.")