# Find Closest Number to Zero

# Big O | Time Complexity - O(n) | Space Complexity - O(N)
def findClosestNumber(nums):
    lowest = nums[0]
    for i in nums:
        if abs(i) < abs(lowest):
           lowest = i

    if lowest > 0:
        return abs(lowest)

    return lowest


x = findClosestNumber([-4, -2, 1, 4, 8])
y = findClosestNumber([-100000,-100000])
z = findClosestNumber([2,1,1,-1,100000])
print(x)
print(y)
print(z)