"""
Given an occupancy matrix. Search if an specific value x is inside the matrix.
"""
import time

#FIRST OPTION
def search_occupancy(occupancy,target):
    for x in range(len(occupancy)):
        for y in range(len(grid[x])):
            if occupancy[x][y] == target:
                return True
    return False

#SECOND OPTION
def search_matrix(occupancy,target):
    if not occupancy:
        return False
    else:
        rows = len(occupancy)
        cols = len(occupancy[0])

        row = 0
        col = cols-1

        while row<rows and col >= 0:
            if occupancy[row][col] == target:
                return True
            elif occupancy[row][col] > target:
                col-=1
            else:
                row+=1
        return False



grid = [
  [1, 4, 7, 11],
  [2, 5, 8, 12],
  [3, 6, 9, 16],
  [10, 13, 14, 17]
]

initial_time = time.time()
print(search_occupancy(grid, 5))
ending_time = time.time()

initial_2 = time.time()
print(search_matrix(grid, 5))
ending_2 = time.time()

print(f"Slow timer: {ending_time - initial_time}"
      f"Fast timer: {ending_2 - initial_2}")