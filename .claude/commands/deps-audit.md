description: Dependency vulnerability scan (pip-audit) and propose minimal upgrades
allowed-tools: Bash, Read, Write
prompt: |
  Scan Python dependencies for known vulnerabilities.

  Run: python -m pip_audit

  If vulnerabilities are found:
  - Summarize each finding (package + recommended fixed version)
  - Propose minimal remediation (prefer smallest safe upgrade)
  - Avoid major version jumps unless necessary; explain risk

  If a requirements file exists, suggest the pin updates.
  At the end:
  - paste the pip-audit output
  - provide a short remediation plan
