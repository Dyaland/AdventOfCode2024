def move_file(file_index, file_size):

    for free_index, chunk in enumerate(disk):
        free_space = chunk[1]
        if all((chunk[0] == None, free_index < file_index, free_space >= file_size)):

            if free_space == file_size:
                disk[free_index] = disk[file_index][:]
                disk[file_index] = [None, file_size]
            elif free_space > file_size:
                disk[free_index] = disk[file_index][:]
                disk[file_index][0] = None
                disk.insert(free_index + 1, [None, free_space - file_size])
            return


def solution():
    
    for file_id in reversed([chunk[0] for chunk in disk if chunk[0] is not None]):
        for index in range(len(disk) - 1, 0, -1):
            if disk[index][0] == file_id:
                size = disk[index][1]
                move_file(index, size)
                break
    
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
