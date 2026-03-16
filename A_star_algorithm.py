import heapq

goal = [[1,2,3],
        [4,5,6],
        [7,8,0]]

# Heuristic: count misplaced tiles
def heuristic(state):
    h = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                h += 1
    return h


# Find blank position
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i,j


# Generate neighbors
def neighbors(state):
    x,y = find_blank(state)
    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    result = []

    for dx,dy in moves:
        nx,ny = x+dx,y+dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            result.append(new_state)

    return result


def a_star(start):

    open_list = []
    closed = []

    g = 0
    h = heuristic(start)
    f = g + h

    heapq.heappush(open_list,(f,g,start))

    while open_list:

        f,g,current = heapq.heappop(open_list)

        print("\nCurrent State (g={}, h={}, f={}):".format(g,heuristic(current),f))
        for row in current:
            print(row)

        if current == goal:
            print("\nGoal Reached!")
            return

        closed.append(current)

        for n in neighbors(current):

            if n in closed:
                continue

            g_new = g + 1
            h_new = heuristic(n)
            f_new = g_new + h_new

            heapq.heappush(open_list,(f_new,g_new,n))


# Initial state from your notebook
initial = [[1,2,3],
        [0,4,5],
        [7,8,6]]

a_star(initial)