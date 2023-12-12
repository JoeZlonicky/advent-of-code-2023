from condition_record import ConditionRecord

INPUT_FILE_NAME = 'inputs/puzzle.txt'


def main():
    with open(INPUT_FILE_NAME) as f:
        lines = [line.strip() for line in f]
        records = [ConditionRecord.from_line(line, 5) for line in lines if line]

    arrangement_sum = 0
    for record in records:
        arrangement_sum += record.calc_n_arrangements()

    print(f'Total arrangement sum: {arrangement_sum}')


if __name__ == '__main__':
    main()
