from day_1.day1_solution import get_top_calory_total, get_top_three_calory_sum

def test_example():
    assert get_top_calory_total("day_1/example.data") == 24000
    assert get_top_three_calory_sum("day_1/example.data") == 45000

def test_input_data():
    assert get_top_calory_total("day_1/input.data") == 69912
    assert get_top_three_calory_sum("day_1/input.data") == 208180