import math
nums = input().split()
length = math.ceil(int(nums[0])/int(nums[2]))
width = math.ceil(int(nums[1])/int(nums[2]))
print(length * width)