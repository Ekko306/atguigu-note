# 定义一个列表
nums = [10, 20, 30, 40, 50]

# 测试正索引,从左边往右，从0开始
# print(nums[0])
# print(nums[1])
# print(nums[2])
# print(nums[3])
# print(nums[4])

# 测试负索引，从右往左，从-1开始，然后-2，以此类推，方便取出对应元素
print(nums[-1])
print(nums[-2])
print(nums[-3])
print(nums[-4])
print(nums[-5])

# 测试错误索引， 下标不能超出范围
# print(nums[5])

# 定义一个嵌套列表
nums2 = [10, 20, ['你好啊','尚硅谷'], 40, 50]
# 取出“尚硅谷”
print(nums2[2][1])