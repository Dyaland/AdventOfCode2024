class Coord:
    def __init__(self, y, x, char):
        self.y, self.x = y, x
        self.value = char
        self.is_antinode = False


def set_antinodes(current, other):
    y_diff = other.y - current.y
    x_diff = other.x - current.x

    ay = current.y - y_diff
    ax = current.x - x_diff
    if ay >= 0 and 0 <= ax < len(base_map[0]):
        base_map[ay][ax].is_antinode = True

    by = other.y + y_diff
    bx = other.x + x_diff
    if by < len(base_map) and 0 <= bx < len(base_map[0]):
        base_map[by][bx].is_antinode = True


def solution():

    for type in types_dict:
        for current in types_dict[type]:
            for other in types_dict[type]:
                if current.y <= other.y and current is not other:
                    set_antinodes(current, other)
    return sum([coord.is_antinode for row in base_map for coord in row])


if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        content = f.read().strip()

    base_map = [[Coord(y, x, char) for x, char in enumerate(row)] for y, row in enumerate(content.split('\n'))]

    all_coords = [coord for row in base_map for coord in row]

    types_dict = {}
    for coord in all_coords:
        if coord.value != '.':
                types_dict.setdefault(coord.value, []).append(coord)

    print(solution())
