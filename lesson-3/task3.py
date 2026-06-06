
# ### List Tasks
# 1. **Count Occurrences**: Given a list and an element, find how many times the element appears in the list.

fruits = ["apple", "banana",  "peach", "orange", "apple", "watermelon", "apple", "cherry"]
fruit = "apple"
fruits.count(fruit)

# 2. **Sum of Elements**: Given a list of numbers, calculate the total of all the elements.

num3 = [2, 8, 8, 12, 15, 1, 25, 10 , 7, 5]
total = sum(num3)
total

# 3. **Max Element**: From a given list, determine the largest element.

num3 = [2, 8, 8, 12, 15, 1, 25, 10 , 7, 5]
max(num3)

# 4. **Min Element**: From a given list, determine the smallest element.

num3 = [2, 8, 8, 12, 15, 1, 25, 10 , 7, 5]
min(num3)

# 5. **Check Element**: Given a list and an element, check if the element is present in the list.

num3 = [2, 8, 8, 12, 15, 1, 25, 10 , 7, 5]
number = 5
number in num3

# 6. **First Element**: Access the first element of a list, considering what to return if the list is empty.

num3 = [2, 8, 8, 12, 15, 1, 25, 10 , 7, 5]
if num3:
    print(num3[0])
else: print(None)

# 7. **Last Element**: Access the last element of a list, considering what to return if the list is empty.

num3 = [2, 8, 8, 12, 15, 1, 25, 10 , 7, 5]
if num3:
    print(num3[-1])
else: print(None)

# 8. **Slice List**: Create a new list that contains only the first three elements of the original list.

num3 = [2, 8, 8, 12, 15, 1, 25, 10 , 7, 5]
num4 = list(num3[0:3])
num4

# 9. **Reverse List**: Create a new list that contains the elements of the original list in reverse order.

num3 = [2, 8, 8, 12, 15, 1, 25, 10 , 7, 5]
num5 = list(reversed(num3))
num5

# 10. **Sort List**: Create a new list that contains the elements of the original list in sorted order.

num3 = [2, 8, 8, 12, 15, 1, 25, 10 , 7, 5]
num5 = list(sorted(num3))
num5

# 11. **Remove Duplicates**: Given a list, create a new list that contains only unique elements from the original list.

num3 = [2, 8, 8, 12, 15, 1, 25, 10 , 7, 5]
numnew = list(set(num3))
numnew

# 12. **Insert Element**: Given a list and an element, insert the element at a specified index.

num3 = [2, 8, 8, 12, 15, 1, 25, 10 , 7, 5]
num3.insert(5, 35)
num3

# 13. **Index of Element**: Given a list and an element, find the index of the first occurrence of the element.

num3 = [2, 8, 8, 12, 15, 1, 25, 10 , 7, 5]
number = 5
num3.index(number)

# 14. **Check for Empty List**: Determine if a list is empty and return a boolean.

num3 = [2, 8, 8, 12, 15, 1, 25, 10 , 7, 5]
bool(not num3)

# 15. **Count Even Numbers**: Given a list of integers, count how many of them are even.

num3 = [2, 8, 8, 12, 15, 1, 25, 10 , 7, 5]
i = 0
for x in num3:
    if divmod(x, 2)[1] != 1:
        i += 1
i

# 16. **Count Odd Numbers**: Given a list of integers, count how many of them are odd.

num3 = [2, 8, 8, 12, 15, 1, 25, 10 , 7, 5]
i = 0
for x in num3:
    if divmod(x, 2)[1] == 1:
        i += 1
i

# 17. **Concatenate Lists**: Given two lists, create a new list that combines both lists.

num3 = [2, 8, 8, 12, 15, 1, 25, 10 , 7, 5]
fruits = ["apple", "banana",  "peach", "orange", "apple", "watermelon", "apple", "cherry"]
newlist = num3 + fruits
print(newlist)

# 18. **Find Sublist**: Given a list and a sublist, check if the sublist exists within the list.

