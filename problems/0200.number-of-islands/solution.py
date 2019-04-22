from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.queue = []
        self.visited = set()
        count = 0

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if self.check_land(grid, y, x) == True:
                    count += 1

                while len(self.queue) > 0:
                    xy = self.queue.pop(0)
                    self.find_adjacent(grid, xy[0], xy[1])

        return count

    def find_adjacent(self, grid: List[List[str]], y: int, x: int):
        self.check_land(grid, y, x + 1)
        self.check_land(grid, y, x - 1)
        self.check_land(grid, y + 1, x)
        self.check_land(grid, y - 1, x)

        return

    def check_land(self, grid: List[List[str]], y: int, x: int) -> bool:
        if y >= len(grid) or y < 0:
            return False
        if x >= len(grid[0]) or x < 0:
            return False
        if (y, x) in self.visited:
            return False
        if grid[y][x] == "0":
            return False

        yx = (y, x)
        self.visited.add(yx)
        self.queue.append(yx)

        return True


class Recursive:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        count = 0

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1":
                    self.find_adjacent(grid, y, x)
                    count += 1

        return count

    def find_adjacent(self, grid: List[List[str]], y: int, x: int):
        if y >= len(grid) or y < 0:
            return
        if x >= len(grid[y]) or x < 0:
            return
        if grid[y][x] != "1":
            return

        grid[y][x] = "#"
        self.find_adjacent(grid, y, x + 1)
        self.find_adjacent(grid, y, x - 1)
        self.find_adjacent(grid, y + 1, x)
        self.find_adjacent(grid, y - 1, x)
