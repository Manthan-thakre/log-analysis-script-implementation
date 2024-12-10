"""
Main script for log analysis.
"""
from src.parsers.log_parser import LogParser
from src.analyzers.log_analyzer import LogAnalyzer
from src.reporters.terminal_reporter import TerminalReporter
from src.reporters.csv_reporter import CSVReporter

def main():
    """Main function to run the log analysis."""
    # Parse log file
    log_entries = LogParser.parse_file("sample.log")
    
    # Analyze logs
    analyzer = LogAnalyzer(failed_login_threshold=10)
    results = analyzer.analyze_logs(log_entries)
    
    # Generate reports
    TerminalReporter.display_results(results)
    CSVReporter.save_to_csv(results)

if __name__ == "__main__":
    main()