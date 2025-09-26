import time

def island_matrix(grid,number):
    rows = len(grid)
    cols = len(grid[0])
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1 and row < rows-1 and col < cols-1:
                if dfc(grid,row + 1, col):
                    number+=1
                if dfc(grid,row, col + 1):
                    number+=1
                if dfc(grid,row + 1, col + 1):
                    number+=1
    return number


def dfc(grid, row, col):
    if grid[row][col] == 1:
        return True
    else:
        return False

def numConnectedComponents(grid: list[list[int]]) -> int:
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]

    def dfs(r, c):
        # check boundaries and visited
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if visited[r][c] or grid[r][c] == 0:
            return

        visited[r][c] = True
        # explore neighbors (4-directional)
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and not visited[r][c]:
                dfs(r, c)
                count += 1

    return count

grid = [
  [1, 1, 0, 0],
  [1, 0, 0, 1],
  [0, 0, 1, 1],
  [0, 0, 0, 0]
]
number = 0
number2 = 0

initial_time = time.time()
print(island_matrix(grid, number))
ending_time = time.time()

initial_2 = time.time()
print(numConnectedComponents(grid))
ending_2 = time.time()

print(f"Fast timer: {ending_time - initial_time}"
      f"slow timer: {ending_2 - initial_2}")