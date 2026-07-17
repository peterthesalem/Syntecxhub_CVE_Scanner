def generate_report(host, port, banner, cve_info, severity):
    with open("reports/report.txt", "w") as report:
        report.write("Vulnerability Scanner Report\n")
        report.write("=" * 40 + "\n")
        report.write(f"Target: {host}:{port}\n")
        report.write(f"Banner: {banner}\n")
        report.write(f"CVE Information: {cve_info}\n")
        report.write(f"Severity: {severity}\n")
