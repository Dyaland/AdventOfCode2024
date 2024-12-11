def change(stone):

    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        num_string = str(stone)
        return [int(num_string[:len(num_string) // 2]), int(num_string[len(num_string) // 2:])]
    else:
        return [stone * 2024]


def solution(stones_count):

    for _ in range(75):
        new_count = {}
        for stone, count in stones_count.items():
            transformed = change(stone)
            for new_stone in transformed:
                new_count[new_stone] = new_count.setdefault(new_stone, 0) + count
        stones_count = new_count
    return sum(stones_count.values())


if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        stones_count = {int(value): 1 for value in f.readline().strip().split()}

    print(solution(stones_count))
