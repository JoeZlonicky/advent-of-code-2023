def parse_input_file(file_name: str) -> list[list[str]]:
    with open(file_name) as f:
        lines = [line.strip() for line in f]
        sections = [[]]
        section_i = 0
        for line in lines:
            if not line:
                sections.append([])
                section_i += 1
                continue

            sections[section_i].append(line)

        return [section for section in sections if len(section) > 0]
