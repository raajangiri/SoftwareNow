# declaring global variable
global_variable = 100

# Dictionary initialization
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# function to process numbers by removing even numbers from the list
def process_numbers():
    global global_variable
    local_variable = 5
    numbers = [1, 2, 3, 4, 5]

    # while loop to process the numbers
    while local_variable > 0:
        if local_variable % 2 == 0:  # If the number is even, remove it
            numbers.remove(local_variable)
        local_variable -= 1

    return numbers

# Set with duplicate values, python automatically handled this by removing duplicates
my_set = {1, 2, 3, 4, 5}

# calling the process_numbers function without passing an argument
result = process_numbers()

# function to modify the dictionary by adding a pair of new key-value
def modify_dict():
    local_variable = 10
    my_dict['key4'] = local_variable  # adding key4 with value 10 to the dictionary

# calling the modify_dict function without arguments
modify_dict()

# function to update the global variable
def update_global():
    global global_variable
    global_variable += 10  # increasing the global variable by 10

# for loop to print numbers from 0 to 4 
for i in range(5):
    print(i)

# conditional check if my_set is not empty and if 'key4' in my_dict has value 10
if my_set is not None and my_dict['key4'] == 10:
    print("Condition met!")

# checking if the value '5' is not in the dictionary's values
if 5 not in my_dict.values():
    print("5 not found in the dictionary!")

# printing the global variable, the dictionary, and the set
print(global_variable)
print(my_dict)
print(my_set)
