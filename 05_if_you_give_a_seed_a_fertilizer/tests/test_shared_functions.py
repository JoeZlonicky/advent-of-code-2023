from shared_functions import get_line_sections_from_text_file, create_mapping_sections, perform_mapping_pipeline


def test_get_sections_from_text_file():
    sections = get_line_sections_from_text_file('../inputs/test_input.txt')
    assert sections == [['seeds: 79 14 55 13'],
                        ['seed-to-soil map:', '50 98 2', '52 50 48'],
                        ['soil-to-location map:', '0 15 37', '37 52 2']]


def test_create_mapping_sections():
    line_sections = get_line_sections_from_text_file('../inputs/test_input.txt')
    mapping_sections = create_mapping_sections(line_sections[1:])
    assert len(mapping_sections) == 2
    assert 'seed' in mapping_sections
    assert 'soil' in mapping_sections


def test_perform_mapping_pipeline():
    line_sections = get_line_sections_from_text_file('../inputs/test_input.txt')
    mapping_sections = create_mapping_sections(line_sections[1:])
    values = perform_mapping_pipeline('seed', [(79, 79), (14, 14), (55, 55), (5, 5), (13, 13)], mapping_sections)
    assert set(values) == {(5, 5), (81, 81), (14, 14), (57, 57), (13, 13)}
