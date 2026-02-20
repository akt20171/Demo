description: Perform security reviewer step after audit
allowed-tools: Read, Write
prompt: |
  Use .claude/agents/security_reviewer.md.
  Review the changes for security risks and request/fix issues.
  If changes are made, rerun tests and bandit.
