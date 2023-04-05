"""Dictionary related utility functions."""

__author__ = "730406615"

# Copied functions:

from csv import DictReader


def read_csv_rows(filename: str) -> list:
    # Note it's a list[dict[str, str]]
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data files as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line by line
    for row in csv_reader:
        result.append(row)

    # Close that file when we're done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list, column: str) -> list:
    """Produces a list[str of all values in a single column."""
    result: list[str] = []

    for row in table:
        # for every index of the list, ex. table[0]
        item: str = row[column]
        result.append(item)

    return result


def columnar(row_table: list) -> dict:
    # note that this is dict[str, list[str]]
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}  # or dict()

    first_row: dict = row_table[0]
    for column in first_row:
        # for every key in first row
        result[column] = column_values(row_table, column)

    return result

# My functions:


def head(coltable: dict, n: int) -> dict:

    # let head return entire table when n is greater then length
    result: dict[str, list[str]] = {}

    for key in coltable:
        # for col in coltable
        result[key] = []
        i: int = 0
        while i < n:
            item: str = coltable[key][i]
            result[key].append(item)
            i += 1

    return result


def select(coltable: dict, querycol: list) -> dict:
    result: dict[str, list[str]] = {}

    for key in querycol:
        result[key] = coltable[key]

    return result


def concat(table1: dict, table2: dict) -> dict:
    result: dict[str, list[str]] = {}

    for key in table1:
        result[key] = table1[key]

    for key in table2:
        if key in result:
            for val in table2[key]:
                result[key].append(val)
        else:
            result[key] = table2[key]

    return result


def count(queryvals: list) -> dict:
    counts: dict[str, int] = {}

    for val in queryvals:
        if val in counts:
            counts[val] += 1
        else:
            counts[val] = 1

    return counts
