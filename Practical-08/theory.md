# Theory – Semantic Network for Knowledge Representation

## Overview
A **Semantic Network** is a graphical knowledge representation technique where knowledge is stored as a directed graph:

- **Nodes** → Concepts or objects (e.g., Animal, Bird, Dog)
- **Edges** → Named relationships between concepts (e.g., ISA, HAS-A, CAN)

It is closely related to **Predicate Logic**, where each relationship in the graph maps to a first-order predicate.

---

## Relationship to Predicate Logic

| Semantic Relation | Predicate Form |
|---|---|
| Dog is an Animal | `isa(dog, animal)` |
| Bird can Fly | `can(bird, fly)` |
| Dog has Tail | `has(dog, tail)` |
| Animal has Cells | `has(animal, cells)` |

**Inheritance Rule (Predicate Logic):**
```
If isa(X, Y) and has(Y, Z)  →  then has(X, Z)
```

---

## Common Relationship Types

| Relation | Meaning | Example |
|---|---|---|
| **ISA** | Inheritance / "is a kind of" | Sparrow ISA Bird |
| **HAS-A** | Property ownership | Animal HAS cells |
| **CAN** | Ability | Bird CAN fly |

---

## Example Semantic Network
**Nodes:** Animal, Bird, Dog, Sparrow

**Relationships:**
- Sparrow **ISA** Bird
- Bird **ISA** Animal
- Dog **ISA** Animal
- Animal **HAS** cells
- Bird **CAN** fly
- Dog **CAN** bark

---

## Inheritance in Semantic Networks
Inheritance allows a child concept to automatically acquire properties of its parent:

- Since **Sparrow ISA Bird** and **Bird ISA Animal**, Sparrow inherits the property `has(cells)` from Animal without it being explicitly stated.
- This avoids redundancy and mirrors how humans categorize knowledge.

---

## Algorithm – Step-by-Step
1. Define ISA relationships (hierarchy) in a dictionary.
2. Define CAN-DO abilities and HAS-PROPERTY facts.
3. To query a property for a concept, check the concept directly.
4. If not found, recursively check its parent (via ISA) until the root is reached.
5. Return `True` if the property is found anywhere in the hierarchy, else `False`.

---

## Applications
- Natural language processing (NLP)
- Expert systems and knowledge bases
- Ontology design (e.g., OWL, RDF in the Semantic Web)
- AI-based question answering systems

---

## Summary
Semantic networks provide an intuitive, graph-based way to represent and query structured knowledge. Combined with **inheritance**, they allow a system to derive new facts without explicitly storing all information — a core principle in AI knowledge representation.
