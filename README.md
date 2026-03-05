# data-structures-and-algorithms

## Overview

Data Structures and Algorithms implemented in Python for practice and interview preparation.

This repository is used to:
- Practice algorithmic problem solving
- Learn fundamental data structures
- Master common algorithm patterns
- Track coding interview preparation progress

## Table of Contents

- [Languages](#languages)
- [Learning Roadmap](#learning-roadmap)
- [Project Structure](#project-structure)
- [Running Tests](#running-tests)
- [Complexity Guidelines](#complexity-guidelines)
- [Notes](#notes)
- [Contributing](#contributing)
- [License](#license)

## Languages

Python

## Learning Roadmap

This roadmap outlines the main algorithm patterns and data structures I am studying.  
Topics are organized roughly from **fundamental → advanced**.

**Fundamentals**

- Arrays & Hashing  
- Two Pointers  
- Stack  
- Binary Search  
- Sliding Window  
- Linked List  

**Trees & Tree-based Structures**

- Trees  
- Tries  

**Recursion & Search**

- Backtracking  

**Priority Structures**

- Heap / Priority Queue  

**Graph Algorithms**

- Graphs  
- Advanced Graphs  

**Dynamic Programming**

- 1-D DP  
- 2-D DP  

**Algorithmic Patterns**

- Intervals  
- Greedy  

**Bit & Mathematical Techniques**

- Bit Manipulation  
- Math & Geometry


## Project Structure

```
data-structures-and-algorithms/
│
└── dsa-python/
    │
    ├── 1-d-dp/
    ├── 2-d-dp/
    ├── arrays-and-hashing/
    ├── backtracking/
    ├── binary-search/
    ├── bit-manipulation/
    ├── graphs/
    ├── advanced-graphs/
    ├── greedy/
    ├── heap-priority-queue/
    ├── intervals/
    ├── linked-list/
    ├── math-and-geometry/
    ├── sliding-window/
    ├── stack/
    ├── trees/
    ├── tries/
    └── two-pointers/
```

Each folder includes:
- Problem solution
- Unit tests

## Running Tests

Each problem includes a solution file and a corresponding test file.

To run the tests, execute the test file

##  Complexity Guidelines

The following table summarizes the **typical target time and space complexities**
for the main algorithm patterns used in this repository.

| Topic | Time | Space |
|------|------|------|
| Arrays & Hashing | O(n) | O(n) |
| Two Pointers | O(n) | O(1) |
| Stack | O(n) | O(n) |
| Binary Search | O(log n) | O(1) |
| Sliding Window | O(n) | O(1) |
| Linked List | O(n) | O(1) |
| Trees | O(n) | O(h) |
| Tries | O(n·m) | O(n·m) |
| Backtracking | O(2ⁿ) – O(n!) | O(n) |
| Heap / Priority Queue | O(n log n) | O(n) |
| Graphs | O(V + E) | O(V) |
| Advanced Graphs | O(E log V) | O(V) |
| 1-D Dynamic Programming | O(n) – O(n²) | O(n) |
| 2-D Dynamic Programming | O(n²) – O(n³) | O(n²) |
| Intervals | O(n log n) | O(n) |
| Greedy | O(n) – O(n log n) | O(1) |
| Bit Manipulation | O(1) – O(n) | O(1) |
| Math & Geometry | O(1) – O(n) | O(1) |

**Notation**

- `n` – number of elements  
- `m` – length of string / word  
- `V` – number of vertices  
- `E` – number of edges  
- `h` – height of tree

## Notes

- Solutions focus on **clarity, correctness, and optimal complexity**.
- Most problems include **unit tests** to ensure correctness.
- Folder organization follows common **algorithm patterns** used in coding interviews.

## Contributing

This repository is primarily for personal learning.  
However, suggestions and improvements are always welcome.

## License

This project is licensed under the terms of the **MIT License**.

---

If you find this repository useful, feel free to star it.