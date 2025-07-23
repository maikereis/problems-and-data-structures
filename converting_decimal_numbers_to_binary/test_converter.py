from converter import divide_by_two, base_converter

def test_divide_by_two():
    assert divide_by_two(42) == '101010'

def test_base_converter():
    assert base_converter(25, 2) == '11001'
    assert base_converter(25, 16) == '19'