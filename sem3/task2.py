import re

file_path_const = 'source2.txt'

time_template = '([0-9]{4})-([0-9]{2})-([0-9]{2})\\s([0-9]{2}):([0-9]{2}):([0-9]{2})'
log_msg_template = time_template + '\\s([A-Z]{4,5})'
ip_template = r'([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})'
log_level_template = r'\b[A-Z]{4,5}\b'

def resolve_log_message(log: str) -> str:
    log_time = re.search(time_template, log).group()
    log_message = log.replace(re.search(log_msg_template, log).group(), "").strip()
    log_level = re.search(log_level_template, log).group()
    return f"{log_time}, {log_level}, {log_message}"

def find_log_by_ip(logs: list[str]):

    for log in logs:
        if re.search(ip_template, log) is not None:
            print(resolve_log_message(log))

def find_log_by_error_level(logs: list[str], log_levels: list[str]):
    for log_level in log_levels:
        for log in logs:
            if log_level not in log:
                continue

            print(resolve_log_message(log))

def read(file_path: str) -> list[str]:
    logs = []
    with open(file_path, 'r') as f:
        for line in f.readlines():
            logs.append(line)

    return logs

def main():
    logs = read(file_path_const)

    print("error by log_level")
    find_log_by_error_level(logs, ['ERROR', "WARN"])
    print("error by ip")
    find_log_by_ip(logs)

if __name__ == '__main__':
    main()