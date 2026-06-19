from datetime import datetime

def log_dns(domain):
    with open("logs/security_logs.txt", "a") as file:
        file.write(
            f"{datetime.now()} | DNS Request | {domain}\n"
        )