num4 = [[2, 8, 8, 12], 15, 1, 25, 10 , 7, 5]
sub = [2, 8, 8, 12]
print(sub in num4)

# 19. **Replace Element**: Given a list, replace the first occurrence of a specified element with another element.

num3 = [2, 8, 8, 12, 15, 1, 25, 10 , 7, 5]
num3[num3.index(8)] = 17
num3

# 20. **Find Second Largest**: From a given list, find the second largest element.

num3 = [2, 8, 8, 12, 15, 1, 25, 10 , 7, 5]
uniqnum3 = list(set(num3))
uniqnum3.sort()
print(uniqnum3[-2])

# 21. **Find Second Smallest**: From a given list, find the second smallest element.

num3 = [2, 8, 8, 12, 15, 1, 25, 10 , 7, 5]
uniqnum3 = list(set(num3))
uniqnum3.sort()
print(uniqnum3[1])

# 22. **Filter Even Numbers**: Given a list of integers, create a new list that contains only the even numbers.

num3 = [2, 8, 8, 12, 15, 1, 25, 10 , 7, 5]
evennums = []
for x in num3:
    if divmod(x, 2)[1] == 0:
        evennums.append(x)
evennums

# 23. **Filter Odd Numbers**: Given a list of integers, create a new list that contains only the odd numbers.

num3 = [2, 8, 8, 12, 15, 1, 25, 10 , 7, 5]
oddnums = []
for x in num3:
    if divmod(x, 2)[1] == 1:
        oddnums.append(x)
oddnums

# 24. **List Length**: Determine the number of elements in the list.

num3 = [2, 8, 8, 12, 15, 1, 25, 10 , 7, 5]
len(num3)

# 25. **Create a Copy**: Create a new list that is a copy of the original list.

num3 = [2, 8, 8, 12, 15, 1, 25, 10 , 7, 5]
num33 = num3.copy()
num33

# 26. **Get Middle Element**: Given a list, find the middle element. If the list has an even number of elements, return the two middle elements.

num3 = [2, 8, 8, 12, 15, 1, 25, 10 , 7, 5, 17]
mid = len(num3) // 2
if len(num3) % 2 != 0:
    print(num3[mid])
else: print(num3[mid-1:mid+1])

# 27. **Find Maximum of Sublist**: Given a list, find the maximum element of a specified sublist.

num27 = [2, 8, 8, 12, 15, 1, 25, 10 , 7, 5, 17]
maxsub = max(num27[3 : 7])
maxsub

# 28. **Find Minimum of Sublist**: Given a list, find the minimum element of a specified sublist.

num27 = [2, 8, 8, 12, 15, 1, 25, 10 , 7, 5, 17]
minsub = min(num27[3 : 7])
minsub

# 29. **Remove Element by Index**: Given a list and an index, remove the element at that index if it exists.

num27 = [2, 8, 8, 12, 15, 1, 25, 10 , 7, 5, 17]
ind = 11
if ind <= len(num27):
    num27.remove(num27[ind-1])
num27

# 30. **Check if List is Sorted**: Determine if the list is sorted in ascending order and return a boolean.

num27 = [2, 8, 8, 12, 15, 1, 25, 10 , 7, 5, 17]
numsortcheck = num27 == sorted(num27)
numsortcheck

# 31. **Repeat Elements**: Given a list and a number, create a new list where each element is repeated that number of times.

num27 = [2, 8, 8, 12, 15, 1, 25, 10 , 7, 5, 17]
returntimes = 2
numreturn = num27 * returntimes
numreturn

# 32. **Merge and Sort**: Given two lists, create a new sorted list that merges both lists.

num27 = [2, 8, 8, 12, 15, 1, 25, 10 , 7, 5, 17]
fruits = ["apple", "banana",  "peach", "orange", "apple", "watermelon", "apple", "cherry"]
newsorted = sorted(num27) + sorted(fruits)
print(newsorted)

# 33. **Find All Indices**: Given a list and an element, find all the indices of that element in the list.

