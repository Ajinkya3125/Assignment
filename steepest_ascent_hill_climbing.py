##steepest ascent hill climbing

def heuristic(state, goal):
    """Count number of blocks in correct position"""
    h = 0
    for i in range(len(state)):
        if state[i] == goal[i]:
            h += 1
    return h


def steepest_ascent_hill_climbing(initial, goal):
    current = initial
    print("Initial State:", current)

    while True:
        current_h = heuristic(current, goal)
        neighbors = []

        # Generate neighbors by swapping adjacent blocks
        for i in range(len(current) - 1):
            new_state = current[:]
            new_state[i], new_state[i+1] = new_state[i+1], new_state[i]
            neighbors.append(new_state)

        # Evaluate all neighbors
        scored_neighbors = []
        for state in neighbors:
            h = heuristic(state, goal)
            scored_neighbors.append((h, state))

        # Sort neighbors based on heuristic (descending)
        scored_neighbors.sort(reverse=True)

        best_h, best_state = scored_neighbors[0]

        # If no improvement, stop
        if best_h <= current_h:
            break

        current = best_state
        print("Next State:", current)

    return current


# Example
initial_state = ['B', 'A', 'D', 'C']
goal_state = ['A', 'B', 'C', 'D']

result = steepest_ascent_hill_climbing(initial_state, goal_state)

print("Final State:", result)
if result == goal_state:
    print("Goal Reached!")
else:
    print("Stuck at Local Optimum")
