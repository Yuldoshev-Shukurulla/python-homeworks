### Number Data Type Questions:

# 1. Create a program that takes a float number as input and rounds it to 2 decimal places.
num1 = float(input('Enter a float number: '))
ro12 = round(num1 , 2)
print(f"Rounded to 2 decimal places: {ro12}")

# 2. Write a Python file that asks for three numbers and outputs the largest and smallest.
num2 = input("Enter three numbers: ")
list1 = num2.split()
list1float = [float(x) for x in list1]
print("Max number is:" + str(max(list1float)) + "\nMin number is:" + str(min(list1float)))

# 3. Create a program that converts kilometers to meters and centimeters.
kms = float(input("Enter value in kilometers: "))
meters = kms * 1000
cms = kms * 100000
print(f"{kms} kilometres is equal to {meters} in meters and {cms} in centimeters")

# 4. Write a program that takes two numbers and prints out the result of integer division and theremainder.
num3  = input("Enter two numbers:")
div1 = float(num3.split()[0])
div2 = float(num3.split()[1])
result = divmod(div1, div2)
print(f"The result of integer division and theremainder is: {result}")

# 5. Make a program that converts a given Celsius temperature to Fahrenheit.
num4 = float(input("Enter a temperature in Celsius degree: "))
faran = (num4 * 9/5) + 32
print(f"{num4} degree Celsius is equal to {faran} Faranheit degree.")

# 6. Create a program that accepts a number and returns the last digit of that number.
num5 = input("Enter a number: ")
print(f"Last digit of {num5} is {num5[-1]}")

# 7. Create a program that takes a number and checks if it’s even or not.
num6 = float(input("Enter a number: "))
div6 = divmod(num6, 2)[1]
if div6 == 1:
    print(f"{num6} is odd number.")
else:
    print(f"{num6} is even number.")


### String Questions:

# 1. Create a program to ask name and year of birth from user and tell them their age.
name1 = input("Enter your name: ")
yearofbirth = float(input("Enter your year of birth: "))
print(f"{name1}, you are {2026-yearofbirth} yeart old.")

# 2. Extract car names from this text:
txt = 'LMaasleitbtui'
print(txt[::2])
print(txt[1::2])

# 3. Write a Python program to:
#    - Take a string input from the user.
#    - Print the length of the string.
#    - Convert the string to uppercase and lowercase.
task3 = input("Enter a string: ")
print(len(task3))
print(task3.upper())
print(task3.lower())

# 4. Write a Python program to check if a given string is `palindrome` or not.
task4 = input("Enter a string: ")
cleaned = task4.lower().replace(" ","")
if task4 == cleaned[::-1]:
    print("String is palindrome.")
else: print("String is not palindrome.")
#  > What is a Palindrome String? A string is called a palindrome if the reverse of the string is the same as the original one. Example: “madam”, “racecar”, “12321”.

# 5. Write a program that counts the number of vowels and consonants in a given string.
task5 = input("Enter a string: ")
task5lower = task5.lower()
vowels = ("a", "o", "i", "e", "u")
i = 0
for x in task5lower:
    if x in vowels:
        i += 1
print(f"In this string there are {len(task5)} letters and {i} of them are vowels and {len(task5)-i} of them are consonants.")
# 6. Write a Python program to check if one string contains another.
task6 = input("Enter a text: ")
task62 = input("Enter a string yo want to check: ")
if task62.lower() in task6.lower():
    print(f"Success! {task62} found in text.")
else: print(f"Sorry, {task62} is not found in text.")

# 7. Ask the user to input a sentence and a word to replace. Replace that word with another word provided by the user.  
# Example:  
#    - Input sentence: "I love apples."  
#    - Replace: "apples"  
#    - With: "oranges"  
#    - Output: "I love oranges."
task7 = input("Enter a setence: ")
task71 = input("Enter a word you want to replace: ")
task72 = input("Enter a word you want to add:")
task73 = task7.replace(task71, task72)
print(task73)

# 8. Write a program that asks the user for a string and prints the first and last characters of the string. 
task8 = input("Enter a string: ")
print(task8[0] + " " + task8[-1])

# 9. Ask the user for a string and print the reversed version of it.
task9 = input("Enter a string: ")
print(f"Reversed: {task9[::-1]}")

