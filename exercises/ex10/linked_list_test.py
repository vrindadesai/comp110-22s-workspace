"""Tests for linked list utils."""


import pytest
from exercises.ex10.linked_list import Node, is_equal, last, value_at, max, scale

__author__ = "730406615"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise an value error."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return a reference to its last Node."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_1() -> None:
    linked_list = Node(10, Node(20, Node(30, None)))
    assert value_at(linked_list, 0) == 10


def test_value_at_2() -> None:
    linked_list = Node(10, Node(20, Node(30, None)))
    assert value_at(linked_list, 1) == 20


def test_value_at_3() -> None:
    linked_list = Node(10, Node(20, Node(30, None)))
    assert value_at(linked_list, 2) == 30


def test_value_at_4() -> None:
    linked_list = Node(10, Node(20, Node(30, None)))
    with pytest.raises(IndexError):
        value_at(linked_list, 4)


def test_max_1() -> None:
    assert max(Node(10, Node(20, Node(30, None)))) == 30


def test_max_2() -> None:
    assert max(Node(10, Node(30, Node(20, None)))) == 30


def test_max_3() -> None:
    assert max(Node(30, Node(20, Node(10, None)))) == 30


def test_scale_1() -> None:
    assert is_equal(scale(Node(1, Node(2, Node(3, None))), 2), (Node(2, Node(4, Node(6, None)))))
