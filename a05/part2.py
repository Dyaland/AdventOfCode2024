import re


def solution():

    result = 0

    for sequence in updates:
        sequence_rules = [rule for rule in all_rules if all(value in sequence for value in rule)]
        if not check_correct(sequence, sequence_rules):
            fixed_sequence = reorder(sequence, sequence_rules)
            result += int(fixed_sequence[len(fixed_sequence) // 2])
    return result


def check_correct(sequence, rules):
    for rule in rules:
        val_a, val_b = rule[0], rule[1]
        index_a, index_b = sequence.index(val_a), sequence.index(val_b)
        if index_a < index_b:
            continue
        else:
            return False
    return True


def reorder(sequence, rules):
    for rule in rules:
        val_a, val_b = rule[0], rule[1]
        index_a, index_b = sequence.index(val_a), sequence.index(val_b)
        if index_a > index_b:
            sequence[index_a], sequence[index_b] = sequence[index_b], sequence[index_a]
            return reorder(sequence, rules)
    return sequence


if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        content = f.read()

    raw_rules = re.findall(r'(\d{2}\|\d{2})', content)
    raw_updates = re.findall(r'\d{2},.*', content)

    all_rules = [rule.split('|') for rule in raw_rules]
    updates = [sequence.split(',') for sequence in raw_updates]

    print(solution())
