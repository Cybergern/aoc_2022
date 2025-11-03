from day_4.day4_solution import get_fully_contained_pairs, get_overlapping_pairs

def test_example():
    assert get_fully_contained_pairs("day_4/example.data") == 2
    assert get_overlapping_pairs("day_4/example.data") == 4

def test_input_data():
    assert get_fully_contained_pairs("day_4/input.data") == 475
    assert get_overlapping_pairs("day_4/input.data") == 825   