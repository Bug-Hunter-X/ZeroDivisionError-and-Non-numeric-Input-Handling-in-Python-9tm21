def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("List must contain only numbers.")
    total = sum(numbers)
    if total == 0:
        return 0 # Handle case where all elements are zero
    average = total / len(numbers)
    return average

my_list = [10, 20, 30, 40, 50]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

my_list_zeros = [0,0,0]
average_zeros = calculate_average(my_list_zeros)
print(f"The average of a list of zeros is: {average_zeros}")

#Example of TypeError handling
try:
    my_list_error = [10, 20, 'a', 40, 50]  
    average_error = calculate_average(my_list_error)
    print(f"The average is: {average_error}")
except TypeError as e:
    print(f"Error: {e}") #Prints 'Error: List must contain only numbers.' 