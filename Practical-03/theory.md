# Theory – Tic-Tac-Toe Game Engine with AI Player

## Overview
Tic-Tac-Toe is a two-player strategy game played on a **3×3 grid**. This practical builds a working game engine in Python where a **human player** competes against a **rule-based AI opponent**. The objective is to align three matching symbols in any row, column, or diagonal before the opponent does.

---

## Game Rules
1. The board is a 3×3 grid.
2. The human player uses **X**; the AI uses **O**.
3. Players alternate turns.
4. A player wins when three of their symbols align horizontally, vertically, or diagonally.
5. If all cells are filled with no winner, the game ends in a **draw**.

---

## Board Representation
The board is stored as a 2D list. A sample mid-game state:

```
-------------
| X | O | X |
-------------
| X | O |   |
-------------
|   |   | O |
-------------
```

---

## AI Decision Logic (Priority Order)
The computer selects a move using these rules in order:

| Priority | Rule |
|----------|------|
| 1 | **Win** – if placing O at any empty cell results in a win, take that cell |
| 2 | **Block** – if the human can win on their next move, block that cell |
| 3 | **Random** – if neither condition applies, pick any available cell at random |

---

## Algorithm – Step-by-Step Flow
1. Create an empty 3×3 grid.
2. Human places X first.
3. After each move check for a win condition.
4. On the AI's turn, apply decision rules to pick the optimal cell.
5. Alternate turns until a win or draw is detected.
6. Print the final board and announce the result.

---

## Applications
- Foundational concept in game AI development
- Basis for understanding advanced algorithms like Minimax
- Demonstrates human-computer interaction patterns
- Useful in educational tools and simple decision engines

---

## Summary
This practical demonstrates how a **rule-based AI agent** can play Tic-Tac-Toe competently by evaluating the board after every move and applying a fixed priority strategy. It provides a clear illustration of how simple heuristics can produce intelligent-seeming behaviour in games.
