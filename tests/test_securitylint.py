from securitylint import lint

def test_detects_risky_settings():
    findings = lint(["debug=true", "bind=0.0.0.0", "password=demo"])
    assert {f["rule"] for f in findings} == {"debug-enabled", "wildcard-bind", "plaintext-secret"}
