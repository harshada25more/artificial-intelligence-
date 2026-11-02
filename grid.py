grid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]

position = [0, 0]
goal = [2, 2]

def move_agent():
    while position != goal:
        x, y = position

        if y < 2 and grid[x][y + 1] == 0:
            position[1] += 1
            print("Move Right")

        elif x < 2 and grid[x + 1][y] == 0:
            position[0] += 1
            print("Move Down")

        else:
            print("Path Blocked")
            break

    print("Final Position:", position)

move_agent()