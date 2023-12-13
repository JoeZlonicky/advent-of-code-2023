from summarize import summarize

INPUT_FILE_NAME = './inputs/puzzle.txt'


def main():
    answer = summarize(INPUT_FILE_NAME)
    print(f'Answer: {answer}')


if __name__ == '__main__':
    main()
