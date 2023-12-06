from race_calculations import calc_number_of_ways_to_beat_record

INPUT_FILE_NAME = './inputs/full_input.txt'


def main():
    time, distance = parse_input_file(INPUT_FILE_NAME)
    n_ways = calc_number_of_ways_to_beat_record(time, distance)
    print(n_ways)


# Returns (time, distance)
def parse_input_file(file_name) -> tuple[int, int]:
    with open(file_name) as f:
        lines = [line.strip() for line in f]
        lines = [line.split(':')[1].strip() for line in lines]
        numbers = [int(''.join(line.split())) for line in lines]
        return numbers[0], numbers[1]


if __name__ == '__main__':
    main()
