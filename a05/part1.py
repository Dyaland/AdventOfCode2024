import re


def solution():

    result = 0

    for sequence in updates:
        sequence_rules = [rule for rule in all_rules if all(value in sequence for value in rule)]
        if check_correct(sequence, sequence_rules):
            result += int(sequence[len(sequence) // 2])
    return result


def check_correct(sequence, rules):
    for rule in rules:
        val_a, val_b = rule[0], rule[1]
        index_a, index_b = sequence.index(val_a), sequence.index(val_b)
        if index_a > index_b:
            return False
    return True


if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        content = f.read()

    raw_rules = re.findall(r'(\d{2}\|\d{2})', content)
    raw_updates = re.findall(r'\d{2},.*', content)

    all_rules = [rule.split('|') for rule in raw_rules]
    updates = [sequence.split(',') for sequence in raw_updates]

    print(solution())
