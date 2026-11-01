
def heuristic(state, goal):
    h = 0

    for i in range(9):
        if state[i] != 0:
            j = goal.index(state[i])

            x1 = i // 3
            y1 = i % 3

            x2 = j // 3
            y2 = j % 3

            h = h + abs(x1 - x2) + abs(y1 - y2)

    return h


def get_moves(state):
    result = []

    pos = state.index(0)

    moves = [-3, 3, -1, 1]

    for move in moves:
        new_pos = pos + move

        if 0 <= new_pos < 9:

            if abs(pos // 3 - new_pos // 3) + abs(pos % 3 - new_pos % 3) == 1:

                new = state.copy()

                new[pos] = new[new_pos]
                new[new_pos] = 0

                result.append(new)

    return result


def astar(start, goal):

    open_list = [(start, 0, [start])]
    visited = []

    while open_list:

        best = 0

        for i in range(len(open_list)):
            f = open_list[i][1] + heuristic(open_list[i][0], goal)

            if f < open_list[best][1] + heuristic(open_list[best][0], goal):
                best = i

        state, cost, path = open_list.pop(best)

        if state == goal:
            print("Solution Found")

            for s in path:
                print(s[0:3])
                print(s[3:6])
                print(s[6:9])
                print()

            return

        if state not in visited:

            visited.append(state)

            for new_state in get_moves(state):

                if new_state not in visited:
                    open_list.append((new_state, cost + 1, path + [new_state]))

    print("No Solution Found")


start = [1, 2, 3,
         4, 0, 6,
         7, 5, 8]

goal = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]

astar(start, goal)

