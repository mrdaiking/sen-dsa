"""
LeetCode 15: 3Sum - Sorting + Two Pointers Approach
Pattern focus: Duplicate elimination, pointer movement, and time/space analysis.
"""

def three_sum(nums):
    """
    Approach: Sort + Two Pointers
    - Sort array to bring duplicates together
    - For each i, use two pointers (left, right) to find triplets
    - Skip duplicates for i, left, and right
    Time: O(n^2)
    Space: O(1) (excluding output)
    """
    nums.sort()
    res = []
    n = len(nums)
    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue  # Skip duplicate i
        left, right = i + 1, n - 1
        while left < right:
            print(nums[i], nums[left], nums[right])
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                res.append([nums[i], nums[left], nums[right]])
                # Skip duplicate left
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                # Skip duplicate right
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return res

# Example usage
test = [-1,0,1,2,-1,-4]
print(three_sum(test))  # Expected: [[-1, -1, 2], [-1, 0, 1]]


