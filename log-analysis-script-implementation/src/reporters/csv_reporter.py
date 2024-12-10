"""
Module for saving analysis results to CSV.
"""
import csv
from src.types.analysis_results import AnalysisResults

class CSVReporter:
    """Reporter for CSV output."""

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