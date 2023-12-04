def get_lines_from_text_file(file_name) -> list[str]:
    with open(file_name) as f:
        lines = [line.strip() for line in f]
        return [line for line in lines if line != '']
