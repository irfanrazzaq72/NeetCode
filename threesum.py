

nums = [-4, -1, -1, 0, 1, 2]
target = 9


def three_sum(nums):
    if not nums:
        return nums
    nums.sort()
    result = []

    for current in range(len(nums)-2):
        if current > 0 and nums[current] == nums[current - 1]:
            continue  # skip duplicates for the first element
        left = current +1
        right = len(nums)-1
        while left < right:
            sum = nums[current] + nums[left] + nums[right]
            if sum == 0:
                result.append([nums[current], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

            elif sum < 0:
                left += 1
            else:
                right -= 1
    return result


print(three_sum(nums))
