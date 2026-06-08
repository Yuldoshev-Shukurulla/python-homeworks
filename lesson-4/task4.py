# ## Questions:

# 1. <a href="https://pynative.com/python-if-else-and-for-loop-quiz/">Loops quiz</a>
# Congratulations, You have completed Python Flow Control ( If Else and Loops) Quiz.
# You scored 24 points out of 25 points in total.

# No of Correct Answers: 24
# No of wrong Answers: 1
# Number of unanswered questions: 0
# Your obtained grade is PASS 
# 2.  What is the difference between the continue and break statements in Python?
# The break statement exits the loop immediately. Any remaining iterations are completely canceled, and Python moves on to the code below the loop.
# The continue statement skips the rest of the code inside the loop for the current iteration only. It jumps straight to the top of the loop to start the very next turn.
# 3. Can you explain the difference between for loop and while loop?
# A for loop is used when we know in advance how many times we want to run the code. It iterates over a sequence (like a list, a dictionary, a string, or a specific range).
# A while loop is used when we do not know how many times the loop will need to run. It keeps executing as long as a specific condition remains True.
# 4. How would you implement a nested for loop system? Provide an example.
# for x in range(1, 4):
#     for y in range(1, 3):
#         print(f"Grid point: ({x}, {y})") 

 

# ## Homeworks:

# **1.** Return uncommon elements of lists. Order of elements does not matter.

# input:
#     list1 = [1, 1, 2]
#     list2 = [2, 3, 4]
# output: [1, 1, 3, 4]




# input:
#     list1 = [1, 2, 3]
#     list2 = [4, 5, 6]
# output: [1, 2, 3, 4, 5, 6]



# input:
#   list1 = [1, 1, 2, 3, 4, 2]
#   list2 = [1, 3, 4, 5]
# output: [2, 2, 5]
list3 = list(set(list1).symmetric_difference(set(list2)))
print(list3)


# **2.** Print the square of each number which is less than `n` on a separate line.


# input: n = 5
# output:
#     1
#     4
#     9
#     16
n = int(input('Enter a number:'))
for i in range(1, n):
    print(i * i)


# **3.** `txt` nomli string saqlovchi o'zgaruvchi berilgan. `txt`dagi har uchinchi belgidan keyin pastgi chiziqcha (underscore) qo'yilsin. Agar belgi unli harf yoki orqasidan ostki chiziqcha qo'yilgan harf bo'lsa, ostki chiziqcha keyingi harfdan keyin qo'yilsin. Agar belgi satrdagi oxirgi belgi bo'lsa chiziqcha qo'yilmasin.


# input: hello
# output: hel_lo



# input: assalom
# output: ass_alom



# input: abcabcdabcdeabcdefabcdefg
# output: abc_abcd_abcdeab_cdef_abcdefg
txt = input('Enter a string:')
vovels = ['a', 'o','u', 'i', 'e', 'A', 'O', 'U', 'I', 'E']
charcount = 0
result = []
dashes = []
n = len(txt)

for idx, char in enumerate(txt):
    charcount += 1
    result.append(char)
    if idx == n - 1:
        break
    if charcount == 3:
        next_char = txt[idx + 1] if idx + 1 < n else ""
        
        if char in vovels or char in dashes:
            charcount -= 1  
        else:
            result.append("_")
            dashes.append(char)
            charcount = 0   

final_text = "".join(result)
print("Natija:", final_text)


# **4. Number Guessing Game**
# Create a simple number guessing game.
# - The computer randomly selects a number between 1 and 100. 
# - If the guess is high, print "Too high!". 
# - If the guess is low, print "Too low!". 
# - If they guess correctly, print "You guessed it right!" and exit the loop.
# - The player has 10 attempts to guess it. If the player can not find the correct number in 10 attempts, print "You lost. Want to play again? ".
# - If the player types one of 'Y', 'YES', 'y', 'yes', 'ok' then start the game from the beginning.
import random as r
yes1 = ['Y', 'YES', 'y', 'yes', 'ok']
play = True
while play:
    i = 0
    number = r.randint(1, 100)
    print('I thought a number between 1 and 100.')

    while i < 10:
        try1 = int(input("Enter your guess:"))
        if try1 < number:
            print("Too low!")
            i += 1
        elif try1 > number:
            print("Too high!")
            i += 1
        else: 
            print('You guessed it right!')
            break

    else: 
        print(f'You lost, number was {number}')
    play1 = input('Do you want to play again?')
    play = True if play1 in yes1 else False


# > Hint: Use Python’s `random.randint()` to generate the number.

# **5. Password Checker**
# Task: Create a simple password checker.
# - Ask the user to enter a password. 
# - If the password is shorter than 8 characters, print "Password is too short." 
# - If the password doesn’t contain at least one uppercase letter, print "Password must contain an uppercase letter.". 
# - If the password meets both criteria, print "Password is strong."
while True:
    passw = input("Create a new password: ")
    if len(passw) < 8:
        print("Password is too short!")
        continue
    elif not any(char.isupper() for char in passw):
        print('Password should contain at list one uppercase letter.')
        continue
    else:
        print("Password is strong.")
        break

# **6. Prime Numbers**
# Task: Write a Python program that prints all prime numbers between 1 and 100.

# > A prime number is a number greater than 1 that is not divisible by any number other than 1 and itself. Use nested loops to check divisibility.
prime = []
for i in range(2, 100):
        if not any(i % m == 0 for m in range(2, i)):
                prime.append(i)
print(prime)

# ---asd

# ### Bonus Challenge
# Task: Create a simple text-based Rock, Paper, Scissors game where the player plays against the computer.
# - The computer randomly chooses `rock`, `paper`, or `scissors` using `random.choice()`.
# - The player enters their choice.
# - Display the winner and keep track of scores for the player and the computer.
# - First to 5 points wins the match.
import random as r
yes2 = ['Y', 'YES', 'y', 'yes', 'ok']
lw = ['rock', 'scissors', 'paper']
while True:
    wc = 0
    wp = 0
    print("--- NEW MATCH: First to 5 points wins! ---")

    while wc < 5 and wp < 5:
        compchoice = r.choice(lw)
        playerch = input("Rock, Paper, Scissors: ").lower()
        if playerch not in lw:
            print("Invalid choice! Please type rock, paper, or scissors.")
            continue
            
        print(f"Computer chose: {compchoice}")
        if playerch == compchoice:
            print(f"Equal. \nComp = {wc} \nYou  = {wp}")
        elif (playerch == 'rock' and compchoice == 'scissors') or \
             (playerch == 'paper' and compchoice == 'rock') or \
             (playerch == 'scissors' and compchoice == 'paper'):
            wp += 1
            print(f"You won this round! \nComp = {wc} \nYou  = {wp}")
        else:
            wc += 1
            print(f"I won this round! \nComp = {wc} \nYou  = {wp}")
    if wc == 5:
        print('\nMATCH OVER: You lost the match! 😢')
    else:
        print('\nMATCH OVER: You won the match! 🎉')
    play2 = input('\nDo you want to play again? ')
    if play2 not in yes2:
        print("Thanks for playing!")
        break