num27 = [2, 8, 8, 12, 15, 1, 25, 8, 8, 10 , 7, 5, 17]
a = int(8)
i = 0
indices = []
for x in num27:
    try:
       b = num27.index(a, i)
       i = b + 1
       indices.append(b)
    except ValueError:
        break

indices

# 34. **Rotate List**: Given a list, create a new list that is a rotated version of the original list (shift elements to the right).

num27 = [2, 8, 8, 12, 15, 1, 25, 8, 8, 10 , 7, 5, 17]
numreversed =  num27[::-1]
numreversed

# 35. **Create Range List**: Create a list of numbers in a specified range (e.g., from 1 to 10).

rangelist = list(range(1, 11))
rangelist

# 36. **Sum of Positive Numbers**: Given a list of numbers, calculate the sum of all positive numbers.

num27 = [2, -8, 8, 12, -15, 1, 25, -8, 8, 10 , -7, 5, -17]
i = 0
for x in num27:
    if x > 0:
        i += x
i

# 37. **Sum of Negative Numbers**: Given a list of numbers, calculate the sum of all negative numbers.

num27 = [2, -8, 8, 12, -15, 1, 25, -8, 8, 10 , -7, 5, -17]
i = 0
for x in num27:
    if x < 0:
        i += x
i

# 38. **Check Palindrome**: Given a list, check if the list is a palindrome (reads the same forwards and backwards).

num27 = [2, -8, 8, 12, -15, 1, 25, -8, 8, 10 , -7, 5, -17]
bool(num27 == num27[::-1])

# 39. **Create Nested List**: Create a new list that contains sublists, where each sublist contains a specified number of elements from the original list.

num27 = [2, -8, 8, 12, -15, 1, 25, -8, 8, 10 , -7, 5, -17]
size = 3
nestedlist = []
for i in range(0, len(num27), size):
    nestedlist.append(num27[i:i+size])
nestedlist

# 40. **Get Unique Elements in Order**: Given a list, create a new list that contains unique elements while maintaining the original order.

num27 = [2, -8, 8, 12, -15, 1, 25, -8, 8, 10 , -7, 5, -17]
uniqnum27 = []
seen = set()
for x in num27:
    if x not in seen:
        uniqnum27.append(x)
        seen.add(x)
uniqnum27

# ### Tuple Tasks
# 1. **Count Occurrences**: Given a tuple and an element, find how many times the element appears in the tuple.

mytuple = ('BMW','Ferrari', 'Mercedes Benz', 'Toyota', 'BMW', 'Lexus', 'BMW', 'Bentley', 'Bugatti')
carcheck = 'BMW'
mytuple.count(carcheck)

# 2. **Max Element**: From a given tuple, determine the largest element.

mynumbers = (5, 8, 12, 7, 10, 11, 7, 15, 9, 7, 11, 1, 7)
max(mynumbers)

# 3. **Min Element**: From a given tuple, determine the smallest element.

mynumbers = (5, 8, 12, 7, 10, 11, 7, 15, 9, 7, 11, 1, 7)
min(mynumbers)

# 4. **Check Element**: Given a tuple and an element, check if the element is present in the tuple.

mynumbers = (5, 8, 12, 7, 10, 11, 7, 15, 9, 7, 11, 1, 7)
nuber1 = 12
bool(nuber1 in mynumbers)

# 5. **First Element**: Access the first element of a tuple, considering what to return if the tuple is empty.

mynumbers = (5, 8, 12, 7, 10, 11, 7, 15, 9, 7, 11, 1, 7)
if mynumbers:
    print(mynumbers[0])
else: print(None)

# 6. **Last Element**: Access the last element of a tuple, considering what to return if the tuple is empty.

mynumbers = (5, 8, 12, 7, 10, 11, 7, 15, 9, 7, 11, 1, 7)
if mynumbers:
    print(mynumbers[-1])
else: print(None)

# 7. **Tuple Length**: Determine the number of elements in the tuple.

