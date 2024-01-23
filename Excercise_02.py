#John Sulzen in cooperation with Tyler Rebman
#Referencing https://www.w3schools.com/python/python_ref_dictionary.asp
def get_combined_dict(dict1, dict2):
    dict3 = {}
    new_value = 0
    for x in dict1: #for each common key
        if x in dict2:
            new_value = dict1.get(x) + dict2.get(x) #summation of values
            dict3[x] = new_value
    return dict3

my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}

combined_dict = get_combined_dict(my_dict_1, my_dict_2)
print(combined_dict)