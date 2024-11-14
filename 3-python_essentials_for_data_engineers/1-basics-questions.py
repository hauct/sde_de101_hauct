
# Variable: A storage location identified by its name, containing some value.
# Question: Assign a value of 10 to variable a and 20 to variable b
# Question: Store the result of a + b in a variable c and print it. What is the result of a + b?

s = '  Some string '
# Question 1: How do you remove the empty spaces in front of and behind the string s?
print('Question 1: ')
print(s.strip())
print("="*20)

# Data Structures are ways of representing data, each has its own pros and cons and places that they are the right fit.
## List: A collection of elements that can be accessed by knowing the location (aka index) of the element
l = [1, 2, 3, 4]

# Question 2: How do you access the elements in index 0 and 3? Print the results.
## NOTE: lists retain the order of elements in it but dictionary doesn't
print('Question 2: ')
print(l[0])
print(l[3])

print("="*20)

## Dictionary: A collection of key-value pairs, where each key is mapped to a value using a hash function. Provides fast data retrieval based on keys.
d = {'a': 1, 'b': 2}

# Question 3: How do you access the values associated with keys 'a' and 'b'?
## NOTE: The dictionary cannot have duplicate keys
print('Question 3: ')
print(d['a'])
print(d['b'])

print("="*20)


## Set: A collection of unique elements that do not allow duplicates
my_set = set()
my_set.add(10)
my_set.add(10)
my_set.add(10)

# Question 4: What will be the output of my_set?
print('Question 4: ')
print('{10}')


print("="*20)

## Tuple: A collection of immutable (non-changeable) elements, tuples retain their order once created.
my_tuple = (1, 'hello', 3.14)

# Question 5: What is the value of my_tuple?
print('Question 5: ')
print(my_tuple)


print("="*20)

# Accessing elements by index

# Question 6: How do you access the elements in index 0 and 1 of my_tuple?
print('Question 6: ')
print('Element at index 0:', my_tuple[0])
print('Element at index 1:', my_tuple[1])

print("="*20)


# Counting occurrences of an element
count_tuple = (1, 2, 3, 1, 1, 2)

# Question 7: How many times does the number 1 appear in count_tuple?
print('Question 7: ')
print('Number 1 appears:', count_tuple.count(1), 'times')

print("="*20)

# Finding the index of an element
# Question 8: What is the index of the first occurrence of the number 2 in count_tuple?
print('Question 8: ')
print('First occurrence of number 2 is at index:', count_tuple.index(2))  # 1

print("="*20)

# Loop allows a specific chunk of code to be repeated a certain number of times
# Example: We can use a loop to print numbers 0 through 10
for i in range(11):
    print(i)

# We can loop through our data structures as shown below
# Question 9: How do you loop through a list and print its elements?
print('Question 9: ')
print('Loop through list:')
for element in l:
    print(element)

print("="*20)

# Dictionary loop
# Question 10: How do you loop through a dictionary and print its keys and values?
print('Question 10: ')
for key, value in d.items():
    print(f'Key: {key}, Value: {value}')
print("="*20)

# Comprehension is a shorthand way of writing a loop
# Question 11: Multiply every element in list l with 2 and print the result
print('Question 11: ')
result = [x * 2 for x in l]
print(result)
print("="*20)

# Functions: A block of code that can be re-used as needed. This allows for us to have logic defined in one place, making it easy to maintain and use.
## For example, let's create a simple function that takes a list as an input and returns another list whose values are greater than 3

def gt_three(input_list):
    return [elt for elt in input_list if elt > 3]
## NOTE: we use list comprehension with filtering in the above function

list_1 = [1, 2, 3, 4, 5, 6]
# Question 12: How do you use the gt_three function to filter elements greater than 3 from list_1?
print('Question 12: ')
filtered_list = gt_three(list_1)
print(filtered_list)
print("="*20)

list_2 = [1, 2, 3, 1, 1, 1]
# Question 13: What will be the output of gt_three(list_2)?
print('Question 13: ')
result = gt_three(list_2)
print(result)
print("="*20)

# Classes and Objects
# Think of a class as a blueprint and objects as things created based on that blueprint
# You can define classes in Python as shown below
class DataExtractor:

    def __init__(self, some_value):
        self.some_value = some_value

    def get_connection(self):
        # Some logic
        # some_value is accessible using self.some_value
        pass

    def close_connection(self):
        # Some logic
        # some_value is accessible using self.some_value
        pass

# Question 14: How do you create a DataExtractor object and print its some_value attribute?
print('Question 14: ')
data_extractor = DataExtractor(some_value='example_value')
print(data_extractor.some_value)
print("="*20)

# Libraries are code that can be reused.

# Python comes with some standard libraries to do common operations, 
# such as the datetime library to work with time (although there are better libraries)
from datetime import datetime  # You can import library or your code from another file with the import statement

# Question 15: How do you print the current date in the format 'YYYY MM DD'? Hint: Google strftime
print('Question 15: ')
current_date = datetime.now().strftime('%Y %m %d')
print(current_date)
print("="*20)

# Exception handling: When an error occurs, we need our code to gracefully handle it without just stopping. 
# Here is how we can handle errors when the program is running
try:
    # Code that might raise an exception
    pass
except Exception as e: 
    # Code that runs if the exception occurs
    pass
else:
    # Code that runs if no exception occurs
    pass
finally:
    # Code that always runs, regardless of exceptions
    pass

# For example, let's consider exception handling on accessing an element that is not present in a list l
l = [1, 2, 3, 4, 5]

# Question 16: How do you handle an IndexError when accessing an invalid index in a list?
# NOTE: in the except block its preferred to specify the exact erro/exception that you want to handle
print('Question 16: ')
try:
    print(l[10])  # Truy cập chỉ số không hợp lệ
except IndexError as e:
    print(f'IndexError: {e}')
print("="*20)