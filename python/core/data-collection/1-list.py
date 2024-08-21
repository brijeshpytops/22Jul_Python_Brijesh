"""
What is list in python?
=====================================

List - mutable, ordered, duplicate values are allowed, indexing, slicing.

syntax:
list_name = [item1, item2, item3, ...]
empty_list = []
list_name = list()

"""

# items = []
# print(type(items))
# print(len(items))

# Accessing a list elements or whole list

# nums = [1,2,3,4,5]
# print(nums) # [1, 2, 3, 4, 5]

# indexing (-/+)
# print(nums[0]) # 1
# print(nums[-1]) # 5
# print(nums[-2]) # 4

# slicing (-/+)
# print(nums[1:3]) # [2, 3]
# print(nums[1:]) # [2, 3, 4, 5]
# print(nums[:3]) # [1, 2, 3]
# print(nums[:]) # [1, 2, 3, 4, 5]

# concat tow or more list
# mummy_list = ['milk', 'butter-milk', 'book']
# aunty_list = ['tomato', '1kg onion']
# sister_list = ['chocolate'] * 2 # replica
# my_list = ['drink', 'chakna']

# total_items = mummy_list + aunty_list + sister_list + my_list

# print(total_items)


# mix_list = [1,2, 4.5, "dhgfds", 43+53j]
# print(mix_list)


# l = list()
# print(dir(l))


items = ['tomato', 'potato', 'onion', 'onion']

new_list = ['apple', 'guava']


# items.append(new_list)
# items.extend(new_list)
# items.insert(0, new_list)
# items[0] = new_list

# items.pop()
# items.pop(1)
# items.remove('onion')
# items.clear()
# del items[0]

# print(items.count('onion'))

# print(items.index('potato'))
# print(items)

#'reverse', 'sort'

# nums = [1,2,3,4,5]
# nums_copy = nums.copy()
# print(id(nums))
# print(id(nums_copy))
# print(nums)
# print(nums_copy)

# x = 10
# print(id(x))
# y = 10
# print(id(y))

# nums = [1,3,54,3,5,54,6,3,5,7,8,3,45,78,3,7,8,2,4,7,4,8,6,5,8]
# # nums.sort(reverse=True)
# # nums.reverse()
# print(nums)


# nested_list = [1,2, [3, [4,5, [8,9,[11, 23, [56,[18, 12, [13]]]]]], 6]]
# print(nested_list)
# print(nested_list[-1])
# print(nested_list[-1][1])
# print(nested_list[-1][1][-1])
# print(nested_list[-1][1][-1][-1])
# print(nested_list[-1][1][-1][-1][-1])
# print(nested_list[-1][1][-1][-1][-1][-1])
# print(nested_list[-1][1][-1][-1][-1][-1][-1])
# print(nested_list[-1][1][-1][-1][-1][-1][-1][0])

# [
#     [
#         [
#             [],
#             []
#         ],
#         [],
#         []
#     ],
#     [],
#     []
# ]