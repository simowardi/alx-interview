#!/usr/bin/python3
'''The minimum operations coding challenge.
'''


def minOperations(n):
   '''Computes the fewest number of operations needed to result
   in exactly n H characters.
   '''
   if not isinstance(n, int):
       return 0

   # Counter for the number of operations performed
   operation_count = 0
   # Stores the number of H's that can be copied and pasted
   buffer = 0
   # Represents the current number of H's in the file
   current_h = 1

   while current_h < n:
       if buffer == 0:
           # Perform the initial Copy All and Paste operations to start building the H's
           buffer = current_h
           current_h += buffer
           operation_count += 2
       elif n - current_h > 0 and (n - current_h) % current_h == 0:
           # Perform Copy All and Paste operations when it's more efficient to do so, 
           # to increase the number of H's in the file
           buffer = current_h
           current_h += buffer
           operation_count += 2
       elif buffer > 0:
           # Perform a Paste operation to add the contents of the buffer to the current H's
           current_h += buffer
           operation_count += 1

   return operation_count
