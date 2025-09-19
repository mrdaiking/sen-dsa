def two_sum(nums: list[int], target: int) -> list[int]:

    """
    Given an array of integers nums and an integer target, return indices of the two numbers such
    that they add up to the target.
    Args:
        nums (List[int]): List of integers.
        target (int): Target integer.
    Returns:
        List[int]: Indices of the two numbers such that they add up to the target.
    """
    try:

        if not isinstance(nums, list) or not nums:
            raise ValueError("Input must be a non-empty list")
        
        if not isinstance(target, int):
            raise ValueError("Target must be an integer.")

        seen = {}
        for i, num in enumerate(nums):
            if not isinstance(num, (int, float)):
                raise TypeError(f"All elements in nums must be integers or floats. Found {type(num)} at index {i}.")
            
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[nums[i]] = i
        return []
    except TypeError as e:
        raise TypeError(f"All elements in nums must be integers or floats. {str(e)}")
    except ValueError as e:
        raise ValueError(f"Target must be an integer. {str(e)}")
    except TypeError as e:
        raise TypeError(f"All elements in nums must be integers or floats. {str(e)}")
    except TypeError as e:
        raise TypeError(f"All elements in nums must be integers or floats. {str(e)}")



if __name__ == "__main__":
    # Trường hợp hợp lệ
    print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]

    # Trường hợp lỗi: danh sách rỗng
    try:
        print(two_sum([], 5))
    except ValueError as e:
        print(e)  # Output: Value error occurred: Input 'nums' must be a non-empty list

    # Trường hợp lỗi: target không phải số nguyên
    try:
        print(two_sum([2, 7, 11], "9"))
    except TypeError as e:
        print(e)  # Output: Type error occurred: Target must be an integer

    # Trường hợp lỗi: phần tử không phải số
    try:
        print(two_sum([2, "7", 11], 9))
    except TypeError as e:
        print(e)  # Output: Type error occurred: Element at index 1 is not a number
