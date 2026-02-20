description: Scan repo for hardcoded secrets (detect-secrets)
allowed-tools: Bash, Read, Write
prompt: |
  Scan the repository for hardcoded secrets.

  Run: python -m detect_secrets scan --all-files

  If potential secrets are found:
  - List file paths and line numbers
  - Recommend remediation (remove, move to env vars, rotate keys)
  - Do NOT print actual secret values

  At the end:
  - paste the scan output
  - summarize what needs fixing
