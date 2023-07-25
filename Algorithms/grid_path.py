max = 1000

dpCost = {}    #store cost from particular row,col pair

def recursiveSearch(grid, row, col1, col2, dpCost):
    '''

    :param grid:
    :param row:
    :param col1:
    :param col2:
    :param dpCost: store the min cost of adjacent cell pair
    :return: minimum cost from particular adjacent pair of cell to any first row cell pairs


    This is a recursive call we start from the last row last two cols
    and work upward to row 0 and any possible columns

    so for pair (1,2)(1,3) we will recurse to (0,2)(0,3) and (0,1)(0,2) and (0,3)(0, outofbound) for 2x4 grid

    if cell pair already visited retrieve from dpCost

    we return the minimum cost

    '''

    key = f'{row},{col1},{col2}'
    if (key in dpCost):

        return dpCost[key]

    if (col1 < 0 or col2 < 0):

        return max
    if(col2 > len(grid[0])-1 or col1 > len(grid[0])-1):
        return max
    if (row == 0):
        return grid[row][col1] + grid[row][col2]
    print(f'recursing')
    cost = min(recursiveSearch(grid, row - 1, col1, col2, dpCost) + grid[row][col1] + grid[row][col2],
           min(recursiveSearch(grid, row - 1, col1 - 1, col1, dpCost) + grid[row][col1] + grid[row][col2],
               recursiveSearch(grid, row - 1, col2, col2 + 1,dpCost) + grid[row][col1] + grid[row][col2]))

    dpCost[key] = cost
    return dpCost[key]

ROWS = 4
COLS = 4

grid  = [[0 for col in range(COLS)] for row in range(ROWS)]  # initialize a grid of any size row, col


for i in range(ROWS):
    print(grid[i])


# ask user to enter the cost of each cell in the grid
for row in range(len(grid)):
    for col in range(len(grid[0])):
        grid[row][col] = int(input(f"give a cost for each cell ({row},{col}):"))

for i in range(ROWS):
    print(grid[i])

# (0,0) (0,1)   and (0,1) (0,2) and (0,2) (0,3)

i=len(grid[0])-2
j=len(grid[0])-1
row = len(grid)-1



costGrid = []   #store the mini cost from each adjacent cell pair

# loop through each adjacent pair from the last row aka (1,2)(1,3)  to (1,0)(1,) for row 2 x col 4 grid
while i > -1 and j > 0:
   print(f'({row},{i}) and ( {row}, {j})')



   cost = recursiveSearch(grid, row, i, j, dpCost) # cal cost using recursion to any possible path
   print(cost)
   costGrid.append(cost)
   i -= 1
   j -= 1


print(dpCost)
print(f'cost from each pair of cells in grid {costGrid}')

print(f'minimum cost is min of costGrid = {min(costGrid)}')





