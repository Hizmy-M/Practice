# Find Closest Number to Zero

# Big O | Time Complexity - O(n) | Space Complexity - O(N)
def findClosestNumber(nums):
    lowest = abs(nums[0])
    for i in nums:
        if abs(i) <= lowest:
           lowest = abs(i)

    return lowest


x = findClosestNumber([-4, -2, 1, 4, 8])
y = findClosestNumber([-100000,-100000])
print(x)
print(y)