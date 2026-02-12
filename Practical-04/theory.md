# Theory – A* Pathfinding Algorithm

## Overview
**A*** (A-Star) is an **informed search algorithm** used in AI to find the least-cost path between a source and a target node in a graph. It combines the actual path cost with a heuristic estimate to efficiently guide the search.

---

## Evaluation Function
A* uses a single scoring formula at every node:

**f(n) = g(n) + h(n)**

| Term | Meaning |
|------|---------|
| **g(n)** | Accumulated cost from the source to node n |
| **h(n)** | Heuristic estimate of the remaining cost from n to the goal |
| **f(n)** | Total estimated cost of the path through n |

---

## Key Data Structures
| Structure | Purpose |
|-----------|---------|
| **Open Set (Frontier)** | Discovered nodes not yet fully processed |
| **Closed Set (Explored)** | Nodes whose neighbours have been examined |
| **Heuristic h(n)** | Admissible estimate of the distance to the goal |

---

## Algorithm – Step-by-Step
1. Add the start node to the frontier with g = 0, f = h(start).
2. Extract the node with the **minimum f value** from the frontier.
3. If it is the goal, reconstruct and return the path.
4. Otherwise, examine each of its neighbours.
5. For each neighbour, compute the tentative g cost via the current node.
6. If this cost is better than the previously recorded g, update the neighbour and add it to the frontier.
7. Repeat until the goal is reached or the frontier is empty.

---

## A* vs BFS Comparison
| Feature | BFS | A* |
|---------|-----|----|
| Search type | Uninformed | Informed (heuristic) |
| Optimal | Yes (unweighted) | Yes (admissible h) |
| Efficiency | Explores all nodes level by level | Skips unlikely paths |
| Speed | Slower on large graphs | Faster with good heuristic |

---

## Applications
- Navigation and route planning (GPS)
- Autonomous robot pathfinding
- NPC movement in video games
- Network routing and logistics

---

## Summary
A* blends the completeness of uniform-cost search with the speed of greedy best-first search. By combining actual path cost with a heuristic estimate, it explores fewer nodes while still guaranteeing an optimal solution — making it one of the most practical search algorithms in AI.
