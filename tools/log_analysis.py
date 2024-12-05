import re
from datetime import datetime

def parse_log(file_path):
    """Parse the log file and extract relevant information."""
    log_entries = []
    with open(file_path, 'r') as file:
        for line in file:
            match = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - (\w+) - (.+)', line)
            if match:
                timestamp = datetime.strptime(match.group(1), '%Y-%m-%d %H:%M:%S')
                log_level = match.group(2)
                message = match.group(3)
                log_entries.append({'timestamp': timestamp, 'level': log_level, 'message': message})
    return log_entries

def filter_logs(log_entries, level=None):
    """Filter logs by level."""
    if level:
        return [entry for entry in log_entries if entry['level'] == level]
    return log_entries

if __name__ == "__main__":
    logs = parse_log("logs/system.log")
    error_logs = filter_logs(logs, level="ERROR")
    for log in error_logs:
        print(f"[{log['timestamp']}] {log['level']}: {log['message']}")
