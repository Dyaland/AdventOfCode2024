def fragment_file(file_id, file_size):

    for index, chunk in enumerate(disk):
        if chunk[0] == None:
            free_space = chunk[1]
            if free_space <= file_size:
                disk[-1][1] -= free_space
                disk[index][0] = file_id
            else:
                new_space = [None, disk[index][1] - file_size]
                disk[index] = disk.pop()
                if free_space > file_size:
                    disk.insert(index + 1, new_space)
            return


def solution():

    while len([i for i, sublist in enumerate(disk) if sublist[0] is None]) > 0:
        file_id, file_size = disk[-1][0], disk[-1][1]
        fragment_file(file_id, file_size)
        if disk[-1][0] == None:
            disk.pop()

    checksum = 0
    i = 0
    for chunk in disk:
        for _ in range(chunk[1]):
            checksum += chunk[0] * i if chunk[0] is not None else 0
            i += 1
    return checksum


if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        disk = [[id // 2 if id % 2 == 0 else None, int(size)] for id, size in enumerate(f.read().strip())]

    print(solution())
