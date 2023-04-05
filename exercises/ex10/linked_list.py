"""Utility functions for working with Linked Lists."""

from __future__ import annotations
from typing import Optional

__author__ = "730406615"


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"


def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Test if two linked lists are deeply (values and order) equal to one another."""
    if lhs is None and rhs is None:
        return True
    elif lhs is None or rhs is None or lhs.data != rhs.data:
        return False
    else:
        return is_equal(lhs.next, rhs.next)


def last(head: Optional[Node]) -> int:
    """Returns the last value of a Linked List, or raises a ValueError if the list is empty."""
    if head is None:
        raise ValueError("last cannot be called with None")
    elif head.next is None:
        return head.data
    else:
        return last(head.next)


def value_at(head: Optional[Node], index: int) -> int:
    """Returns value at a given index."""
    if head is None:
        raise ValueError("value_at cannot be called with None")
    elif index == 0:
        return head.data
    elif head.next is None and index >= 1:
        raise IndexError("Index is out of bounds on the list.")
    else:
        return value_at(head.next, index - 1)


def max(head: Optional[Node]) -> int:
    if head is None:
        raise ValueError("Cannot call max with None")  # do first thing
    current: int = head.data
    next: int
    if head.next is None:
        return current
    else:
        next = max(head.next)  # this is like working backwards
    if current > next:
        return current
    else:
        return next


def linkify(items: list[int]) -> Optional[Node]:
    if len(items) == 0:
        return None
    else:
        return Node(items[0], linkify(items[1:]))  # Splices list by first valye and will make a new list based on the first value.


def scale(head: Optional[Node], factor: int) -> Optional[Node]:
    if head is None:
        return None
    else:
        return Node(head.data * factor, scale(head.next, factor))


def main() -> None:
    print(scale(linkify([1, 2, 3]), 2))


if __name__ == "__main__":
    main()