mynumbers = (5, 8, 12, 7, 10, 11, 7, 15, 9, 7, 11, 1, 7)
len(mynumbers)

# 8. **Slice Tuple**: Create a new tuple that contains only the first three elements of the original tuple.

mynumbers = (5, 8, 12, 7, 10, 11, 7, 15, 9, 7, 11, 1, 7)
newtuple= tuple(mynumbers[0:3])
newtuple

# 9. **Concatenate Tuples**: Given two tuples, create a new tuple that combines both.

mynumbers = (5, 8, 12, 7, 10, 11, 7, 15, 9, 7, 11, 1, 7)
mytuple = ('BMW','Ferrari', 'Mercedes Benz', 'Toyota', 'BMW', 'Lexus', 'BMW', 'Bentley', 'Bugatti')
addded = mynumbers + mytuple
print(addded)

# 10. **Check if Tuple is Empty**: Determine if a tuple has any elements.

mynumbers = (5, 8, 12, 7, 10, 11, 7, 15, 9, 7, 11, 1, 7)
bool(mynumbers)

# 11. **Get All Indices of Element**: Given a tuple and an element, find all the indices of that element in the tuple.

mynumbers = (5, 8, 12, 7, 10, 11, 7, 15, 9, 7, 11, 1, 7)
element = 7
i = 0
indices2 = []
for x in mynumbers:
    try:
        b = mynumbers.index(element, i)
        i = b + 1
        indices2.append(b)
    except ValueError:
        break
indices2

# 12. **Find Second Largest**: From a given tuple, find the second largest element.

mynumbers = (5, 8, 12, 7, 10, 11, 7, 15, 9, 7, 11, 1, 7)
unique = sorted(set(mynumbers))
unique[-2]

# 13. **Find Second Smallest**: From a given tuple, find the second smallest element.

mynumbers = (5, 8, 12, 7, 10, 11, 7, 15, 9, 7, 11, 1, 7)
unique = sorted(set(mynumbers))
unique[1]

# 14. **Create a Single Element Tuple**: Create a tuple that contains a single specified element.

single = (1,)
single

# 15. **Convert List to Tuple**: Given a list, create a tuple containing the same elements.

listednum = [2, -8, 8, 12, -15, 1, 25, -8, 8, 10, -7, 5, -17]
numtuple = tuple(listednum)
numtuple

# 16. **Check if Tuple is Sorted**: Determine if the tuple is sorted in ascending order and return a boolean.

mynumbers = (5, 8, 12, 7, 10, 11, 7, 15, 9, 7, 11, 1, 7)
unique = sorted(mynumbers)
bool(mynumbers == unique)

# 17. **Find Maximum of Subtuple**: Given a tuple, find the maximum element of a specified subtuple.

mynumbers = (5, 8, 12, 7, 10, 11, 7, 15, 9, 7, 11, 1, 7)
suptup = mynumbers[1:7]
max(suptup)

# 18. **Find Minimum of Subtuple**: Given a tuple, find the minimum element of a specified subtuple.

mynumbers = (5, 8, 12, 7, 10, 11, 7, 15, 9, 7, 11, 1, 7)
suptup = mynumbers[1:7]
min(suptup)

# 19. **Remove Element by Value**: Given a tuple and an element, create a new tuple that removes the first occurrence of that element.

mynumbers = (5, 8, 12, 7, 10, 11, 7, 15, 9, 7, 11, 1, 7)
elem1 = 7
removed = list(mynumbers)
removed.remove(elem1)
removedt = tuple(removed)
removedt

# 20. **Create Nested Tuple**: Create a new tuple that contains subtuples, where each subtuple contains specified elements from the original tuple.

mynumbers = (5, 8, 12, 7, 10, 11, 7, 15, 9, 7, 11, 1, 7)
size = 3
templist = []
for i in range(0, len(mynumbers), size):
    chunk = mynumbers[i:i+size]
    templist.append(chunk)

nestedtuple = tuple(templist)
nestedtuple

# 21. **Repeat Elements**: Given a tuple and a number, create a new tuple where each element is repeated that number of times.

