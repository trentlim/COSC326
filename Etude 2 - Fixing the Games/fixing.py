import numpy as np


def solve(grid, row):
    duplicates, duplicate_indexes = find_duplicates(grid, row)
    new_grid = []

    if len(duplicates) != 1:
        if row == len(grid) - 1:
            grid[row][np.where(grid[row] == "")] = "_"
            return [grid]
        else:
            return new_grid

    for index in duplicate_indexes:
        for i in range(2):
            col = index[0][i]
            a = grid.copy()

            if "_" in a[:, col]:
                continue

            a[row:, col] = np.roll(a[row:, col], 1, axis=0)
            a[row][col] = "_"
            new_grid.append(a)

        return new_grid


def find_duplicates(grid, row):
    current_line = grid[row].tolist()
    duplicates = []
    [duplicates.append(i) for i in current_line if current_line.count(i) == 2 and i not in duplicates]

    duplicate_indexes = []
    for i in duplicates:
        duplicate_indexes.append(np.where(grid[row] == i))
    

    return duplicates, duplicate_indexes


if __name__ == "__main__":
    collapsed_results = []
    p = 0

    while True:
        try:
            line = input().strip()
            line = line.split(" ")
        except EOFError:
            break

        collapsed_results.append(line)

    # Number of players
    p = len(collapsed_results[0])

    # Check formatting of input
    if not all(len(i) == p for i in collapsed_results):
        print("Bad format")
        exit()
    else:
        for i in collapsed_results:
            for j in i:
                j = int(j)
                if j < 1 or j > (p - 1):
                    print("Bad values")
                    exit()

    collapsed_results.append([""] * p)
    collapsed_results = np.array(collapsed_results)

    results = [collapsed_results]

    for row in range(0, p):
        new_results = []
        for result in results:
            solved = solve(result, row)
            if solved:
                for solution in solved:
                    new_results.append(solution)

        results = new_results

    if not results:
        print("Inconsistent results")
        exit()

    # Print results
    for result in results:
        for row in result:
            print(" ".join(row))
        print()

    # Find number of different results
    diff_results = []
    for result in results:
        sorted_result = result[np.argsort(result[:, len(result) - 1])]
        if not any(np.array_equal(sorted_result, i) for i in diff_results):
            diff_results.append(sorted_result)

    print(f"Different results: {len(diff_results)}")
