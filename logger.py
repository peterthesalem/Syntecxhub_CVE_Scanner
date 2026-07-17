from datetime import datetime

def log_scan(host, port, banner, severity):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("logs/scan.log", "a") as logfile:
        logfile.write(
            f"[{timestamp}] "
            f"Target: {host}:{port} | "
            f"Banner: {banner} | "
            f"Severity: {severity}\n"
        )
