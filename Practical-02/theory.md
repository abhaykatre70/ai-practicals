# Theory – Water Jug Problem

## Overview
The **Water Jug Problem** is a classic AI problem that demonstrates **state-space search** and **rule-based transitions**. Two containers of different capacities are used, and the goal is to reach a desired water quantity using a set of allowed operations.

---

## Problem Setup
- **Jug A** — capacity: 4 litres
- **Jug B** — capacity: 3 litres
- Unlimited water source available
- Neither jug has measurement markings

**Goal:** Measure exactly **2 litres** in Jug A.

---

## State Representation
Every configuration is expressed as a tuple **(a, b)**, where:
- `a` = current volume in Jug A
- `b` = current volume in Jug B

**Initial state:** (0, 0) | **Goal state:** (2, 0)

---

## Allowed Operations (Production Rules)
| Rule | Operation |
|------|-----------|
| R1 | Fill Jug A completely |
| R2 | Fill Jug B completely |
| R3 | Empty Jug A |
| R4 | Empty Jug B |
| R5 | Pour water from A into B (until B full or A empty) |
| R6 | Pour water from B into A (until A full or B empty) |

---

## Algorithm – Breadth-First Search (BFS)
1. Start from the initial state (0, 0).
2. Apply every valid operation to generate successor states.
3. Track visited states to prevent infinite loops.
4. Expand states level by level until the goal is found.
5. Output the path from initial to goal state.

---

## Summary
This practical demonstrates how a logical problem can be modelled as a graph of states and solved via systematic BFS exploration. BFS guarantees finding the **shortest sequence** of operations to reach the desired water measurement.
