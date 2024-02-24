import numpy as np


def assign_numbers(rectangles):
    """
    Assign numbers (1 to 4) to rectangles based on the length of the line inside each rectangle.

    Parameters:
    - rectangles (list): List of dictionaries with keys 'length', 'x', and 'y' representing rectangles.

    Returns:
    - list: List of dictionaries with assigned numbers.
    """
    # Sort rectangles based on the length in ascending order
    rectangles.sort(key=lambda x: x["length"])

    # Assign numbers from 1 to 4 based on the sorted order
    for i, rectangle in enumerate(rectangles):
        rectangle["number"] = i + 1

    return rectangles


def sort_rectangles_by_length(rectangles):
    """
    Sort rectangles based on the length of the line inside each rectangle.

    Parameters:
    - rectangles (list): List of dictionaries with keys 'length', 'x', and 'y' representing rectangles.

    Returns:
    - list: List of dictionaries with rectangles sorted by length.
    """
    # Sort rectangles based on the length of the line inside each rectangle
    rectangles.sort(key=lambda x: x["length"])

    return rectangles


def main():
    # Assuming rectangles is a list of dictionaries with keys 'length', 'x', and 'y'
    rectangles = [
        {"length": 80, "x": 10, "y": 20},
        {"length": 120, "x": 30, "y": 40},
        {"length": 160, "x": 50, "y": 60},
        {"length": 100, "x": 70, "y": 80},
    ]

    sorted_rectangles = sort_rectangles_by_length(rectangles)
    numbered_rectangles = assign_numbers(sorted_rectangles)
    print(numbered_rectangles)


if __name__ == "__main__":
    main()
