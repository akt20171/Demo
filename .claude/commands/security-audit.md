description: Static code security scan (bandit) and resolve findings
allowed-tools: Bash, Read, Write
prompt: |
  Run a static security scan.

  1) Run: python -m bandit -r . -q

  If findings exist:
  - Fix real issues safely (no risky eval/exec/subprocess patterns, etc.)
  - If a finding is a false positive, add a brief comment explaining why.
  - Re-run bandit until results are acceptable.

  At the end:
  - paste the bandit output (summary)
  - list findings and what you did
