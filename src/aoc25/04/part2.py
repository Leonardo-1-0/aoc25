grid = [[col for col in row.strip()] for row in open(0).readlines()]


def print_grid(grid: list[list[str]]) -> None:
    print("\n".join("".join(char) for char in grid))


def count_neighbors(grid: list[list[str]], row: int, col: int) -> int:
    counter = 0
    for i in range(row - 1, row + 2):
        if i < 0 or i > len(grid) - 1:
            continue
        for j in range(col - 1, col + 2):
            if j < 0 or j > len(grid[0]) - 1:
                continue
            if i == row and j == col:
                continue
            if grid[i][j] == "@":
                counter += 1
    return counter


start = True
total = 0
remove = []
while len(remove) > 0 or start:
    remove.clear()
    start = False
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] != "@":
                continue
            if count_neighbors(grid, row, col) < 4:
                total += 1
                remove.append((row, col))

    for i, j in remove:
        grid[i][j] = "."

print(total)
