description: Performance reviewer step (manual reasoning + minimal improvements)
allowed-tools: Read, Write
prompt: |
  Perform a performance review of the code changes.

  Check for:
  - Inefficient loops (O(n^2) where avoidable)
  - Unnecessary conversions/copies
  - Repeated I/O in loops
  - Any obvious wasteful patterns

  For this small project, keep changes minimal.
  If you change code, note what changed and why.