# 10. Write a program that asks the user for a sentence and prints the number of words in it.  
task10 = input("Enter a sentence: ")
print(f"There are {len(task10.split())} words in youer sentence.")

# 11. Write a program to check if a string contains any digits.  
task11 = input("Enter a string: ")
if any(x.isdigit() for x in task11):
    print("String contains digit.")
else: print("String does not contain digit.")

# 12. Write a program that takes a list of words and joins them into a single string, separated by a character (e.g., `-` or `,`).  
list12 = ("there", "are", "four", "words.")
joined = "-".join(list12)
print(joined)

# 13. Ask the user for a string and remove all spaces from it.  
task13 = input("Enter a string: ")
print(task13.replace(" ", ""))

# 14. Write a program to ask for two strings and check if they are equal or not.  
task14 = input("Enter first string: ")
task141 = input("Enter second string: ")
if task141 == task14:
    print("These strings are equal.")
else: print("These strings are not equal.")

# 15. Ask the user for a sentence and create an acronym from the first letters of each word.  
    # Example:  
    # - Input: "World Health Organization"  
    # - Output: "WHO"  
task15 = input("Enter a sentence: ")
list15 = task15.split()
for x in list15:
    print(x[0],end="")

# 16. Write a program that asks the user for a string and a character, then removes all occurrences of that character from the string. 
task16 = input("Enter a string: ")
char = input("Enter a character: ")
print(task16.replace(char, "")) 

# 17. Ask the user for a string and replace all the vowels with a symbol (e.g., `*`).  
task17 = input("Enter a string: ").lower()
vowels = ("a", "o", "i", "e", "u")
for x in task17:
    if x in vowels:
        task17 = task17.replace(x, "*")
    else: break
print(task17)

# 18. Write a program that checks if a string starts with one word and ends with another.  
    # Example:  
    # - Input: "Python is fun!"  
    # - Starts with: "Python"  
    # - Ends with: "fun!"  
main = input("Enter a sentence: ")
start = input("Enter a start word: ")
end = input("Enter an end word: ")
if main.startswith(start) and main.endswith(end):
    print("Match.")
else: print("Not match.")

### Boolean Data Type Questions:
# 1. Write a program that accepts a username and password and checks if both are not empty.
username = input("Enter username: ")
password = input("Enter password: ")
print(f"Usename: {bool(username)} \nPassword: {bool(password)}")

# 2. Create a program that checks if two numbers are equal and outputs a message if they are.
boo2 = input("Enter first number: ")
boo21 = input("Enter second number: ")
if boo2 == boo21:
    print("These numbers are equal.")
else: print("These numbers are not equal.")

# 3. Write a program that checks if a number is positive and even.
boo3 = float(input("Enter a number: "))
even1 = divmod(boo3, 2)[1]
if boo3 > 0 and even1 == 0:
    print("The number is positive and even: True")
else:
    print("The number is positive and even: False")
        
# 4. Write a program that takes three numbers and checks if all of them are different.
boo4 = input("Enter three numbers: ")
boo4spl = boo4.split()
boo4float = [float(x) for x in boo4spl]
if boo4float[0] == boo4float[1] or boo4float[1] == boo4float[2] or boo4float[0] == boo4float[2]:
    print("They are not different.")
else: print("They are different.")

# 5. Create a program that accepts two strings and checks if they have the same length.
boo5 = input("Enter the first string: ")
boo51 = input("Enter the second string: ")
print(f"Length of these strings are equal: {bool(len(boo5) == len(boo51))}")

# 6. Create a program that accepts a number and checks if it’s divisible by both 3 and 5.
boo6 = float(input("Enter a number: "))
div3 = divmod(boo6, 3)[1]
div5 = divmod(boo6, 5)[1]
print(f"This number is divisible by both 3 and 5: {bool(div3 == 0 and div5 == 0)}")

# 7. Write a program that checks if the sum of two numbers is greater than 50.
boo7 = input("Enter two numbers: ")
sum7 = float(boo7.split()[0]) +float(boo7.split()[1])
print(f"Summ of these number is greater than 50: {bool(sum7 > 50)}")

# 8. Create a program that checks if a given number is between 10 and 20 (inclusive)
boo8 = float(input("Enter a number: "))
print(f"This number is between 10 and 20(inclusive): {bool(boo8 >= 10 and boo8 <= 20)}")
