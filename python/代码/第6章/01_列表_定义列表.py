# 定义有内容的列表
list1 = [34, 56, 21, 56, 11]
list2 = ['北京', '尚硅谷', '你好啊'] # 字符串
list3 = [23, '尚硅谷', True, None] # 没有类型限制
list4 = [23, '尚硅谷', True, None, [100, 200, 300]]  # 套娃
# 定义空列表（列表中的数据，后期会通过特定写法填充）
list5 = []  # 空列表不是永远空， 后面有特定写法填充
list6 = list() # 内置函数有list关键字，不能重复，自己不能用了

print(list1, type(list1))
print(list2, type(list2))
print(list3, type(list3))
print(list4, type(list4))
print(list5, type(list5))
print(list6, type(list6))