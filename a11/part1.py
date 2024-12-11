def change(stones):

    for i in range(len(stones) - 1, -1, -1):
        if stones[i] == 0:
            stones[i] = 1
        elif len(str(stones[i])) % 2 == 0:
            num_string = str(stones[i])
            stones[i:i + 1] = (int(num_string[:len(num_string) // 2]), int(num_string[len(num_string) // 2:]))
        else:
            stones[i] *= 2024
            

def solution():
    for _ in range(25):
        change(stones)
    return len(stones)


if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        stones = [int(value) for value in f.readline().strip().split()]

    print(solution())
