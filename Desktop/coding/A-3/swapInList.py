lst = [1, 2, 3, 4, 5]
pos1, pos2 = 1, 3  # Example positions

temp = lst[pos1]
lst[pos1] = lst[pos2]
lst[pos2] = temp

print("List after swapping:", lst)

