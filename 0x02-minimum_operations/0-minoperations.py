#!/usr/bin/python3
'''The minimum operations coding challenge.'''


def minOperations(n):
    '''
    Computes the fewest number of operations needed to result
    in exactly n H characters.
    '''
    if not isinstance(n, int):
        return 0

    # The number of H's currently in the file
    current_h = 1
    # The number of H's currently stored in the clipboard
    clipboard_h = 0
    # The number of operations performed
    operation_count = 0

    while current_h < n:
        # If the clipboard is empty
        if clipboard_h == 0:
            # Perform a Copy All operation
            clipboard_h = current_h
            # Increment the operation count
            operation_count += 1
        # If we haven't pasted anything yet
        if current_h == 1:
            # Perform a Paste operation
            current_h += clipboard_h
            # Increment the operation count
            operation_count += 1
            # Continue to the next loop iteration
            continue
        remaining_h = n - current_h  # The remaining H's needed to reach the target
        # Check if it's impossible to achieve the target
        if remaining_h < clipboard_h:
            return 0
        # If the remaining H's can't be divided by the current H's
        if remaining_h % current_h != 0:
            # Perform a Paste operation
            current_h += clipboard_h
            # Increment the operation count
            operation_count += 1
        else:
            # Perform a Copy All and Paste operation
            clipboard_h = current_h
            current_h += clipboard_h
            operation_count += 2
    # If we've reached the target
    if current_h == n:
        return operation_count
    else:
        return 0
