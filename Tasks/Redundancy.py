my_list = [[21, 77, 31, 12, 35], [10, 10, 10, 10, 10], [30, 23, 35, 62, 94]]

print("The list is :")
print(my_list)

my_result = []
for sub in my_list:
   my_result.append(1 - len(set(sub)) / len(sub))

print("The result is :")
print(my_result)
