#John Sulzen in cooperation with Tyler Rebman
def get_unique_list(input_list):
    set1 = set(input_list) #convert to set, which can only have unique values
    return list(set1) #convert back to list

list1 = [1, 2, 3, 2, 1, 4, 5, 1, 4, 6, 3]
unique_list = get_unique_list(list1)

print("List1 (input):")
print(list1)
print("Unique List:")
print(unique_list)