lst = [1, 2, 3, 4, 5]
pos1, pos2 = 1, 3

lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
print("List after swapping:", lst)