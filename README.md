# NPDA Simulation for Language wwr

## **Overview**
This repository provides a Python-based simulation of a Non-Deterministic Pushdown Automaton (NPDA) that accepts the language **L = { wwr | w ∈ {a, b}\***. This language consists of strings that are a word followed by its reverse (e.g., `"abba"`, `"aabbaa"`), which are context-free but **not** deterministic context-free.

## **Why NPDA?**
Deterministic Pushdown Automata (DPDA) are limited in expressive power compared to NPDA. The language **wwr** is a classic example of a language that **cannot be recognized by any DPDA**, but can be accepted by an NPDA.

## **Python Simulation**
The NPDA is implemented in Python using recursive backtracking to simulate non-determinism. The automaton:

- Pushes symbols from the first half of the input onto a stack
- Non-deterministically guesses the midpoint
- Then matches and pops symbols while reading the second half in reverse