mynumbers = (5, 8, 12, 7, 10, 11, 7)
numrep = 3
newtuprep = mynumbers * numrep
newtuprep

# 22. **Create Range Tuple**: Create a tuple of numbers in a specified range (e.g., from 1 to 10).

rangetuple = tuple(list(range(1, 11)))
rangelist

# 23. **Reverse Tuple**: Create a new tuple that contains the elements of the original tuple in reverse order.

mynumbers = (5, 8, 12, 7, 10, 11, 7)
listrev = tuple(reversed(list(mynumbers)))
listrev

# 24. **Check Palindrome**: Given a tuple, check if the tuple is a palindrome (reads the same forwards and backwards).

mynumbers = (5, 8, 12, 7, 10, 11, 7)
reverst = mynumbers[::-1]
bool(mynumbers == reverst)

# 25. **Get Unique Elements**: Given a tuple, create a new tuple that contains only the unique elements while maintaining the original order.

mynumbers = (5, 8, 12, 7, 10, 11, 7, 15, 9, 7, 11, 1, 7)
sortup = []
seem = set()
for  x in mynumbers:
    if x not in seem:
        sortup.append(x)
        seem.add(x)
sortup1 = tuple(sortup)
sortup1

# ### Set Tasks
# 1. **Union of Sets**: Given two sets, create a new set that contains all unique elements from both sets.

set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1 | set2
print(union_set)

# 2. **Intersection of Sets**: Given two sets, create a new set that contains elements common to both sets.

set1 = {1, 2, 3}
set2 = {3, 4, 5}

intersection_set = set1 & set2
print(intersection_set)

# 3. **Difference of Sets**: Given two sets, create a new set with elements from the first set that are not in the second.

set1 = {1, 2, 3}
set2 = {3, 4, 5}

difference_set = set1 - set2
print(difference_set)

# 4. **Check Subset**: Given two sets, check if one set is a subset of the other.

set1 = {1, 2}
set2 = {1, 2, 3, 4}

is_subset = set1.issubset(set2)
print(is_subset)

# 5. **Check Element**: Given a set and an element, check if the element exists in the set.

my_set = {10, 20, 30}
element = 20

exists = element in my_set
print(exists)

# 6. **Set Length**: Determine the number of unique elements in a set.

my_set = {5, 10, 15, 20}

length = len(my_set)
print(length)

# 7. **Convert List to Set**: Given a list, create a new set that contains only the unique elements from that list.

my_list = [1, 2, 2, 3, 4, 4]

unique_set = set(my_list)
print(unique_set)

# 8. **Remove Element**: Given a set and an element, remove the element if it exists.

my_set = {1, 2, 3}
element = 2

my_set.discard(element)
print(my_set)

# 9. **Clear Set**: Create a new empty set from an existing set.

my_set = {1, 2, 3}

empty_set = my_set.copy()
empty_set.clear()
print(empty_set)

# 10. **Check if Set is Empty**: Determine if a set has any elements.

my_set = set()

is_empty = len(my_set) == 0
print(is_empty)

# 11. **Symmetric Difference**: Given two sets, create a new set that contains elements that are in either set but not in both.

set1 = {1, 2, 3}
set2 = {3, 4, 5}

sym_diff = set1 ^ set2
print(sym_diff)

# 12. **Add Element**: Given a set and an element, add the element to the set if it is not already present.

my_set = {1, 2, 3}
element = 4

my_set.add(element)
print(my_set)

# 13. **Pop Element**: Given a set, remove and return an arbitrary element from the set.

my_set = {10, 20, 30}

popped_val = my_set.pop()
print(popped_val)
print(my_set)

# 14. **Find Maximum**: From a given set of numbers, find the maximum element.

numbers = {4, 12, 3, 19, 7}

max_val = max(numbers)
print(max_val)

# 15. **Find Minimum**: From a given set of numbers, find the minimum element.

numbers = {4, 12, 3, 19, 7}

min_val = min(numbers)
print(min_val)

