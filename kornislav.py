import sys

inputstd = sys.stdin.read()

line = inputstd.split("\n")
nums = line[0].split()

nums = [int(x) for x in nums]

m_num = nums.index(max(nums))

del nums[m_num]

print max(nums) * min(nums)
