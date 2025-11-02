from day_3.day3_solution import get_common_item_priority_sum, get_badges_priority_sum

def test_example():
    assert get_common_item_priority_sum("day_3/example.data") == 157
    assert get_badges_priority_sum("day_3/example.data") == 70

def test_input_data():
    assert get_common_item_priority_sum("day_3/input.data") == 7716
    assert get_badges_priority_sum("day_3/input.data") == 2973