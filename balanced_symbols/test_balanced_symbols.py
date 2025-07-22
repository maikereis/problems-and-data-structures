from balanced_symbols.balanced_symbols import par_checker


def test_par_checker():
    assert par_checker("([{}])")


def test_fail_par_checker():
    assert par_checker("{{([][])}()}") != 0