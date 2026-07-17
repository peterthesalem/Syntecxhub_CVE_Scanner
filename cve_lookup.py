CVE_DATABASE = {
    "OpenSSH_10.3": {
        "cve": "No known critical CVEs found in local database.",
        "severity": "Informational"
    },

    "OpenSSH_9": {
        "cve": "Example CVE entry",
        "severity": "Medium"
    },

    "Apache/2.4.68": {
        "cve": "Example CVE entry",
        "severity": "High"
    }
}


def lookup_cve(banner):
    for software in CVE_DATABASE:
        if software.lower() in banner.lower():
            return CVE_DATABASE[software]

    return {
        "cve": "No matching CVE found.",
        "severity": "Unknown"
    }
