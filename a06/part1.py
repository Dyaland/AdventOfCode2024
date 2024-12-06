class Guard:
    def __init__(self):
        self.current_dir = '^'
        self.directions = ['^', '<', 'v', '>']
        self.changes = {
            '^': [-1, 0],
            '<': [0, -1],
            'v': [+1, 0],
            '>': [0, +1]
        }
        for i, row in enumerate(base_map):
            if self.current_dir in row:
                self.coordinates = [i, row.index(self.current_dir)]
        self.x_coords = set()
        self.x_coords.add(tuple(self.coordinates))

    def move(self):
        y, x =  self.coordinates
        a, b = self.changes[self.current_dir]
        if base_map[y+a][x+b] == '#':
            self.current_dir = self.directions[self.directions.index(self.current_dir) - 1]
            a, b = self.changes[self.current_dir]
        self.coordinates = [y+a, x+b]
        self.x_coords.add(tuple(self.coordinates))
        return

    @property
    def exited(self):
        if self.coordinates[0] in [0, len(base_map) - 1] or self.coordinates[1] in [0, len(base_map[0]) - 1]:
            return True
        else:
            return False


def solution():
    guard = Guard()
    while not guard.exited:
        guard.move()
    count = len(guard.x_coords)
    return count


if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        base_map = [list(row.strip()) for row in f.readlines() if row.strip()]

    print(solution())
