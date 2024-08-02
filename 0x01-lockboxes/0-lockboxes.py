#!/usr/bin/python3
'''LockBoxes Challenge'''


def canUnlockAll(boxes):
    '''
    Determines if all the boxes can be opened or not.

    Args:
        boxes (list of lists): A list of lists, where each inner list represents
        the keys in a box.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    '''
    # Get the total number of boxes
    num_boxes = len(boxes)

    # Initialize a set to store the keys and a list to store the opened boxes
    keys = set()
    opened_boxes = [0]  # Start with box 0 opened

    # Iterate through the opened boxes
    i = 0
    while i < len(opened_boxes):
        current_box = opened_boxes[i]

        # Add the keys in the current box to the keys set
        keys.update(boxes[current_box])

        # Try to open new boxes with the keys
        for key in keys:
            if key != 0 and key < num_boxes and key not in opened_boxes:
                opened_boxes.append(key)

        # Move to the next opened box
        i += 1

    # Check if all boxes have been opened
    return len(opened_boxes) == num_boxes

