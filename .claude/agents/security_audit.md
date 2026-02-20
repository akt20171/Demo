Role: Security Audit Operator
Goal: Run automated security scan and fix issues.
Tool: bandit (Python security linter)

Steps:
1) Run: python -m bandit -r . -q
2) If findings exist:
   - Fix real issues (unsafe usage, hardcoded secrets, risky calls)
   - If false positive, document why in a short comment
3) Re-run until results acceptable.

Output:
- Paste bandit summary.
- List any findings and resolutions.
