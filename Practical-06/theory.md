# Theory – Alpha-Beta Pruning in Game Trees

## Overview
**Alpha-Beta Pruning** is an optimization of the **Minimax algorithm** used in adversarial two-player game AI. It eliminates branches of the game tree that cannot affect the final decision, allowing the search to reach greater depths in the same amount of time.

---

## Minimax Algorithm
Minimax applies to zero-sum two-player games:

- The **maximizing player** tries to achieve the highest possible score.
- The **minimizing player** tries to achieve the lowest possible score.

The algorithm recursively evaluates all reachable game states and propagates scores upward, alternating between maximization and minimization at each level.

---

## How Alpha-Beta Pruning Works
Two running bounds are maintained:

| Bound | Maintained by | Meaning |
|-------|--------------|---------|
| **Alpha (α)** | Maximizing player | Best (highest) score found so far on the current path |
| **Beta (β)** | Minimizing player | Best (lowest) score found so far on the current path |

**Pruning condition:** If **α ≥ β** at any node, the remaining children of that node are skipped — they cannot change the outcome for either player.

---

## Algorithm – Step-by-Step
1. Start at the root with α = −∞ and β = +∞.
2. At a **MAX node**: choose the child with the highest value; update α.
3. At a **MIN node**: choose the child with the lowest value; update β.
4. If α ≥ β at any point, **prune** (stop exploring remaining children of that node).
5. Return the optimal value to the root.

---

## Advantages Over Plain Minimax
| Feature | Minimax | Alpha-Beta |
|---------|---------|-----------|
| Nodes explored | All | Only promising branches |
| Search depth | Limited | Deeper in same time |
| Result quality | Optimal | Identical to Minimax |
| Efficiency | O(b^d) | O(b^(d/2)) best case |

---

## Applications
- Chess, Go, and Checkers engines
- Tic-Tac-Toe AI solvers
- Othello and board game AIs
- General adversarial decision-making systems

---

## Summary
Alpha-Beta Pruning preserves the correctness of Minimax while eliminating redundant computation. By tracking upper and lower score bounds and discarding out-of-range branches, it results in **faster and more scalable game-tree evaluation**.
