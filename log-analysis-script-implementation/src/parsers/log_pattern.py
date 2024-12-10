"""
Regular expression patterns for log parsing.
"""

LOG_PATTERN = r'(\d+\.\d+\.\d+\.\d+).*\[(.*?)\]\s+"(\w+)\s+([^\s]+).*?"\s+(\d+)\s+(\d+)(?:\s+"([^"]*)")?'