def same_region(y:int, x:int, region:str):
    if all((0 <= y < height,
            0 <= x < width)):
        return grid[y][x] == region


def find_area(y:int, x:int, region:str):

    if not same_region(y, x, region):
        return 0, 1
    if visited[y][x]:
        return 0, 0

    visited[y][x] = True
    area, perimeter = 1, 0

    for change in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_area, new_perimeter = find_area(y + change[0], x + change[1], region)
        area += new_area
        perimeter += new_perimeter
    return area, perimeter


def solution():

    regions_list = []
    for y, x in ((y, x) for y in range(height) for x in range(width)):
        if not visited[y][x]:
            regions_list.append(find_area(y, x, grid[y][x]))
    return sum(area * perimeter for area, perimeter in regions_list)


with open('input.txt', 'r') as f:
    grid = [[char for char in row.strip()] for row in f.readlines()]
    height, width = len(grid), len(grid[0])
    visited = [[False] * width for _ in range(height)]

print(solution())