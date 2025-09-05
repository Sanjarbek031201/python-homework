1. Create and Access List Elements
Create a list containing five different fruits and print the third fruit.
fruits = ['Apple', 'Banana', 'Cherry', 'Mango', 'Orange']
print("The third fruit is:", fruits[2])

2. Concatenate Two Lists
Create two lists of numbers and concatenate them into a single list.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print(combined_list)
3. Extract Elements from a List
Given a list of numbers, extract the first, middle, and last elements and store them in a new list.
numbers = [10, 20, 30, 40, 50, 60, 70]
first = numbers[0]
middle = numbers[len(numbers) // 2]
last = numbers[-1]
new_list = [first, middle, last]
print(new_list)
4. Convert List to Tuple
Create a list of your five favorite movies and convert it into a tuple.
favorite_movies = ['Inception', 'The Matrix', 'Interstellar', 'The Dark Knight', 'Parasite']
movies_tuple = tuple(favorite_movies)
print(movies_tuple)
5. Check Element in a List
Given a list of cities, check if "Paris" is in the list and print the result.
cities = ['New York', 'London', 'Tokyo', 'Paris', 'Berlin']
if 'Paris' in cities:
    print("Paris is in the list.")
else:
    print("Paris is not in the list.")
6. Duplicate a List Without Using Loops
Create a list of numbers and duplicate it without using loops.
numbers = [1, 2, 3, 4, 5]
duplicated = numbers * 2
print(duplicated)
7. Swap First and Last Elements of a List
Given a list of numbers, swap the first and last elements.
numbers = [10, 20, 30, 40, 50]
numbers[0], numbers[-1] = numbers[-1], numbers[0]
print(numbers)
8. Slice a Tuple
Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.
numbers = tuple(range(1, 11))
slice_result = numbers[3:7]
print(slice_result)
9. Count Occurrences in a List
Create a list of colors and count how many times "blue" appears in the list.
colors = ['red', 'blue', 'green', 'blue', 'yellow', 'blue']
blue_count = colors.count('blue')
print("The color 'blue' appears", blue_count, "times.")
10. Find the Index of an Element in a Tuple
Given a tuple of animals, find the index of "lion".
animals = ('cat', 'dog', 'lion', 'tiger', 'elephant')
lion_index = animals.index('lion')
print("The index of 'lion' is:", lion_index)
11. Merge Two Tuples
Create two tuples of numbers and merge them into a single tuple.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged_tuple = tuple1 + tuple2
print(merged_tuple)
12. Find the Length of a List and Tuple
Given a list and a tuple, find and print their lengths.
my_list = [10, 20, 30, 40]
my_tuple = (5, 15, 25, 35, 45)
print("Length of list:", len(my_list))
print("Length of tuple:", len(my_tuple))
13. Convert Tuple to List
Create a tuple of five numbers and convert it into a list.
my_tuple = (10, 20, 30, 40, 50)
my_list = list(my_tuple)
print(my_list)
14. Find Maximum and Minimum in a Tuple
Given a tuple of numbers, find and print the maximum and minimum values.
numbers = (15, 42, 7, 23, 89, 5)
max_value = max(numbers)
min_value = min(numbers)
print("Maximum value:", max_value)
print("Minimum value:", min_value)
15. Reverse a Tuple
Create a tuple of words and print it in reverse order.
words = ('apple', 'banana', 'cherry', 'date', 'elderberry')
reversed_words = words[::-1]
print(reversed_words)

