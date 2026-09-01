
def numIslands( grid):
    m = len(grid)
    n = len(grid[0])

    parent = list(range(m * n))
    count = 0

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)

        if root_x == root_y:
            return False

        parent[root_y] = root_x
        return True

    for i in range(m):
        for j in range(n):

            if grid[i][j] == '0':
                continue

            # 当前是一个新的岛
            count += 1

            current = i * n + j

            # 看上面
            if i > 0 and grid[i - 1][j] == '1':
                up = (i - 1) * n + j

                if union(current, up):
                    count -= 1

            # 看左边
            if j > 0 and grid[i][j - 1] == '1':
                left = i * n + (j - 1)

                if union(current, left):
                    count -= 1

    return count

res= numIslands([
  ['1','1','1','1','0'],
  ['1','1','0','1','0'],
  ['1','1','0','0','0'],
  ['0','0','0','0','0']
])

print(res)


