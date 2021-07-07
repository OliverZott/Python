from ls24_module import total, join


def test_total_empty() -> None:
    """Total of empty set should be 0.0"""
    assert total([]) == 0.0


def test_total_list() -> None:
    """Total of List should be sum of all elements"""
    assert total([1, 2, 3.1]) == 6.1


def test_total_single_element() -> None:
    """Total of single item should be first item"""
    assert total([2.0]) == 2.0


def test_join_empty_string() -> None:
    """Concatenation of empty list should be empty string"""
    assert join([], '-') == ""


def test_join_single_string() -> None:
    """Concatenation of single item should be item without delimeter"""
    assert join([17], '#') == "17"


def test_join_example_string() -> None:
    """
    Concatenation of non-empty string should be of form as follows:
        join([1,3, 42.0], '') -> 1-3-42.0
    """
    assert join([1, 3, 42.14], '=') == "1=3=42.14"
