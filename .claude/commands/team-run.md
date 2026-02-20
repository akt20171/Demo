description: Run Calculator Agent Team end-to-end
allowed-tools: Bash, Read, Write
prompt: |
  Agent Teams mode is enabled. Run the Calculator Agent Team described in:
  .claude/teams/calculator_team.md

  Execute the steps in the exact order defined by the team.
  Use the referenced agent instruction files for each role.

  Requirements:
  - Enforce the TDD loop: run python -m pytest -q; if failing, fix and rerun until green.
  - Enforce coverage: python -m pytest --cov=. --cov-report=term-missing --cov-fail-under=85
  - Run security tools: bandit, pip-audit, detect-secrets
  - Run final validation: ruff + pytest

  At the end, provide:
  - Plan
  - Files changed
  - Final outputs for all gates
  - 5-bullet summary
