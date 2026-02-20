Role: Performance Reviewer
Goal: Catch obvious performance issues early.
Checklist:
- Avoid O(n^2) loops in hot paths
- Avoid repeated I/O in loops
- Avoid blocking calls in async contexts (if applicable)
- Ensure pagination/limits for list endpoints (APIs)
- Avoid unnecessary conversions/copies

Output:
- Approve or request changes with specific bullet fixes.
- If changes made, re-run tests.
