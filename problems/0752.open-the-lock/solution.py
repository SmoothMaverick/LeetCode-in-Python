from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        self.queue = []
        self.visited = set()

        step = 0
        start = "0000"
        self.queue.append((start, step))

        while len(self.queue) > 0:
            pos, step = self.queue.pop(0)

            if pos == target:
                return step

            if pos in self.visited or pos in deadends:
                continue

            self.visited.add(pos)
            self.findTarget(pos, step)

        return -1

    def findTarget(self, pos, step):
        for i in range(4):
            self.turnWheel(pos, step, i, 1)
            self.turnWheel(pos, step, i, -1)

    def turnWheel(self, pos, step, index, move):
        num = (int(pos[index]) + move) % 10
        next_pos = pos[:index] + str(num) + pos[index + 1 :]

        self.queue.append((next_pos, step + 1))
