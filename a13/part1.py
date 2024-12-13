import heapq
import re


def largest_divisor(a, b):

    while b != 0:
        a, b = b, a % b
    return a


def divisibility_check(a_x, b_x, a_y, b_y, prize_x, prize_y):

    def greatest_common_and_coeff(a, b):

        if b == 0:
            return a, 1, 0
        g, x1, y1 = greatest_common_and_coeff(b, a % b)
        x, y = y1, x1 - (a // b) * y1
        return g, x, y

    gcd_x = greatest_common_and_coeff(a_x, b_x)[0]
    gcd_y = greatest_common_and_coeff(a_y, b_y)[0]
    if prize_x % gcd_x == 0 and prize_y % gcd_y == 0:
        return True


def dijkstra_cheapest_path(machine):

    a_x, a_y = machine['A']
    b_x, b_y = machine['B']
    prize_x, prize_y = machine['prize']

    if not divisibility_check(a_x, b_x, a_y, b_y, prize_x, prize_y):
        return 0

    queue = [(0, 0, 0, 0, 0)]
    visited = set()

    while queue:

        cost, a_press, b_press, x, y = heapq.heappop(queue)

        if any((a_press > 100, b_press > 100, (x, y) in visited)):
            continue
        if (x, y) == (prize_x, prize_y):
            return cost
        visited.add((x, y))

        new_x, new_y = x + a_x, y + a_y
        if (new_x, new_y) not in visited:
            heapq.heappush(queue, (cost + 3, a_press + 1, b_press, new_x, new_y))

        new_x, new_y = x + b_x, y + b_y
        if (new_x, new_y) not in visited:
            heapq.heappush(queue, (cost + 1,  a_press, b_press + 1, new_x, new_y))
    return 0


def solution():

    return sum(dijkstra_cheapest_path(machine) for machine in claw_machines or 0)


if __name__ == '__main__':

    pattern = re.compile(r'Button A: X\+(\d+), Y\+(\d+)\s+Button B: X\+(\d+), Y\+(\d+)\s+Prize: X=(\d+), Y=(\d+)')

    with open('input.txt', 'r') as f:

        claw_machines = (
            {
                'prize': (int(prize_x), int(prize_y)),
                'A': (int(a_x), int(a_y)),
                'B': (int(b_x), int(b_y))
            }
            for a_x, a_y, b_x, b_y, prize_x, prize_y in pattern.findall(f.read())
        )

    print(solution())
