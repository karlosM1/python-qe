def dup(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return None

print(dup([1, 2, 3, 4, 3, 5]))