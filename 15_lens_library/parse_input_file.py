def parse_input_file_csv(file_name) -> list[str]:
    with open(file_name) as f:
        line = f.readline().strip()
        csv = line.split(',')
        return csv
