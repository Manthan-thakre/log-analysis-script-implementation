"""
Main script for log analysis.
"""
from log_parser import LogParser
from log_analyzer import LogAnalyzer
from report_generator import ReportGenerator

def main():
    """Main function to run the log analysis."""
    # Parse log file
    log_entries = LogParser.parse_file("sample.log")
    
    # Analyze logs
    analyzer = LogAnalyzer(failed_login_threshold=10)
    results = analyzer.analyze_logs(log_entries)
    
    # Generate reports
    ReportGenerator.display_results(results)
    ReportGenerator.save_to_csv(results)

if __name__ == "__main__":
    main()