import numpy as np


def straighten_rectangles(rectangles):
    """
    Straightens the rectangles presented diagonally by rotating them.

    Args:
        rectangles (list): List of dictionaries representing rectangles,
                           each containing keys 'x', 'y', 'width', and 'height'.

    Returns:
        list: List of dictionaries representing straightened rectangles.
    """
    # Assuming you have logic to straighten the rectangles based on their corners
    # You might use the corner points of each rectangle to perform rotation or perspective transformation

    # Get the rotation angle to straighten the rectangles
    angle = calculate_rotation_angle(
        rectangles[0]["x"], rectangles[0]["y"], rectangles[2]["x"], rectangles[2]["y"]
    )

    # Apply the rotation angle to each rectangle
    for rectangle in rectangles:
        rotate_rectangle(rectangle, angle)

    return rectangles


def calculate_rotation_angle(x1, y1, x2, y2):
    """
    Calculates the rotation angle needed to straighten the rectangles.

    Args:
        x1 (int): X-coordinate of the first point.
        y1 (int): Y-coordinate of the first point.
        x2 (int): X-coordinate of the second point.
        y2 (int): Y-coordinate of the second point.

    Returns:
        float: Rotation angle in degrees.
    """
    # Implement your logic to calculate the rotation angle
    # You might use the coordinates of two points on the line inside the rectangle
    # For simplicity, I'll assume a horizontal line and calculate the angle
    dx = x2 - x1
    dy = y2 - y1
    angle = np.arctan2(dy, dx) * 180 / np.pi

    return angle


def rotate_rectangle(rectangle, angle):
    """
    Rotates an individual rectangle based on a given angle.

    Args:
        rectangle (dict): Dictionary representing a rectangle with keys 'x', 'y', 'width', and 'height'.
        angle (float): Rotation angle in degrees.
    """
    # Rotate the rectangle based on the calculated angle
    # Assuming rectangle has keys 'x', 'y', 'width', 'height'
    center_x = rectangle["x"] + rectangle["width"] // 2
    center_y = rectangle["y"] + rectangle["height"] // 2

    # Apply the rotation to rectangle coordinates
    rotated_x = (
        (rectangle["x"] - center_x) * np.cos(np.radians(angle))
        - (rectangle["y"] - center_y) * np.sin(np.radians(angle))
        + center_x
    )
    rotated_y = (
        (rectangle["x"] - center_x) * np.sin(np.radians(angle))
        + (rectangle["y"] - center_y) * np.cos(np.radians(angle))
        + center_y
    )

    # Update rectangle coordinates
    rectangle["x"], rectangle["y"] = int(rotated_x), int(rotated_y)


def main():
    # Assuming rectangles is a list of dictionaries with keys 'x', 'y', 'width', 'height'
    rectangles = [
        {"x": 10, "y": 20, "width": 30, "height": 40},
        {"x": 30, "y": 40, "width": 50, "height": 60},
        {"x": 50, "y": 60, "width": 70, "height": 80},
        {"x": 70, "y": 80, "width": 90, "height": 100},
    ]

    aligned_rectangles = straighten_rectangles(rectangles)
    print(aligned_rectangles)


if __name__ == "__main__":
    main()
