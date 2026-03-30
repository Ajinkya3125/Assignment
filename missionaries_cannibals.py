from collections import deque

# Check if state is valid
def is_valid(m_left, c_left, m_right, c_right):
    # Missionaries should not be outnumbered by cannibals
    if (m_left > 0 and m_left < c_left):
        return False
    if (m_right > 0 and m_right < c_right):
        return False
    return True


def missionaries_cannibals():
    # (m_left, c_left, boat_position, path)
    # boat_position: 0 = left, 1 = right
    start = (3, 3, 0, [])
    queue = deque([start])
    visited = set()

    while queue:
        m_left, c_left, boat, path = queue.popleft()

        # Calculate right side
        m_right = 3 - m_left
        c_right = 3 - c_left

        # Goal state
        if m_left == 0 and c_left == 0:
            return path + [(m_left, c_left, boat)]

        if (m_left, c_left, boat) in visited:
            continue

        visited.add((m_left, c_left, boat))

        # Possible moves (m, c)
        moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]

        for m, c in moves:
            if boat == 0:  # Boat on left → move to right
                new_m_left = m_left - m
                new_c_left = c_left - c
                new_boat = 1
            else:          # Boat on right → move to left
                new_m_left = m_left + m
                new_c_left = c_left + c
                new_boat = 0

            new_m_right = 3 - new_m_left
            new_c_right = 3 - new_c_left

            # Check bounds
            if (0 <= new_m_left <= 3 and 0 <= new_c_left <= 3 and
                is_valid(new_m_left, new_c_left, new_m_right, new_c_right)):
                
                queue.append((new_m_left, new_c_left, new_boat,
                              path + [(m_left, c_left, boat)]))

    return None


# Run program
result = missionaries_cannibals()

# Print result
if result:
    print("Solution Steps (M_left, C_left, Boat):")
    for step in result:
        print(step)
else:
    print("No solution found")