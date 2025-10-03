"""
Day 11 - 3Sum
Tìm tất cả bộ ba số (triplets) trong mảng nums sao cho tổng bằng 0, không trùng lặp.
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Leetcode link: https://leetcode.com/problems/3sum/
Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.            
Constraints:
0 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5


"""

def three_sum(nums):
    res = set()
    if nums is None or len(nums) < 3:
        return res

    # Sort the array
    nums.sort()
    n = len(nums)
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i-1]: # skip duplicate i
            continue
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                res.add((nums[i], nums[left], nums[right]))
                # skip duplicate left
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # skip duplicate right
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return [list(triplet) for triplet in res]
    

# Test cases
if __name__ == "__main__":
    tests = [
        ([], []),
        ([0,0,0], [[0,0,0]]),
        ([1,2,-2,-1], []),
        ([-1,0,1,2,-1,-4], [[-1,-1,2], [-1,0,1]]),
        ([3,-2,1,0], []),
        ([0,0,0,0], [[0,0,0]]),
        ([-2,0,1,1,2], [[-2,0,2], [-2,1,1]]),
    ]
    for i, (nums, expected) in enumerate(tests):
        result = three_sum(nums)
        print(f"Test {i+1}: Input: {nums}\n  Output: {result}\n  Expected: {expected}\n")
