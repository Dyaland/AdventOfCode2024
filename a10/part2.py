def solution():

    def find_paths(value, y, x):
        nonlocal total_score
        
        if value == 9:
            total_score += 1
            return
        
        if y < len(hike_map) - 1 and hike_map[y + 1][x] - value == 1:
            find_paths(value + 1, y + 1, x)
        if x < len(hike_map[0]) - 1 and hike_map[y][x + 1] - value == 1:
            find_paths(value + 1, y, x + 1)
        if y > 0 and hike_map[y - 1][x] - value == 1:
            find_paths(value + 1, y - 1, x)
        if x > 0 and hike_map[y][x - 1] - value == 1:
            find_paths(value + 1, y, x - 1)

    total_score = 0

    trailheads = [(y, x) for y, line in enumerate(hike_map) for x, value in enumerate(line) if value == 0]
    for coords in trailheads:
        find_paths(0, coords[0], coords[1])
    return total_score


if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        hike_map = [[int(value) for value in line.strip()] for line in f.readlines()]

    print(solution())
