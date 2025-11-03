from day_5.day5_solution import get_single_crate_move_top_crates, get_multiple_crate_move_top_crates

def test_example():
    assert get_single_crate_move_top_crates("day_5/example.data") == "CMZ"
    assert get_multiple_crate_move_top_crates("day_5/example.data") == "MCD"

def test_input_data():
    assert get_single_crate_move_top_crates("day_5/input.data") == "SPFMVDTZT"
    assert get_multiple_crate_move_top_crates("day_5/input.data") == "ZFSJBPRFP"