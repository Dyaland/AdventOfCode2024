def solution(filename):
    
    l1, l2 = [], []
    
    with open(filename, 'r') as f:
        for line in f:
            x, y = map(int, line.split())
            l1.append(x)
            l2.append(y)

    def count_matches(value, lst):
        return sum(x == value for x in lst)

    return sum([l1[i] * count_matches(l1[i], l2) for i in range(len(l1))])


if __name__ == '__main__':

    print(solution('input.txt'))