def solution(filename):

    safe_reports = 0

    with open(filename, 'r') as f:
        for line in f:
            report = list(map(int, line.split()))
            if check_safe(report):
                safe_reports += 1
            else:
                # With dampener
                for i in range(len(report)):
                    dampened = report[::]
                    dampened.pop(i)
                    if check_safe(dampened):
                        safe_reports += 1
                        break
    return safe_reports


def check_safe(report):
    if not all(report[i] < report[i + 1] for i in range(len(report) - 1)) and not all(report[i] > report[i + 1] for i in range(len(report) - 1)):
        return False
    for i in range(len(report) - 1):
        if not abs(report[i] - report[i +1]) <= 3:
            return False
    return True

if __name__ == '__main__':

    print(solution('input.txt'))
