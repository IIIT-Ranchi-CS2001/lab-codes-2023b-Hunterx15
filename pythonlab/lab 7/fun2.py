# Define a function my_sort() to sort the list of tuples created using my_zip function in the last question. The function must have two types of arguments- the list that carry the data, the key that determines the argument of sorting:
# [Usage of built-in function sorted() is a punishable offense]
# Key = 0: sorting based on customer name in ascending order
# Key = 1: sorting based on Customer ID
# Key = 2: sorting based on shopping points

def my_sort(data, key=0):
    def manual_sort(data, key):
        n = len(data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if data[j][key] > data[j + 1][key]:
                    data[j], data[j + 1] = data[j + 1], data[j]  # Swap elements
        return data
    
    if key not in [0, 1, 2]:
        raise ValueError("Invalid key. Must be 0 (Name), 1 (ID), or 2 (Points).")
    
    return manual_sort(data, key)

data = [('Alice', 101, 200), ('Bob', 102, 150), ('Charlie', 103, 300)]

sorted_by_name = my_sort(data, key=0) 
sorted_by_id = my_sort(data, key=1)   
sorted_by_points = my_sort(data, key=2) 

print(sorted_by_name)
print(sorted_by_id)
print(sorted_by_points)
