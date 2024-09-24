#!/usr/bin/python3
"""
A function to calculate the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    This function calculates the perimeter of the island.
    Args:
    grid: A list of lists where 0 represents water and 1 represents land.
    Returns:
    The perimeter of the island.
    """
    # This will store the total perimeter
    perimeter = 0

    # Loop through each row in the grid
    for row in range(len(grid)):
        # Loop through each column in the current row
        for col in range(len(grid[row])):
            # Check if the current cell is land (1)
            if grid[row][col] == 1:
                # Start by adding 4 to the perimeter for this piece of land
                perimeter += 4

                # If there is land directly above, subtract 2
                # (they share a side)
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2

                # If there is land directly to the left, subtract 2
                # (they share a side)
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2

    # Return the final perimeter
    return perimeter
