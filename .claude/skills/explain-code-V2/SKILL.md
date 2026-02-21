---
name: explain-code-V2
description: Explains code with visual diagrams and analogies. Use when
  explaining how code works, teaching about a codebase, or when the user
  asks "how does this work?" or "walk me through this."
allowed-tools: Read, Grep
---

# Code Explainer Skill

When explaining code, always follow this structure:

## 1. Start with an analogy
Compare the code to something from everyday life.
Example: "A function is like a recipe — you give it ingredients, it follows steps, and returns a result."

## 2. Draw an ASCII diagram
Show the flow, structure, or relationships visually.

Example for a function call:

```
Input --> [Function] --> Output
  |                        |
"hello"   reverses it   "olleh"
```

## 3. Walk through the code step-by-step
Explain what each part does in plain English.
Keep each step to 1-2 sentences.

## 4. Highlight a gotcha
End with one common mistake or misconception.
Example: "A common mistake is forgetting that Python lists are mutable —
changing a copy also changes the original."

## 5. Output
  Provide output mermaid code to depict high level flow in separate mermaid-v2.md
  This should be semantic versions so that it generate new unique file.  
  Please output the code review findings into two separate files i.e explain-code-V2-findings.md and explain-code-V2-findings.pdf in two separate formats.
  This should be semantic versions so that it generate new unique file.  
---

For Python-specific patterns and terms, see `reference.md`.
For a visual summary of a file, you can run `scripts/summarize.py`.

Keep explanations conversational. Assume the reader is a beginner.
