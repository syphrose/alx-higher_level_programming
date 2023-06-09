def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list

my_list = [10, 20, 30, 40, 50]
print(replace_in_list(my_list, 3, 55))
print(replace_in_list(my_list, -1, 40))
print(replace_in_list(my_list, 5, 35))
