description: Full security suite (bandit + pip-audit + detect-secrets)
allowed-tools: Bash, Read, Write
prompt: |
  Run the full security suite and summarize results.

  1) Code scan:
     python -m bandit -r . -q

  2) Dependency vulnerability scan:
     python -m pip_audit

  3) Secrets scan:
     python -m detect_secrets scan --all-files

  If issues appear:
  - Categorize: CODE vs DEPENDENCIES vs SECRETS
  - Fix CODE issues directly when appropriate
  - For dependencies, propose minimal safe upgrades (avoid major jumps unless required)
  - For secrets, recommend remediation steps WITHOUT exposing secret values

  At the end:
  - Provide a short status summary for each scan
  - Paste the outputs