# 16. **Filter Even Numbers**: Given a set of integers, create a new set that contains only the even numbers.

numbers = {1, 2, 3, 4, 5, 6}

evens = {x for x in numbers if x % 2 == 0}
print(evens)

# 17. **Filter Odd Numbers**: Given a set of integers, create a new set that contains only the odd numbers.

numbers = {1, 2, 3, 4, 5, 6}

odds = {x for x in numbers if x % 2 != 0}
print(odds)

# 18. **Create a Set of a Range**: Create a set of numbers in a specified range (e.g., from 1 to 10).

range_set = set(range(1, 11))
print(range_set)

# 19. **Merge and Deduplicate**: Given two lists, create a new set that merges both lists and removes duplicates.

list1 = [1, 2, 3]
list2 = [3, 4, 5]

merged_set = set(list1 + list2)
print(merged_set)

# 20. **Check Disjoint Sets**: Given two sets, check if they have no elements in common.

set1 = {1, 2, 3}
set2 = {4, 5, 6}

is_disjoint = set1.isdisjoint(set2)
print(is_disjoint)

# 21. **Remove Duplicates from a List**: Given a list, create a set from it to remove duplicates, then convert back to a list.

my_list = [1, 2, 2, 3, 4, 4, 5]

clean_list = list(set(my_list))
print(clean_list)

# 22. **Count Unique Elements**: Given a list, determine the count of unique elements using a set.

my_list = ['a', 'b', 'a', 'c', 'b', 'd']

unique_count = len(set(my_list))
print(unique_count)

# 23. **Generate Random Set**: Create a set with a specified number of random integers within a certain range.

import random

random_set = set(random.sample(range(1, 100), 5))
print(random_set)

# ### Dictionary Tasks
# 1. **Get Value**: Given a dictionary and a key, retrieve the associated value, considering what to return if the key doesn’t exist.

men = {
    'name' : 'Shukurulla',
    'lname' : 'Yuldoshev',
    'age' : 24,
    'birthday' : '28 january'
}
key = 'name'
if key in men.keys():
    print(men[key])

# 2. **Check Key**: Given a dictionary and a key, check if the key is present in the dictionary.

men = {
    'name' : 'Shukurulla',
    'lname' : 'Yuldoshev',
    'age' : 24,
    'birthday' : '28 january'
}
key = 'name'
bool(key in men.keys())

# 3. **Count Keys**: Determine the number of keys in the dictionary.

men = {
    'name' : 'Shukurulla',
    'lname' : 'Yuldoshev',
    'age' : 24,
    'birthday' : '28 january'
}
len(men.keys())

# 4. **Get All Keys**: Create a list that contains all the keys in the dictionary.

men = {
    'name' : 'Shukurulla',
    'lname' : 'Yuldoshev',
    'age' : 24,
    'birthday' : '28 january'
}
a = list(men.keys())
a

# 5. **Get All Values**: Create a list that contains all the values in the dictionary.

men = {
    'name' : 'Shukurulla',
    'lname' : 'Yuldoshev',
    'age' : 24,
    'birthday' : '28 january'
}
b = list(men.values())
b

# 6. **Merge Dictionaries**: Given two dictionaries, create a new dictionary that combines both.

men = {
    'name' : 'Shukurulla',
    'lname' : 'Yuldoshev',
    'age' : 24,
    'birthday' : '28 january'
}
Diyorbek = {
    'name1' : 'Diyorbek',
    'lname1' : 'Maxmudjonov',
    'age1' : 23,
    'birthday1' : '25 january'
}
newdict = men | Diyorbek
newdict

# 7. **Remove Key**: Given a dictionary and a key, remove the key if it exists, handling the case if it doesn’t.

data = {'a': 1, 'b': 2, 'c': 3}
key_to_remove = 'b'

data.pop(key_to_remove, None)
print(data)

# 8. **Clear Dictionary**: Create a new empty dictionary.

newdic1 = {}
newdic1

