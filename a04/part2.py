def solution():

    xmas = 0
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            if content[y][x] == 'A':
                xmas += 1 if find_xmas(y, x) else 0
    return xmas


def find_xmas(y, x):

    matching = ['MAS', 'SAM']
    diagonal_r = ''.join([content[var][j] for var, j in zip(range(y - 1, y + 2), range(x - 1, x + 2))]) in matching
    diagonal_l = ''.join([content[var][j] for var, j in zip(range(y - 1, y + 2), range(x + 1, x - 2, -1))]) in matching
    return all([diagonal_r, diagonal_l])

if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        content = [line for line in f.readlines()]
    height, width = len(content), len(content[0])

    print(solution())
