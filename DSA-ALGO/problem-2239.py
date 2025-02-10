# Find Closest Number to Zero

# Function to find the number closest to zero in a list
# Big O Analysis:
# Time Complexity: O(n) - We traverse the entire list once to find the closest number.
# Space Complexity: O(1) - Only a constant amount of space is used for the variable `lowest`.
def findClosestNumber(nums):
    # Initialize the closest number as the first element in the list
    lowest = nums[0]

    # Iterate through the list to find the number closest to zero
    for i in nums:
        # Update `lowest` if the absolute value of the current number is smaller
        if abs(i) < abs(lowest):
            lowest = i

    # Handle the edge case when two opposite numbers are equidistant from zero
    # Return the positive number if both are present in the list
    if lowest < 0 and abs(lowest) in nums:
        return abs(lowest)

    return lowest


# Test cases
x = findClosestNumber([2, -1, 1])  # Expected output: 1
y = findClosestNumber([-100000, -100000])  # Expected output: -100000
z = findClosestNumber([2, 1, 1, -1, 100000])  # Expected output: 1

# Print results
print(x)
print(y)
print(z)
