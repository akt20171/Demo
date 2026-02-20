# Calculator Agent Team

Team Goal:
Deliver changes using a disciplined pipeline: Plan → Implement → Lint → Test → Coverage → Security → Perf → Final.

Team Members (roles):
1) Planner
   - File: .claude/agents/planner.md
   - Output: 5–10 step plan, edge cases, impacted files. No code.

2) Implementer
   - File: .claude/agents/implementer.md
   - Output: minimal code changes per plan.

3) Lint/Format Operator
   - File: .claude/agents/lint_formatter.md
   - Output: black + ruff clean.

4) Test Writer
   - File: .claude/agents/test_writer.md
   - Output: tests added/updated for behavioral changes.

5) TDD Runner/Fixer
   - File: .claude/agents/test_runner.md
   - Output: pytest loop until green.

6) Coverage Gate Operator
   - File: .claude/agents/coverage_gate.md
   - Output: coverage >= 85% enforced.

7) Security Audit Operator
   - File: .claude/agents/security_audit.md
   - Output: bandit findings addressed.

8) Dependency Auditor
   - Command: python -m pip_audit
   - Output: vuln findings summarized + minimal upgrade plan.

9) Secrets Scanner
   - Command: python -m detect_secrets scan --all-files
   - Output: paths/lines only, no secret values.

10) Security Reviewer
    - File: .claude/agents/security_reviewer.md

11) Performance Reviewer
    - File: .claude/agents/performance_reviewer.md

Rules:
- Follow CLAUDE.md as the source of truth.
- If any step changes code/tests, re-run pytest -q.
- Final output must include: plan, files changed, final outputs (ruff/pytest/coverage/bandit/pip-audit/detect-secrets).
