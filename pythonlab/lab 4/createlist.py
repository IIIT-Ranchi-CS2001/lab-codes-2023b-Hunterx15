# create a list of int using list comprehensive . find the mean , median and mode of the given list
numbers = list(map(int, input("Enter your numbers: ").split())) 

mean = sum(numbers) / len(numbers)
sorted_numbers = sorted(numbers)
n = len(sorted_numbers)
if n % 2 == 0:
    median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
else:
    median = sorted_numbers[n // 2]

frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
mode = max(frequency, key=frequency.get)
print(f"List of numbers: {numbers}")
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
