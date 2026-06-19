def detect_intrusion(ip):
    suspicious_ips = [
        "192.168.1.100",
        "10.10.10.10"
    ]

    if ip in suspicious_ips:
        return True

    return False
