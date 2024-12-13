# Define a function my_zip() that can form a list of tuples by iterating the following customer details:- ‘customer Name, customer ID , shopping points’ and based on the keyword parameter ‘strct’: If strct = True, zipping shall be done only if all lists are of equal length. If strct = False, zipping can be done by taking the minimum length of the iterable.


def my_zip(customer_name, customer_id, shopping_points, strct=True):
    result = []
    
    # Get the lengths of the input lists
    len_name = len(customer_name)
    len_id = len(customer_id)
    len_points = len(shopping_points)

    if strct:
        # Strict mode: only proceed if all lists are of equal length
        if len_name == len_id == len_points:
            for i in range(len_name):
                result.append((customer_name[i], customer_id[i], shopping_points[i]))
        else:
            raise ValueError("All lists must be of the same length when `strct=True`.")
    else:
        # Non-strict mode: proceed with the minimum length of the lists
        min_length = min(len_name, len_id, len_points)
        for i in range(min_length):
            result.append((customer_name[i], customer_id[i], shopping_points[i]))

    return result

# Example usage:
customer_name = ['Alice', 'Bob', 'Charlie']
customer_id = [101, 102, 103, 104]
shopping_points = [200, 150, 300]

try:
    result_strict = my_zip(customer_name, customer_id, shopping_points, strct=True)
except ValueError as e:
    result_strict = str(e)

result_non_strict = my_zip(customer_name, customer_id, shopping_points, strct=False)

print("Strict Mode:", result_strict)
print("Non-Strict Mode:", result_non_strict)






# def my_zip(customer_name, customer_id, shopping_points, strct=True):
#     if strct:
#         if len(customer_name) == len(customer_id) == len(shopping_points):
#             return list(zip(customer_name, customer_id, shopping_points))
#         else:
#             raise ValueError("All lists must be of the same length when `strct=True`.")

#     else:
#         min_length = min(len(customer_name), len(customer_id), len(shopping_points))
#         return list(zip(customer_name[:min_length], customer_id[:min_length], shopping_points[:min_length]))

# customer_name = ['Alice', 'Bob', 'Charlie']
# customer_id = [101, 102, 103, 104]
# shopping_points = [200, 150, 300]

# try:
#     result_strict = my_zip(customer_name, customer_id, shopping_points, strct=True)
# except ValueError as e:
#     result_strict = str(e)

# result_non_strict = my_zip(customer_name, customer_id, shopping_points, strct=False)

# print(result_strict)
# print(result_non_strict)
