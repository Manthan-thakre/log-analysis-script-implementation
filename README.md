# Log Analysis Tool

A Python-based log analysis tool that processes web server logs to extract valuable insights about traffic patterns and potential security threats.

## Features

### 1. IP Address Analysis
- Tracks and counts requests from each IP address
- Sorts results by request frequency
- Helps identify unusual traffic patterns

### 2. Endpoint Monitoring
- Identifies the most frequently accessed endpoints
- Provides access counts for each endpoint
- Helps understand user behavior and resource utilization

### 3. Security Analysis
- Detects potential brute force login attempts
- Monitors failed login attempts per IP
- Flags suspicious activity based on configurable thresholds

## Project Structure

```
src/
├── analyzers/
│   ├── endpoint_analyzer.py
│   ├── ip_analyzer.py
│   ├── log_analyzer.py
│   └── security_analyzer.py
├── parsers/
│   ├── log_parser.py
│   └── log_pattern.py
├── reporters/
│   ├── csv_reporter.py
│   └── terminal_reporter.py
├── types/
│   ├── analysis_results.py
│   └── log_entry.py
└── main.py
```

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses standard library only)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd log-analysis-tool
```

2. Ensure you have Python 3.6+ installed:
```bash
python --version
```

## Usage

1. Place your log file in the project root directory as `sample.log`

2. Run the analysis:
```bash
python src/main.py
```

3. View the results:
- Terminal output will show immediate results
- Check `log_analysis_results.csv` for detailed analysis

## Output Format

### Terminal Output

```
=== Requests per IP Address ===
IP Address           Request Count
-----------------------------------
203.0.113.5          8
198.51.100.23        8
192.168.1.1          7
10.0.0.2             6
192.168.1.100        5

=== Most Frequently Accessed Endpoint ===
/login (Accessed 13 times)

=== Suspicious Activity Detected ===
No suspicious activity detected.
```

### CSV Output

The tool generates a CSV file (`log_analysis_results.csv`) with three sections:
1. Requests per IP
2. Most Accessed Endpoint
3. Suspicious Activity

## Configuration

You can modify the following parameters in `src/main.py`:

- `failed_login_threshold`: Number of failed login attempts before flagging as suspicious (default: 10)
- Output filename: Change the CSV output filename in the `CSVReporter.save_to_csv()` call

## Log Format

The tool expects logs in the following format:
```
IP_ADDRESS - - [TIMESTAMP] "METHOD ENDPOINT HTTP/1.1" STATUS_CODE RESPONSE_SIZE "ERROR_MESSAGE"
```

Example:
```
192.168.1.1 - - [03/Dec/2024:10:12:34 +0000] "GET /home HTTP/1.1" 200 512
```

## Architecture

The project follows a modular architecture with clear separation of concerns:

1. **Types** (`src/types/`)
   - Define data structures for log entries and analysis results

2. **Parsers** (`src/parsers/`)
   - Handle log file reading and parsing
   - Convert raw log lines into structured data

3. **Analyzers** (`src/analyzers/`)
   - Process parsed log data
   - Generate statistical analysis and insights

4. **Reporters** (`src/reporters/`)
   - Format and present analysis results
   - Generate terminal output and CSV reports

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.