from race_calculations import calc_number_of_ways_to_beat_record

INPUT_FILE_NAME = 'inputs/puzzle.txt'


def main():
    times, distances = parse_input_file(INPUT_FILE_NAME)
    ways_of_beating_record = []
    for t, d in zip(times, distances):
        ways_of_beating_record.append(calc_number_of_ways_to_beat_record(t, d))

    if len(ways_of_beating_record) == 0:
        print(0)
        return

    product = ways_of_beating_record[0]
    for n_ways in ways_of_beating_record[1:]:
        product *= n_ways
    print(product)


# Returns (times, distances)
def parse_input_file(file_name) -> tuple[list[int], list[int]]:
    with open(file_name) as f:
        lines = [line.strip() for line in f]
        lines = [line.split(':')[1] for line in lines]
        numbers = [[int(number_string) for number_string in line.split()] for line in lines]
        return numbers[0], numbers[1]


if __name__ == '__main__':
    main()
