candidates = [2, 3, 6, 7]
target = 7


def backtrack(nums: list[int], remaning, path, start, result):
    if remaning == 0:
        result.append(path.copy())
        return
    if remaning < 0:
        return
    for i in range(start, len(nums)):
        path.append(nums[i])
        backtrack(nums, remaning-nums[i], path, i, result)
        path.pop()


def target_combination(nums: list[int], target ):
    nums.sort()
    result = []
    backtrack(nums, target, [], 0, result)
    return result

print(target_combination(candidates, target))
