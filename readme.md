Here is a detailed README.md for the astar.py and ucs.py code files:

# Pancake Puzzle Solver

This project contains implementations of A* search and Uniform Cost Search (UCS) to solve pancake sorting problems.

## Contents

- `astar.py`: Implements A* search to find an optimal solution to a defined pancake puzzle problem
- `ucs.py`: Implements uniform cost search to find a solution to the same pancake puzzle 

## The Pancake Puzzle

The "pancake puzzle" involves sorting a stack of differently sized pancakes using only spatula flips. A spatula can go under any pancake and flip all pancakes above it. The goal is to sort the pancakes from smallest on top to largest on bottom using the minimum number of flips.

For example, given the stack [3, 1, 2], a possible solution is:

1. Flip top 2 pancakes: [1, 3, 2] 
2. Flip all 3 pancakes: [2, 1, 3] -> Solved!

This required 2 flips to solve.

The puzzle becomes more challenging as the number of pancakes increases.

## Usage

The `PancakePuzzle` class represents a state in the search space. It contains:

- `pancakes` - list representing stack order 
- Methods to check if state is goal, generate successor states, and compute heuristic

The search algorithms are implemented as standalone functions:

- `a_star_search()` - performs A* search using a priority queue ordered by f(n) = g(n) + h(n)
- `uniform_cost_search()` - performs uniform cost search using a priority queue ordered by path cost g(n)

Example usage:

```python
start_state = PancakePuzzle([3, 1, 2]) 

came_from = a_star_search(start_state)
solution_path = reconstruct_solution(came_from, start_state)

print(solution_path)
# [PancakePuzzle([2, 1, 3]), PancakePuzzle([1, 3, 2]), PancakePuzzle([3, 1, 2])]
```

The output solution path shows the sequence of states leading to the solved state, requiring a minimum of 2 flips.

## Algorithm Details

**A* Search** uses both the path cost g(n) and a heuristic estimate of remaining cost h(n) to focus search efforts on the most promising nodes. The heuristic used here counts the number of disjoint pairs in the stack, which estimates how many flips are needed to sort it.

**Uniform Cost Search** expands nodes in order of path cost g(n). It guarantees an optimal solution but is less informed than A*.

Both algorithms use data structures like `came_from` to reconstruct the final solution path after reaching the goal state.