# 9. **Check if Dictionary is Empty**: Determine if a dictionary has any elements.

newdic1 = {}
bool(newdic1)

# 10. **Get Key-Value Pair**: Given a dictionary and a key, retrieve the key-value pair if the key exists.


# 11. **Update Value**: Given a dictionary, update the value for a specified key.

men = {
    'name' : 'Shukurulla',
    'lname' : 'Yuldoshev',
    'age' : 24,
    'birthday' : '28 january'
}
men['age'] = 25
men

# 12. **Count Value Occurrences**: Given a dictionary, count how many times a specific value appears across the keys.

from collections import Counter

data = {'item1': 'apple', 'item2': 'banana', 'item3': 'apple', 'item4': 'orange'}

value_counts = Counter(data.values())

print(value_counts)

# 13. **Invert Dictionary**: Given a dictionary, create a new dictionary that swaps keys and values.

original = {'apple': 'fruit', 'banana': 'fruit', 'carrot': 'vegetable'}

inverted = {}

for key, value in original.items():
    if value not in inverted:
        inverted[value] = []
    inverted[value].append(key)

print(inverted)

# 14. **Find Keys with Value**: Given a dictionary and a value, create a list of all keys that have that value.

data = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
target = 1

keys_with_value = [k for k, v in data.items() if v == target]
print(keys_with_value)

# 15. **Create a Dictionary from Lists**: Given two lists (one of keys and one of values), create a dictionary that pairs them.

keys = ['name', 'age', 'role']
values = ['Alice', 25, 'Analyst']

combined = dict(zip(keys, values))
print(combined)

# 16. **Check for Nested Dictionaries**: Given a dictionary, check if any values are also dictionaries.

data = {'item1': 10, 'item2': {'sub_key': 'value'}, 'item3': 30}

has_nested = any(isinstance(v, dict) for v in data.values())
print(has_nested)

# 17. **Get Nested Value**: Given a nested dictionary, retrieve a value from within one of the inner dictionaries.

nested_data = {'user': {'profile': {'id': 101}}}

value = nested_data.get('user', {}).get('profile', {}).get('id')
print(value)

# 18. **Create Default Dictionary**: Create a dictionary that provides a default value for missing keys.

from collections import defaultdict

default_dict = defaultdict(int)
default_dict['missing_key'] += 1

print(default_dict['missing_key'])

# 19. **Count Unique Values**: Given a dictionary, determine the number of unique values it contains.

data = {'a': 5, 'b': 10, 'c': 5, 'd': 20}

unique_count = len(set(data.values()))
print(unique_count)

# 20. **Sort Dictionary by Key**: Create a new dictionary sorted by keys.

data = {'c': 3, 'a': 1, 'b': 2}

sorted_by_key = dict(sorted(data.items()))
print(sorted_by_key)

# 21. **Sort Dictionary by Value**: Create a new dictionary sorted by values.

data = {'a': 3, 'b': 1, 'c': 2}

sorted_by_value = dict(sorted(data.items(), key=lambda item: item[1]))
print(sorted_by_value)

# 22. **Filter by Value**: Given a dictionary, create a new dictionary that only includes items with values that meet a certain condition.

data = {'a': 15, 'b': 8, 'c': 22, 'd': 5}

filtered_dict = {k: v for k, v in data.items() if v >= 10}
print(filtered_dict)

# 23. **Check for Common Keys**: Given two dictionaries, check if they have any keys in common.

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'c': 4, 'd': 5}

has_common = not dict1.keys().isdisjoint(dict2.keys())
print(has_common)

# 24. **Create Dictionary from Tuple**: Given a tuple of key-value pairs, create a dictionary from it.

pairs_tuple = (('a', 1), ('b', 2), ('c', 3))

resulting_dict = dict(pairs_tuple)
print(resulting_dict)

# 25. **Get the First Key-Value Pair**: Retrieve the first key-value pair from a dictionary.

data = {'a': 1, 'b': 2, 'c': 3}

first_pair = next(iter(data.items()))
print(first_pair)