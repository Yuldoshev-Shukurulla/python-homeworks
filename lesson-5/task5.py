# ### Task 1

# Write a script called temperature.py that defines two functions:

# 1. _convert_cel_to_far()_ which takes one float parameter representing degrees Celsius and returns a float representing the same temperature in degrees Fahrenheit using the following formula:
#    _F = C \* 9/5 + 32_
# 2. _convert_far_to_cel()_ which take one float parameter representing degrees Fahrenheit and returns a float representing the same temperature in degrees Celsius using the following formula:
#    _C = (F - 32) \* 5/9_

# The script should first prompt the user to enter a temperature in degrees Fahrenheit and then display the temperature converted to Celsius. Then prompt the user to enter a temperature in degrees Celsius and display the temperature converted to Fahrenheit. All converted temperatures should be rounded to 2 decimal places.

# Here’s a sample run of the program:

# Enter a temperature in degrees C: 72
# 72 degrees F = 22.22 degrees C

# Enter a temperature in degrees C: 37 
# 37 degrees C = 98.60 degrees F

# <hr />
def convert_cel_to_far(c):
    Fr = round(c * 9 / 5 +32, 2)
    print(f'{c} degrees C = {Fr} degrees in F.')

def convert_far_to_cel(f):
    Cel = round((f - 32) * 5 / 9, 2)
    print(f'{f} degrees F = {Cel} degrees in C.')

ca = float(input('Enter a temperature in degrees C: '))
convert_cel_to_far(ca)
ba = float(input('Enter a temperature in degrees F: '))
convert_far_to_cel(ba)



# ### Task 2

# In this challenge, you will write a program called invest.py that tracks the growing amount of an investment over time.

# An initial deposit, called the principal amount, is made. Each year, the amount increases by a fixed percentage, called the annual rate of return.

# For example, a principal amount of \$100 with an annual rate of return of 5% increases the first year by \$5. The second year, the increase is 5% of the new amount \$105, which is \$5.25.

# Write a function called invest with three parameters: the principal amount, the annual rate of return, and the number of years to calculate. The function signature might look something like this:

# python
# def invest(amount, rate, years):


# The function then prints out the amount of the investment, rounded to 2 decimal places, at the end of each year for the specified number of years.

# For example, calling _invest(100, .05, 4)_ should print the following:


# year 1: $105.00
# year 2: $110.25
# year 3: $115.76
# year 4: $121.55


# To finish the program, prompt the user to enter an initial amount, an annual percentage rate, and a number of years. Then call invest() to display the calculations for the values entered by the user.

# <hr />

def invest(amount, rate, years):
    i = 1
    invest = amount
    while i <= years:
        invest = round(invest * (1 + rate), 2)
        print(f'year {i}: ${invest}.')
        i += 1
a = float(input('Enter an initial amount: '))
b = float(input('Enter an annual percentage rate: '))
c = float(input('Enter a number of years: '))
invest(a, b, c)
# ### Task 3

# A factor of a positive integer n is any positive integer less than or equal to n that divides n with no remainder.

# For example, 3 is a factor of 12 because 12 divided by 3 is 4, with no remainder. However, 5 is not a factor of 12 because 5 goes into 12 twice with a remainder of 2.

# Write a script factors.py that asks the user to input a positive integer and then prints out the factors of that number. Here’s a sample run of the program with output:


# Enter a positive integer: 12
# 1 is a factor of 12
# 2 is a factor of 12
# 3 is a factor of 12
# 4 is a factor of 12
# 6 is a factor of 12
# 12 is a factor of 12

def factors(numa):
    for i in range(1, numa+1):
        if numa % i == 0:
            print(f'{i} is a factor of {numa}')
numb = int(input('Enter a positive integer: '))
factors(numb)
    


# ### Task 4

# Write a program that contains the following lists of lists:

# python
universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]


# Define a function, _enrollment_stats()_, that akes, as an input, a list of lists where each individual list contains three elements: (a) the name of a university, (b) the total number of enrolled students, and (c) the annual tuition fees.

# _enrollment_stats()_ should return two lists: the first containing all of the student enrollment values and the second containing all of the tuition fees.

# Next, define a _mean()_ and a _median()_ function. Both functions should take a single list as an argument and return the mean and median of the values in each list.

# Using universities, _enrollment_stats()_, _mean()_, and _median()_, calculate the total number of students, the total tuition, the mean and median of the number of students, and the mean and median tuition values.

# Finally, output all values, and format the output so that it looks like this:


# ******************************
# Total students: 77,285
# Total tuition: $ 271,905

# Student mean: 11,040.71
# Student median: 10,566

# Tuition mean: $ 38,843.57
# Tuition median: $ 39,849
# ******************************

def enrolment_stats(univ):
    enrol_val = []
    tuition = []
    for i in range(0, len(univ)):
        enrol_val.append(univ[i][1])
        tuition.append(univ[i][2])
    return enrol_val, tuition

def mean(mn):
    return sum(mn)/len(mn)
def median(md):
    md.sort()
    lmd = len(md)
    if lmd % 2 != 0:
        return md[lmd // 2]
    else:
        return (md[(lmd // 2) - 1] + md[lmd // 2]) / 2
nums, fees = enrolment_stats(universities)
meanen = mean(nums)
meaden = median(nums)
meant = mean(fees)
meadt = median(fees)
print(f'Total students: {sum(nums):,}')
print(f'Total tuition: $ {sum(fees):,}')
print(f'Student mean: {meanen:,.2f}')
print(f'Student median: {meaden:,}')
print(f'Tuition mean: $ {meant:,.2f}')
print(f'Tuition median: $ {meadt:,}')



# ---

# ### Task 5
# Define a function `is_prime(n)` which returns `True` if the given $n$ ($n$ > 0) is _prime number_, otherwise returns `False`.
def is_prime(n):
    if n < 2:
        print(False)
    else:
        print(not any(n%i == 0 for i in range(2, n)))
abd = int(input('Enter a number you want to check: '))
is_prime(abd)