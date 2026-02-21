#!/usr/bin/env python3
"""
summarize.py — prints a quick summary of a Python file's structure.

Usage: python3 scripts/summarize.py path/to/file.py

Claude can run this and use the output without loading the whole file.
"""

import sys
import ast

def summarize(filepath):
    try:
        with open(filepath, "r") as f:
            source = f.read()
    except FileNotFoundError:
        print(f"Error: File not found: {filepath}")
        sys.exit(1)

    try:
        tree = ast.parse(source)
    except SyntaxError as e:
        print(f"Error: Could not parse Python file: {e}")
        sys.exit(1)

    lines = source.splitlines()
    print(f"File: {filepath}")
    print(f"Lines: {len(lines)}")
    print()

    # Find top-level functions and classes
    functions = []
    classes = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and isinstance(node.col_offset, int) and node.col_offset == 0:
            functions.append((node.name, node.lineno))
        elif isinstance(node, ast.ClassDef):
            classes.append((node.name, node.lineno))

    if classes:
        print("Classes:")
        for name, line in classes:
            print(f"  line {line}: class {name}")
        print()

    if functions:
        print("Top-level functions:")
        for name, line in functions:
            print(f"  line {line}: def {name}()")
        print()

    if not classes and not functions:
        print("No classes or top-level functions found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/summarize.py <file.py>")
        sys.exit(1)
    summarize(sys.argv[1])
