"""
Module for generating and saving analysis reports.
"""
import csv
from typing import Dict, Tuple
from log_analyzer import AnalysisResults

class ReportGenerator:
    """Generator for creating and saving analysis reports."""

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

    @staticmethod
    def save_to_csv(results: AnalysisResults, filename: str = "log_analysis_results.csv") -> None:
        """Save analysis results to a CSV file."""
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            
            # Requests per IP
            writer.writerow(["=== Requests per IP ==="])
            writer.writerow(["IP Address", "Request Count"])
            for ip, count in sorted(results.requests_per_ip.items(), 
                                  key=lambda x: x[1], reverse=True):
                writer.writerow([ip, count])
            
            # Most Accessed Endpoint
            writer.writerow([])
            writer.writerow(["=== Most Accessed Endpoint ==="])
            writer.writerow(["Endpoint", "Access Count"])
            writer.writerow([results.most_accessed_endpoint[0], 
                           results.most_accessed_endpoint[1]])
            
            # Suspicious Activity
            writer.writerow([])
            writer.writerow(["=== Suspicious Activity ==="])
            writer.writerow(["IP Address", "Failed Login Count"])
            for ip, count in sorted(results.suspicious_activity.items(), 
                                  key=lambda x: x[1], reverse=True):
                writer.writerow([ip, count])