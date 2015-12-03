def find_start(lab):  # findiding position start
    for a, s in enumerate(lab):  # pridava indexi
        if 2 in s:
            return (a, s.index(2))


def find_end(lab):  # finding position goal
    for a, s in enumerate(lab):
        if 1 in s:
            return (a, s.index(1))


def labtograph(labyrint, enemy, my_bot):
    height = len(labyrint)
    width = len(labyrint[0]) if height else 0
    graph = {(i, j): [] for i in range(height) for j in range(width)
             if labyrint[i][j] != 3 and ((i, j) != (enemy[0], enemy[-1]))
    }  # paste key and [] if cell is "free" (labyrint[i][j])

    for row, col in graph.keys():  # finding neighbors around each point in the graph
        if row < (height - 1) and (labyrint[row + 1][col] == 0 or labyrint[row + 1][col] == 1 or (row + 1, col) ==
            (my_bot[0], my_bot[-1]) ):
            graph[(row, col)].append(("S", (row + 1, col)))  # ptam se vyskove - prohledam jih
            graph[(row + 1, col)].append(("N", (row, col)))  # davam jiznimu sousedu predchozi vrchol od kteryho ptam
        if col < (width - 1) and (labyrint[row][col + 1] == 0 or labyrint[row][col + 1] == 1 or (row, col + 1) == (
                my_bot[0], my_bot[-1])):
            graph[(row, col)].append(("E", (row, col + 1)))
            graph[(row, col + 1)].append(("W", (row, col)))
    return graph


# algorithm wave
def wave(labyrint, location, start, enemy):
    goal = find_end(labyrint)
    queue = [("", start)]
    graph = labtograph(labyrint, enemy, my_bot=start)
    visited = set()
    print(start)
    print(goal)
    while queue:
        path, current = queue.pop(0)
        if current == goal:
            print(path)
            move = action(path, location)
            return move
        if current in visited:
            continue
        visited.add(current)
        for direction, neighbour in graph[current]:
            queue.append((path + direction, neighbour))
    return 'No way!'


def action(path, location):
    loc = {0: "N", 1: "E", 2: "S", 3: "W"}
    ori = loc.get(location)
    moves = []
    path = list(path)
    for p in path:
        if p == ori:
            moves.append("step")
        else:
            if ori == "N":  # divam se nahoru
                if p == "W":
                    ori = "W"
                    moves.append("turn_left")
                elif p == "E":
                    ori = "E"
                    moves.append("turn_right")
                elif p == "S":
                    ori = "S"
                    moves.append("turn_left")
                    moves.append("turn_left")

            elif ori == "E":  # divam se doprava
                if p == "W":
                    ori = "W"
                    moves.append("turn_right")
                    moves.append("turn_right")
                elif p == "N":
                    ori = "N"
                    moves.append("turn_left")
                elif p == "S":
                    ori = "S"
                    moves.append("turn_right")


            elif ori == "S":  # divam se dolu
                if p == "W":
                    ori = "W"
                    moves.append("turn_right")
                elif p == "E":
                    ori = "E"
                    moves.append("turn_left")
                elif p == "N":
                    ori = "N"
                    moves.append("turn_left")
                    moves.append("turn_left")

            elif ori == "W":  # divam se doleva
                if p == "N":
                    ori = "N"
                    moves.append("turn_right")
                elif p == "E":
                    ori = "E"
                    moves.append("turn_right")
                    moves.append("turn_right")
                elif p == "S":
                    ori = "S"
                    moves.append("turn_left")

            moves.append("step")
    return moves



