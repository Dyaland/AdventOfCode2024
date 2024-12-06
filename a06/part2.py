class Guard:
    def __init__(self, input_map):
        self.map = input_map
        self.current_dir = '^'
        self.directions = ['^', '<', 'v', '>']
        self.changes = {
            '^': [-1, 0],
            '<': [0, -1],
            'v': [+1, 0],
            '>': [0, +1]
        }
        for i, row in enumerate(self.map):
            if self.current_dir in row:
                self.coordinates = [i, row.index(self.current_dir)]
                self.starting_pos = self.coordinates[:]
        self.x_coords = set()
        self.x_coords.add(tuple(self.starting_pos))
        self.loop_check_dict = {'placeholder': 0}

    def move(self):
        y, x =  self.coordinates
        a, b = self.changes[self.current_dir]
        while self.map[y+a][x+b] in ['#', 'O']:
            if not str(self.coordinates) in self.loop_check_dict.keys():
                self.loop_check_dict[str(self.coordinates)] = 0
            self.loop_check_dict[str(self.coordinates)] += 1
            self.current_dir = self.directions[self.directions.index(self.current_dir) - 1]
            a, b = self.changes[self.current_dir]
        self.coordinates = [y+a, x+b]
        self.x_coords.add(tuple(self.coordinates))

    @property
    def looped(self):
        if max(self.loop_check_dict.values()) > 2:
            return True

    @property
    def exited(self):
        if self.coordinates[0] in [0, len(self.map) - 1] or self.coordinates[1] in [0, len(self.map[0]) - 1]:
            return True


def solution():
    # Create set of unique path coords without the starting position
    guard = Guard(base_map)
    while not guard.exited:
        guard.move()
    guard.x_coords.remove(tuple(guard.starting_pos))
    path_coords = [coords for coords in guard.x_coords]
    count = 0
    # Check for loops at each possible path coordinate
    for coords in path_coords:
        blocked_map = [row[:] for row in base_map]
        blocked_map[coords[0]][coords[1]] = 'O'
        guard = Guard(blocked_map)
        # Move until exited or a loop is detected
        while not guard.exited:
            guard.move()
            if guard.looped:
                count += 1
                break
    return count


if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        base_map = [list(row.strip()) for row in f.readlines() if row.strip()]

    print(solution())
