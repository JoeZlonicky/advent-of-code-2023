from hand import Hand


def parse_hands_from_file(file_name):
    with open(file_name) as f:
        lines = [line.strip() for line in f]
        hands = [Hand.from_line(line) for line in lines if line != '']
        return hands
