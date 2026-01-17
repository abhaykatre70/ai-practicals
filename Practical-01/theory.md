# Theory – Magic Square Generation

## Overview
A **Magic Square** is an n × n grid filled with distinct positive integers (1 to n²) such that every row, column, and both principal diagonals add up to the same fixed value — the **Magic Constant**.

---

## Magic Constant Formula
For a square of order **n**:

**M = n(n² + 1) / 2**

Example for n = 3:  M = 3 × (9 + 1) / 2 = **15**

---

## Algorithm – The Siamese (Odd-Order) Method
Works only for odd values of n. Follows a diagonal placement strategy:

1. Place **1** at the centre column of the top row.
2. For each subsequent number, move **one cell up** and **one cell right**.
3. If the move goes out of bounds, **wrap to the opposite edge**.
4. If the target cell is already occupied, **drop one row down** from the previous position instead.
5. Repeat until all n² values are placed.

---

## Step-by-Step Procedure
1. Allocate a 2D matrix of size n × n, initialized to zero.
2. Set the starting position to the centre of the top row.
3. Assign values 1 through n² following the placement rules above.
4. Handle wrap-around and collision at each step.
5. Display the completed square along with the magic constant.

---

## Applications
- Logical reasoning tasks in AI
- Matrix-based algorithm design
- Number theory and mathematical puzzles
- Teaching algorithmic thinking and iteration control

---

## Summary
This practical illustrates how structured rules constrain a grid-filling process so that every directional sum remains equal. The Siamese method offers an elegant and efficient approach for constructing odd-order magic squares in Python.
