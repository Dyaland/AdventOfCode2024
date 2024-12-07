def test_number(test_value, numbers):

    def try_operators(test_value, numbers, operators):

        nonlocal validated
        if len(operators) == len(numbers) - 1:
            value = numbers[0]

            for i, operator in enumerate(operators, start=1):
                if operator == '*':
                    value *= numbers[i]
                elif operator == '+':
                    value += numbers[i]
                if value > test_value:
                    break
            if value == test_value:
                validated = True
            return

        for operator in ['*', '+']:
            try_operators(test_value, numbers, operators + [operator])

    validated = False
    try_operators(test_value, numbers, operators=list())
    return validated

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        rows = [row.strip() for row in f.readlines()]

    valid_nums = []

    for row in rows:
        test_value = int(row.split(':')[0])
        numbers = [int(num) for num in row.split(':')[1].split()]
        if test_number(test_value, numbers):
            valid_nums.append(test_value)
    print(sum(valid_nums))
