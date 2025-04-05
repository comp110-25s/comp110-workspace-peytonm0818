"""Unit test functions for dictionary functions"""

__author__: str = "730573512"

from exercises.ex03.dictionary import invert, favorite_color, count, bin_len

import pytest

with pytest.raises(KeyError):
    my_dictionary = {"kris": "jordan", "michael": "jordan"}
    invert(my_dictionary)


def test_invert_empty() -> None:
    """Tests return value of an empty dictionary parameter, edge case"""
    assert invert({}) == {}


def test_invert_one_key() -> None:
    """Tests return value of just one key/value pair, use case"""
    assert invert({"one": "two"}) == {"two": "one"}


def test_invert_multiple_key() -> None:
    """Tests return value of multiple key/value pairs, use case"""
    assert invert({"one": "two", "three": "four", "five": "six"}) == {
        "two": "one",
        "four": "three",
        "six": "five",
    }


def test_count_empty() -> None:
    """Tests return value of empty list input, edge case"""
    assert count([]) == {}


def test_count_one() -> None:
    """Tests return value if list is one item, use case"""
    assert count(["Peyton"]) == {"Peyton": 1}


def test_count_multiple() -> None:
    """Tests return value if list is multiple items, use case"""
    assert count(["Peyton", "Peyton", "Morgan"]) == {"Peyton": 2, "Morgan": 1}


def test_favorite_color_empty() -> None:
    """Tests return value if list is empty, edge case"""
    assert favorite_color({}) == ""


def test_favorite_color_one() -> None:
    """Tests return value if list has one item, use case"""
    assert favorite_color({"Peyton": "Brown"}) == "Brown"


def test_favorite_color_tie() -> None:
    """Tests return value if there is a tie, use case"""
    assert favorite_color({"Peyton": "Brown", "John": "Blue"}) == "Brown"


def test_bin_len_empty() -> None:
    """Tests return value if input is empty, edge case"""
    assert bin_len([]) == {}


def test_bin_len_single() -> None:
    """Tests return value if there is only 1 item in input, use case"""
    assert bin_len(["Peyton"]) == {6: {"Peyton"}}


def test_bin_len_multiple() -> None:
    """Tests return value if there is multiple items"""
    assert bin_len(["Peyton", "Lauren", "John"]) == {
        6: {"Peyton", "Lauren"},
        4: {"John"},
    }
