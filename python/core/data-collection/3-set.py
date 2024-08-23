"""
Set : mutable, unordered, unindexed, slicing is not allowed, duplicate values ar not allowed

syntax:
set_name = {} 
set_name = {1,2,3,4,4} 
"""

# set_name = {1,2,3,4,4,564,34,65,78,2,6,78,3,478,2,37,89,89,45,8,61,368,78} 
# # print(type(set_name))
# # print(set_name)
# # print(set_name[2]) # TypeError: 'set' object is not subscriptable
# # print(set_name[::-1]) # TypeError: 'set' object is not subscriptable
# l_set = list(set_name)
# print(l_set)


# Define a set
# set_name = {1, 2, 3, 4, 564, 34, 65, 78, 478, 37, 89, 45, 8, 61, 368}

# # Print the set multiple times
# print("First print:", set_name)
# print("Second print:", set_name)
# print("Third print:", set_name)

# # Convert the set to a list and print
# list_from_set = list(set_name)
# print("List from set:", list_from_set)

# # Sort the list to show a consistent order
# sorted_list = sorted(list_from_set)
# print("Sorted list from set:", sorted_list)

# nums = {1,2,3,4,5}
# nums_frozenset = frozenset(nums)
# nums_frozenset.add(6) # AttributeError: 'frozenset' object has no attribute 'add'
# print(nums_frozenset)
