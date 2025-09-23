def two_sum_closest_debug(nums, target):
    print(f"Original: {nums}")
    nums.sort()
    print(f"Sorted: {nums}")
    
    left, right = 0, len(nums) - 1
    closest_sum = 0
    min_distance = float('inf')

    while left < right:
        current_sum = nums[left] + nums[right]
        distance = abs(current_sum - target)
        
        print(f"left={left}({nums[left]}), right={right}({nums[right]}) -> sum={current_sum}, distance={distance}")
        
        if distance < min_distance:
            min_distance = distance
            closest_sum = current_sum
            print(f"  -> NEW BEST: closest_sum={closest_sum}, min_distance={min_distance}")

        if current_sum < target:
            left += 1
            print(f"  -> sum < target, move left to {left}")
        else:
            right -= 1
            print(f"  -> sum >= target, move right to {right}")
        print()

    return closest_sum

# Test
result = two_sum_closest_debug([1, 3, 4, 7, 10], 15)
print(f"Final result: {result}")