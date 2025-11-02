from day_2.day2_solution import get_first_strategy_total, get_second_strategy_total

def test_example():
    assert get_first_strategy_total("day_2/example.data") == 15
    assert get_second_strategy_total("day_2/example.data") == 12

def test_input_data():
    assert get_first_strategy_total("day_2/input.data") == 13682
    assert get_second_strategy_total("day_2/input.data") == 12881