import re


def solution(filename):

    result = 0

    with open(filename, 'r') as f:
        cleaned_text = re.sub(r"don't\(\).*?do\(\)", "do()", f.read(), flags=re.DOTALL)
        match_group = re.findall(r'mul\((\d{1,3},\d{1,3})\)', cleaned_text)

    for string in match_group:
        a, b = map(int, string.split(','))
        result += a * b

    return result


if __name__ == '__main__':

    print(solution('input.txt'))
