nums = input().split()
nums[0], nums[1] = nums[0][::-1], nums[1][::-1]
print(max(list(map(int, nums))))