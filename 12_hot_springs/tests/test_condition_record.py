import pytest
from condition_record import ConditionRecord


@pytest.fixture
def undamaged_record():
    return ConditionRecord.from_line('#.#.### 1,1,3')


@pytest.fixture
def simple_record():
    return ConditionRecord.from_line('????.#...#... 4,1,1')


@pytest.fixture
def complex_record():
    return ConditionRecord.from_line('?###???????? 3,2,1')


def test_calc_n_arrangements_undamaged(undamaged_record):
    assert undamaged_record.calc_n_arrangements() == 1


def test_calc_n_arrangements_simple(simple_record):
    assert simple_record.calc_n_arrangements() == 1


def test_calc_n_arrangements_complex(complex_record):
    assert complex_record.calc_n_arrangements() == 10


def test_from_line(simple_record):
    assert simple_record.spring_row == '????.#...#...'
    assert simple_record.damaged_contiguous_groups == [4, 1, 1]
