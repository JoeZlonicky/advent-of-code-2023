import pytest
from mapping_section import MappingSection
from mapping import Mapping


@pytest.fixture
def example_mapping():
    m_s = MappingSection('seed', 'soil')
    m_s.add_mapping(Mapping(10, 20, 5))
    m_s.add_mapping(Mapping(40, 70, 2))
    return m_s


def test_map_values(example_mapping):
    values = example_mapping.map_ranges([(5, 5), (14, 14), (41, 41), (43, 43)])
    assert set(values) == {(5, 5), (24, 24), (71, 71), (43, 43)}


def test_map_values_with_ranges(example_mapping):
    values = example_mapping.map_ranges([(4, 4), (8, 12), (13, 16), (40, 41)])
    assert set(values) == {(4, 4), (8, 9), (20, 22), (23, 24), (15, 16), (70, 71)}


def test_from_section_lines():
    lines = ['seed-to-soil map:',
             '50 98 2',
             '52 50 48']
    m_s = MappingSection.from_section_lines(lines)
    assert m_s.input_name == 'seed'
    assert m_s.output_name == 'soil'
    assert len(m_s.mappings) == 2


def test_parse_mapping_title():
    input_name, output_name = MappingSection.parse_mapping_title('seed-to-soil map:')
    assert input_name == 'seed'
    assert output_name == 'soil'
