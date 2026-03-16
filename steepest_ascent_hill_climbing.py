import copy

goal = ['A','B','C', 'D']

# Heuristic function
def heuristic(state):
    score = 0
    for stack in state:
        for i in range(len(stack)):
            if i < len(goal) and stack[i] == goal[i]:
                score += 1
    return score


# Generate successors
def successors(state):
    succ = []

    for i in range(len(state)):
        if len(state[i]) == 0:
            continue

        for j in range(len(state)):
            if i != j:
                new_state = copy.deepcopy(state)

                block = new_state[i].pop()
                new_state[j].append(block)

                succ.append(new_state)

    return succ


def steepest_ascent(initial):

    current = initial

    while True:

        current_h = heuristic(current)
        best_state = current
        best_h = current_h

        print("Current State:", current, "h =", current_h)

        for s in successors(current):

            h = heuristic(s)

            if h > best_h:
                best_state = s
                best_h = h

        if best_h <= current_h:
            print("No better successor found (Local Maximum)")
            break

        current = best_state

        if heuristic(current) == len(goal):
            print("Goal Reached:", current)
            break


initial = [['D','C','B'],['A']]

steepest_ascent(initial)