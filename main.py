
grid = [[]]


def solver(grid):
    width, height = grid_size(grid)
    counter = 0

    def out_of_bounds(x, y):
        return not (0 <= x < width and 0 <= y < height)

    def dfs(x, y):
        if out_of_bounds(x, y): return
        if grid[y][x] == '0': return
        grid[y][x] = '0'
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)

        
    for y, row in enumerate(grid):
        for x, cell in row:
            if cell == '1':
                counter += 1
                dfs(x, y)
    
    return counter

                
def grid_size(grid):
    width = len(grid[0])
    height = len(grid)
    return (width, height)




