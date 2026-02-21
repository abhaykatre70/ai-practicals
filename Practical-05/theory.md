# Theory – Cryptarithmetic Puzzle Solver

## Overview
A **Cryptarithmetic Puzzle** is an arithmetic equation where each letter represents a distinct digit (0–9). The challenge is to find the letter-to-digit mapping that makes the equation mathematically correct.

---

## Classic Example
```
  SEND
+ MORE
------
 MONEY
```
No two letters may share the same digit. The unique valid assignment gives:
- SEND = 9567, MORE = 1085, MONEY = 10652

---

## Constraints
1. Each letter maps to exactly one unique digit (0–9).
2. No two different letters share the same digit.
3. The resulting numbers must satisfy the arithmetic equation.

---

## Solving Approach – Backtracking
The puzzle is solved through **systematic trial with backtracking**:

1. Tentatively assign a digit to each letter.
2. Check if the assignment violates any constraint.
3. If a conflict is found, **backtrack** (revert the last assignment) and try the next available digit.
4. If all letters are assigned and the equation holds, the solution is found.

---

## Algorithm – Step-by-Step
1. Extract every distinct letter appearing in the puzzle words.
2. Assign digits 0–9 to letters one at a time.
3. Enforce the uniqueness constraint — no digit assigned to more than one letter.
4. Translate letter strings into numeric equivalents.
5. Verify whether the numbers satisfy the arithmetic equation.
6. If valid, report the solution; otherwise backtrack and try the next option.

---

## Applications
- Demonstrates **Constraint Satisfaction Problems (CSP)** in AI
- Applies backtracking to real combinatorial tasks
- Builds intuition for search-space pruning
- Foundational concept for advanced CSP solvers

---

## Summary
This practical shows how backtracking systematically explores a constrained search space to find the letter-to-digit assignment satisfying a given arithmetic puzzle. It highlights the interplay between **trial, validation, and rollback** that underpins many AI problem-solving strategies.
