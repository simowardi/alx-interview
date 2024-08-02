#!/usr/bin/python3
"""
Determines if all the boxes can be opened.
"""

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list of lists): A list of lists where each inner list represents the
        keys in a box.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    # Initialize variables
    num_boxes = len(boxes)
    opened_boxes = 1  # Start with box 0 opened
    current_box = 0

    # Use a while loop to open as many boxes as possible
    while current_box < num_boxes:
        # Get the keys in the current box
        keys = boxes[current_box]

        # Try to open new boxes with the keys
        for key in keys:
            if key < num_boxes and key not in boxes[key]:
                opened_boxes += 1
                boxes[key] = []  # Mark the box as opened by emptying its keys

        # Move to the next unopened box
        current_box += 1

    # Check if all boxes have been opened
    return opened_boxes == num_boxes
