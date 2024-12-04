def solution():

    xmas = 0
    for y in range(height):
        for x in range(width):
            xmas += find_xmas(y, x)
    return xmas


def find_xmas(y, x):
    
    matching = ['XMAS', 'SAMX']
    count = 0

    horizontal = content[y][x:x+4]
    if horizontal in matching:
        count += 1

    if y <= height - 4:
        vertical = ''.join([content[vert][x] for vert in range(y, y + 4)])
        if vertical in matching:
            count += 1

    if y <= height - 4 and x <= width -4:
        diagonal_r = ''.join([content[i][j] for i, j in zip(range(y, y + 4), range(x, x + 4))])
        if diagonal_r in matching:
            count += 1

    if y <= height - 4 and x <= width - 4:
        diagonal_l = ''.join([content[i][j] for i, j in zip(range(y, y + 4), range(x + 3, x - 1, -1))])
        if diagonal_l in matching:
            count += 1

    return count

if __name__ == '__main__':
    
    with open('input.txt', 'r') as f:
        content = [line for line in f.readlines()]
    height, width = len(content), len(content[0])

    print(solution())