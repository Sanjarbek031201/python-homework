1. Sort a Dictionary by Value
Write a Python script to sort (ascending and descending) a dictionary by value.
my_dict = {'apple': 5, 'banana': 2, 'cherry': 7, 'date': 3}
asc_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Ascending:", asc_sorted)
desc_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Descending:", desc_sorted)
2. Add a Key to a Dictionary
Write a Python script to add a key to a dictionary.
Sample Dictionary:
{0: 10, 1: 20}
Expected Result:
{0: 10, 1: 20, 2: 30}
my_dict = {0: 10, 1: 20}
my_dict[2] = 30
print(my_dict)
3. Concatenate Multiple Dictionaries
Write a Python script to concatenate the following dictionaries to create a new one.
Sample Dictionaries:
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
Expected Result:
{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
new_dict = {**dic1, **dic2, **dic3}
print(new_dict)
4. Generate a Dictionary with Squares
Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
Sample Dictionary (n = 5):
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
n = 5
squared_dict = {x: x*x for x in range(1, n+1)}
print(squared_dict)        
5. Dictionary of Squares (1 to 15)
Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
Expected Output:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
squares = {x: x**2 for x in range(1, 16)}
print(squares)
Set Exercises
1. Create a Set
Write a Python program to create a set.
my_set = {1, 2, 3, 4, 5}
print(my_set)       
2. Iterate Over a Set
Write a Python program to iterate over sets.
my_set = {'apple', 'banana', 'cherry'}
for item in my_set:
    print(item)
3. Add Member(s) to a Set
Write a Python program to add member(s) to a set.
my_set = {'apple', 'banana', 'cherry'}
my_set.add('orange')
my_set.update(['mango', 'grape'])
print(my_set)
4. Remove Item(s) from a Set
Write a Python program to remove item(s) from a given set.
my_set = {'apple', 'banana', 'cherry', 'orange'}
my_set.remove('banana')
my_set.discard('grape')
print(my_set)
5. Remove an Item if Present in the Set
Write a Python program to remove an item from a set if it is present in the set.
my_set = {'apple', 'banana', 'cherry'}
item_to_remove = 'banana'
if item_to_remove in my_set:
    my_set.remove(item_to_remove)
print(my_set)
