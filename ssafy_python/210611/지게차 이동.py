
def dfs(height, width, array, memo, x, y):

    if x+1 < height:
        if memo[x+1][y] != 0:
            memo[x+1][y] = memo[x+1][y] if memo[x+1][y] <= memo[x][y] + array[x+1][y] else memo[x][y] + array[x+1][y]
    if array[x+1][y] <= array[x][y+1]:
        if x == height - 1 and y == width - 1:
            if memo[x][y] == 0:
                memo[x][y] = array[x][y]


h, w = map(int, input().split())
mem = [0 * w for _ in range(h)]
arr = [list(map(int, input().split()))]
