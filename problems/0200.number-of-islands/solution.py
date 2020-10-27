from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.queue = []
        self.visited = set()
        count = 0

        # iterate through matrix
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                # check if land and not visited
                if grid[y][x] == "1" and (y, x) not in self.visited:
                    # queue node to visit surrounding nodes later
                    self.queue.append((y, x))
                    # increment count
                    count += 1

                # visit surrounding nodes
                while len(self.queue) > 0:
                    yx = self.queue.pop()
                    self.findAdjacent(grid, yx[0], yx[1])

        return count

    def findAdjacent(self, grid, y, x):
        # check within matrix bounds
        if y > len(grid) - 1:
            return
        elif y < 0:
            return
        elif x > len(grid[0]) - 1:
            return
        elif x < 0:
            return

        # check if water or already visited
        if grid[y][x] != "1" or (y, x) in self.visited:
            return

        # mark node as visited
        self.visited.add((y, x))

        # queue surrounding nodes to visit later
        self.queue.append((y + 1, x))
        self.queue.append((y - 1, x))
        self.queue.append((y, x + 1))
        self.queue.append((y, x - 1))


class Recursive:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        # iterate through matrix
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                # check for land
                if grid[y][x] == "1":
                    # visit surrounding lands
                    self.checkAround(grid, y, x)
                    # increment count
                    count += 1

        return count

    def checkAround(self, grid, y, x):
        # check within matrix bounds
        if y > len(grid) - 1:
            return
        elif y < 0:
            return
        elif x > len(grid[0]) - 1:
            return
        elif x < 0:
            return

        # check if water or already visited
        if grid[y][x] != "1":
            return

        # mark node as visited
        grid[y][x] = "2"

        # recursively visit surrounding nodes
        self.checkAround(grid, y + 1, x)
        self.checkAround(grid, y - 1, x)
        self.checkAround(grid, y, x + 1)
        self.checkAround(grid, y, x - 1)