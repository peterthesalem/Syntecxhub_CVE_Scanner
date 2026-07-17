from banner import grab_banner
from cve_lookup import lookup_cve
from report import generate_report
from logger import log_scan

host = input("Enter target host: ")
port = int(input("Enter target port: "))

print("\nScanning target...\n")

banner = grab_banner(host, port)

print("Banner Found:")
print(banner)

result = lookup_cve(banner)

print("\nPossible Vulnerabilities:")
print(f"CVE Information: {result['cve']}")
print(f"Severity: {result['severity']}")

generate_report(
    host,
    port,
    banner,
    result["cve"],
    result["severity"]
)

log_scan(
    host,
    port,
    banner,
    result["severity"]
)

print("\nReport saved to reports/report.txt")
print("Scan logged to logs/scan.log")
