import re

def linear_calculation(machine):

    prize_x, prize_y = machine['prize']
    a_x, a_y = machine['A']
    b_x, b_y = machine['B']

    denominator = (a_x * b_y) - (a_y * b_x)
    if denominator == 0:
        return 0

    y = ((a_x * prize_y) - (a_y * prize_x)) // denominator
    x = (prize_x - (b_x * y)) // a_x
    return (y * 1) + (x * 3) if (b_x * y + a_x * x) == prize_x and (b_y * y + a_y * x) == prize_y else 0


def solution():

    return sum(linear_calculation(machine) for machine in claw_machines)


if __name__ == '__main__':

    pattern = re.compile(r'Button A: X\+(\d+), Y\+(\d+)\s+Button B: X\+(\d+), Y\+(\d+)\s+Prize: X=(\d+), Y=(\d+)')

    with open('input.txt', 'r') as f:

        claw_machines = (
            {
                'prize': (10000000000000 + int(prize_x), 10000000000000 + int(prize_y)),
                'A': (int(a_x), int(a_y)),
                'B': (int(b_x), int(b_y))
            }
            for a_x, a_y, b_x, b_y, prize_x, prize_y in pattern.findall(f.read())
            )

    print(solution())
