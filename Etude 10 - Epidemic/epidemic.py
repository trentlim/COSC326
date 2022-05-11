# Prints grid in a readable format
def print_grid(grid):
    for row in grid:
        row = "".join(row)
        print(row)


# Returns final state of a given universe
def solve(grid):
    rows = len(grid)
    cols = len(grid[0])

    while True:
        got_sick = 0
        for x, row in enumerate(grid):
            for y, col in enumerate(row):
                if col == ".":
                    sick_neighbors = 0

                    # Check cell above
                    if x > 0:
                        if grid[x - 1][y] == "S":
                            sick_neighbors += 1

                    # Check cell to the right
                    if y < cols - 1:
                        if grid[x][y + 1] == "S":
                            sick_neighbors += 1

                    # Check cell below
                    if x < rows - 1:
                        if grid[x + 1][y] == "S":
                            sick_neighbors += 1

                    # Check cell to the left
                    if y > 0:
                        if grid[x][y - 1] == "S":
                            sick_neighbors += 1

                    # print(sick_neighbors)
                    if sick_neighbors >= 2:
                        grid[x][y] = "S"
                        got_sick += 1

        if got_sick == 0:
            break

    return grid


# Reads input file and prints grid
if __name__ == "__main__":
    grids = []

    grid = []
    while True:
        try:
            line = input()
        except EOFError:
            grids.append(grid)
            break

        if line == "":
            grids.append(grid)
            grid = []
        else:
            line = list(line)
            grid.append(line)

    for grid in grids:
        print_grid(solve(grid))
        print()
