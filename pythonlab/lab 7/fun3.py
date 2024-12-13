# Write program to define a function my_max() to complete the following tasks: [Usage of built-in function max() is strictly prohibited]
# If a list of integers is passed as the input argument, the function shall return maximum value present in the list
# If a set is passed, maximum value present in the list
# If a tuple is passed, maximum value present in the tuple
# Hint: Pass the container type unpacked using *


def my_max(*args):
    if len(args) == 0:
        raise ValueError("No elements provided")
    
    max_value = args[0]
    
    for item in args[1:]:
        if item > max_value:
            max_value = item
    
    return max_value

# Helper function to handle different types (list, set, tuple) by unpacking
def get_max(container):
    if isinstance(container, (list, set, tuple)):
        return my_max(*container)
    else:
        raise TypeError("Input must be a list, set, or tuple")

max_in_list = get_max([3, 7, 2, 9, 5])
max_in_set = get_max({10, 20, 5, 15})
max_in_tuple = get_max((100, 25, 75, 50))

print(max_in_list)  
print(max_in_set)  
print(max_in_tuple) 
