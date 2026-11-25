class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        x, y = 0, 0
        d = 0
        for move in instructions:
            if move == 'G':
                dx, dy = directions[d]
                x += dx
                y += dy
            elif move == 'L':
                d = (d+3) % 4
            elif move == 'R':
                d = (d+1) % 4
        return (x == 0 and y == 0) or d != 0