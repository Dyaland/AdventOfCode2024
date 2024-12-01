def solution(filename):
    
    l1, l2 = [], []
    
    with open(filename, 'r') as f:
        for line in f:
            x, y = map(int, line.split())
            l1.append(x)
            l2.append(y)

    lst1 = sorted(l1)
    lst2 = sorted(l2)

    return sum([abs(lst1[i] - lst2[i]) for i in range(len(lst1))])


if __name__ == '__main__':

    print(solution('input.txt'))