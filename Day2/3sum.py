class ThreeSum:
    def three_sum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        num_len = len(nums)
        for i in range(num_len):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, num_len - 1
            while left < right:
                print(nums[i], nums[left], nums[right])
                sum_of_three = nums[i] + nums[left] + nums[right]

                if sum_of_three == 0:
                    # Add the combination into res
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif sum_of_three < 0:
                    left += 1
                else:
                    right -= 1

        return res
def main():
    test = [-1,0,1,2,-1,-4]
    ts = ThreeSum()
    print(ts.three_sum(test))  # Expected: [[-1, -1, 2], [-1, 0, 1]]


if __name__ == "__main__":
    main()
        