from day_6.day6_solution import get_start_of_packet_marker

def test_example():
    assert get_start_of_packet_marker("day_6/example.data", 4) == 7
    assert get_start_of_packet_marker("day_6/example.data", 14) == 19

def test_input_data():
    assert get_start_of_packet_marker("day_6/input.data", 4) == 1651
    assert get_start_of_packet_marker("day_6/input.data", 14) == 3837