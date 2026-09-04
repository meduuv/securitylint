"""Dependency-free configuration security linting."""

def lint(lines):
    findings = []
    for number, raw in enumerate(lines, 1):
        line = raw.strip().lower()
        if not line or line.startswith("#"):
            continue
        if "debug=true" in line or "debug = true" in line:
            findings.append({"line": number, "rule": "debug-enabled", "severity": "medium"})
        if "bind=0.0.0.0" in line or "bind = 0.0.0.0" in line:
            findings.append({"line": number, "rule": "wildcard-bind", "severity": "high"})
        if any(key in line for key in ("password=", "password =", "secret=", "secret =")):
            findings.append({"line": number, "rule": "plaintext-secret", "severity": "high"})
    return findings
