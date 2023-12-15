from lens_box import create_lens_boxes, perform_operations_on_boxes, sum_focusing_powers
from parse_input_file import parse_input_file_csv

INPUT_FILE_PATH = './inputs/puzzle.txt'
N_BOXES = 256


def main():
    operations = parse_input_file_csv(INPUT_FILE_PATH)

    boxes = create_lens_boxes(N_BOXES)
    perform_operations_on_boxes(boxes, operations)

    power_sum = sum_focusing_powers(boxes)
    print(f'Sum: {power_sum}')


if __name__ == '__main__':
    main()
