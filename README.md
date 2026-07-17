# SyntecxHub CVE Scanner

## Description
A lightweight vulnerability scanner developed during the SyntecxHub Cybersecurity Internship.

The scanner performs:
- Banner grabbing
- Service detection
- Version identification
- Local CVE matching
- Severity classification
- Report generation
- Logging

## Project Structure

```
Syntecxhub_CVE_Scanner/
│
├── scanner.py
├── banner.py
├── cve_lookup.py
├── logger.py
├── report.py
├── config.py
├── README.md
├── requirements.txt
│
├── logs/
└── reports/
```

## Features
- Detects service banners
- Matches detected versions against a local CVE database
- Generates reports
- Stores scan history

## Example Output

```
Target: localhost:22
Banner: SSH-2.0-OpenSSH_10.3p1 Debian-4

CVE Information:
No known critical CVEs found in local database.

Severity:
Informational
```

## Technologies Used
- Python
- Socket Programming
- Kali Linux
- Git
- GitHub

## Ethical Notice
This project is intended strictly for educational purposes and authorized testing environments only.

## Author
PeterTheSalem
SOC Analyst Path | SyntecxHub Intern
