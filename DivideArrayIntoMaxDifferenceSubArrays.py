def divide_array(nums, k):
    nums.sort()

    answer_array = []

    for i in range(0, len(nums), 3):
        current_array = [nums[i]]
        current_number = nums[i]
        lower_limit = current_number - k
        higher_limit = current_number + k
        first_number = nums[i + 1]
        second_number = nums[i + 2]

        if lower_limit <= (first_number) <= higher_limit:
            current_array.append(first_number)
        else:
            return []
        if lower_limit <= (second_number) <= higher_limit:
            current_array.append(second_number)
        else:
            return []
        answer_array.append(current_array)
    return answer_array

print(divide_array([1,3,3,2,7,3], 3))