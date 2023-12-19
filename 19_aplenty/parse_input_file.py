from machine_part import MachinePart
from processor import Processor


def parse_input_file(file_path) -> tuple[dict[str, Processor], list[MachinePart]]:
    processor_section, part_section = parse_sections(file_path)

    processors = {}
    parts = []

    for line in processor_section:
        name, processor = Processor.from_line(line)
        processors[name] = processor

    for line in part_section:
        parts.append(MachinePart.from_line(line))

    return processors, parts


def parse_sections(file_path: str) -> list[list[str]]:
    with open(file_path) as f:
        lines = [line.strip() for line in f]

    sections = [[]]
    for line in lines:
        if line == '' and len(sections[-1]) > 0:
            sections.append([])
        else:
            sections[-1].append(line)
    return sections
