# Theory – Prolog Family Relationship Program

## Overview
**Prolog** (Programming in Logic) is a declarative logic programming language rooted in **First-Order Predicate Logic**. Unlike procedural languages (C, Python) that describe *how* to solve a problem, Prolog declares *what is true* and lets its built-in inference engine figure out the rest.

---

## Structure of a Prolog Program
A Prolog program consists of three building blocks:

| Building Block | Description | Example |
|---|---|---|
| **Facts** | Unconditionally true statements | `parent(rajesh, priya).` |
| **Rules** | Conditional (if–then) statements | `father(X,Y) :- parent(X,Y), male(X).` |
| **Queries** | Questions posed to the system | `?- father(rajesh, priya).` |

---

## Core Concepts

### Unification
Prolog matches terms by **unification**. When a query is made, Prolog binds variables to values that make the query true.

Example:
```prolog
?- parent(rajesh, X).
X = priya ;
X = arjun.
```

### Backtracking
When a goal fails or the user requests another answer (by pressing `;`), Prolog **backtracks** — it undoes the last variable binding and tries the next alternative. This automatic search is fundamental to Prolog's power.

### Recursion
Recursive rules allow reasoning over chains of any depth. The `ancestor` rule handles multi-generation ancestry:

```prolog
ancestor(X, Y) :- parent(X, Y).             % Base case
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y). % Recursive case
```

---

## Family Relationship Predicates

| Predicate | Meaning |
|---|---|
| `parent(X, Y)` | X is a parent of Y |
| `male(X)` / `female(X)` | Gender facts |
| `father(X, Y)` | X is the father of Y |
| `mother(X, Y)` | X is the mother of Y |
| `sibling(X, Y)` | X and Y share a common parent |
| `grandparent(X, Y)` | X is a grandparent of Y |
| `ancestor(X, Y)` | X is an ancestor of Y (any depth) |

---

## Important Prolog Operators

| Operator | Meaning |
|---|---|
| `:-` | If (rule neck) |
| `,` | AND (conjunction) |
| `;` | OR (disjunction) |
| `=` | Unification |
| `\=` | Not unifiable |
| `is` | Arithmetic evaluation |
| `\+` | Negation as failure |

---

## Sample Queries & Expected Output
```prolog
?- father(rajesh, arjun).       % true
?- mother(X, ananya).           % X = priya
?- sibling(priya, arjun).       % true
?- grandparent(rajesh, vivaan). % true
?- ancestor(rajesh, X).         % X = priya ; arjun ; ananya ; vivaan
```

---

## Summary
This practical demonstrates how Prolog represents structured knowledge as **facts** and derives new knowledge through **rules**. The family relationship model illustrates core AI concepts — knowledge representation, logical inference, unification, and backtracking — in a clear, easy-to-visualise scenario.
