# # ### Zero Check Decorator

# # Write a decorator function called `check` that verifies that the denominator is not equal to 0 and apply it to the following function:

# # python
# # @check
# # def div(a, b):
# #    return a / b



# # input: div(6, 2)
# # output: 3



# # input: div(6, 0)
# # output: "Denominator can't be zero"
# def check(funk):
#     def wrapper(a, b):
#         if b == 0:
#             c = 'Denominator can\'t be zero'
#             return c
#         else:
#             return funk(a, b)
#     return wrapper
        
# @check
# def div(a, b):
#    return a / b

# r1 = div(6, 2)
# print(r1)
# r2 = div(6, 0)
# print(r2)

# # ---

# # ### **Employee Records Manager**
# # **Objective**: Create a program to manage employee records using file handling.  

# # **Tasks**:  
# # 1. **File Creation and Data Entry**  
# #    - Create a file named **"employees.txt"**.  
# #    - Allow the user to add new employee records. Each record should have the following fields:  
     
# #      Employee ID, Name, Position, Salary
     
# #      Example of a record:  
     
# #      1001, John Doe, Software Engineer, 75000
# file = open('employees.txt', mode = 'w')
# file.write('Employee ID, Name, Position, Salary\n1001, John Doe, Software Engineer, 75000')
# file.close()
# # 2. **Menu Options**  
# #    Your program should present the following options:  
   
# #    1. Add new employee record
# #    2. View all employee records
# #    3. Search for an employee by Employee ID
# #    4. Update an employee's information
# #    5. Delete an employee record
# #    6. Exit
   

# # 3. **Functional Requirements**  
# #    - **Option 1**: Append a new employee record to **"employees.txt"**.  
# #    - **Option 2**: Display all employee records from **"employees.txt"**.  
# #    - **Option 3**: Allow the user to search for an employee by **Employee ID** and display their details.  
# #    - **Option 4**: Update an employee’s information (name, position, or salary) based on the Employee ID.  
# #    - **Option 5**: Delete an employee's record from the file using the Employee ID.  
# #    - **Option 6**: Exit the program. 

# import os

# def load_data():
#     if not os.path.exists("employees.txt"):
#         with open("employees.txt", "w") as f:
#             f.write("Employee ID, Name, Position, Salary\n")
#         return []
    
#     with open("employees.txt", "r") as f:
#         lines = f.readlines()
#         return [line.strip().split(", ") for line in lines[1:] if line.strip()]

# def save_data(data):
#     with open("employees.txt", "w") as f:
#         f.write("Employee ID, Name, Position, Salary\n")
#         for record in data:
#             f.write(", ".join(record) + "\n")

# while True:
#     print("\n1. Add new employee record\n2. View all employee records\n3. Search by ID\n4. Update employee info\n5. Delete employee record\n6. Exit")
#     choice = input("Select an option: ")

#     if choice == '1':
#         eid = input("Enter ID: ")
#         name = input("Enter Name: ")
#         pos = input("Enter Position: ")
#         sal = input("Enter Salary: ")
#         with open("employees.txt", "a") as f:
#             f.write(f"{eid}, {name}, {pos}, {sal}\n")
    
#     elif choice == '2':
#         data = load_data()
#         for row in data:
#             print(row)
            
#     elif choice == '3':
#         search_id = input("Enter ID to search: ")
#         data = load_data()
#         emp = next((x for x in data if x[0] == search_id), None)
#         print(emp if emp else "Employee not found.")

#     elif choice == '4':
#         update_id = input("Enter ID to update: ")
#         data = load_data()
#         found = False
#         for i, row in enumerate(data):
#             if row[0] == update_id:
#                 data[i][1] = input("New Name: ")
#                 data[i][2] = input("New Position: ")
#                 data[i][3] = input("New Salary: ")
#                 found = True
#                 break
#         if found:
#             save_data(data)
#             print("Updated.")
#         else:
#             print("ID not found.")

#     elif choice == '5':
#         del_id = input("Enter ID to delete: ")
#         data = load_data()
#         new_data = [x for x in data if x[0] != del_id]
#         if len(new_data) < len(data):
#             save_data(new_data)
#             print("Deleted.")
#         else:
#             print("ID not found.")

#     elif choice == '6':
#         break
# # ---

# # ### **Word Frequency Counter**
# # **Objective**: Analyze a text file and count how often each word appears.  

# # **Tasks**:  
# # 1. **File Input**  
# #    - Use the file **"sample.txt"**. The file can contain any text (like a paragraph or an article).  
# #    - If **"sample.txt"** does not exist, prompt the user to create it by typing in a paragraph.  

# # 2. **Count Word Frequency**  
# #    - Read the file content and split it into individual words.  
# #    - Count the frequency of each word (ignore capitalization, e.g., "The" and "the" should be counted as the same word).  
# #    - Ignore punctuation (like commas, periods, etc.).  

# # 3. **Output**  
# #    - Display the total number of words in the file.  
# #    - Display the top 5 most common words with their counts.  
# #    - Save the output to a new file called **"word_count_report.txt"**.  

# # 4. **Example Output**  
# #    **Content of sample.txt**:  
   
# #    This is a simple file.
# #    This file, is for testing purposes. It is a test file.
   

# #    **Console Output**:  
   
# #    Total words: 14
# #    Top 5 most common words:
# #    is - 3 times
# #    this - 2 times
# #    file - 3 times
# #    a - 2 times
# #    test - 1 time
   

# #    **Content of word_count_report.txt**:  
   
# #    Word Count Report
# #    Total Words: 14
# #    Top 5 Words:
# #    is - 3
# #    file - 3
# #    this - 2
# #    a - 2
# #    test - 1
   import os

file_name = "sample.txt"

if not os.path.exists(file_name):
    print(f"'{file_name}' topilmadi.")
    user_text = input("Iltimos, fayl yaratish uchun biror matn kiriting:\n")
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(user_text)

with open(file_name, "r", encoding="utf-8") as f:
    text = f.read()

punctuation = [".", ",", "!", "?", ";", ":", "-", "(", ")", "\n"]
cleaned_text = text.lower()

for char in punctuation:
    cleaned_text = cleaned_text.replace(char, " ")

words = [word for word in cleaned_text.split(" ") if word != ""]
total_words = len(words)

word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
top_5 = sorted_words[:5]

print(f"\nTotal words: {total_words}")
print("Top 5 most common words:")
for word, count in top_5:
    times_word = "time" if count == 1 else "times"
    print(f"{word} - {count} {times_word}")

report_name = "word_count_report.txt"
with open(report_name, "w", encoding="utf-8") as report:
    report.write("Word Count Report\n")
    report.write(f"Total Words: {total_words}\n")
    report.write("Top 5 Words:\n")
    for word, count in top_5:
        report.write(f"{word} - {count}\n")

# # **Bonus Task**:  
# # - Allow the user to specify how many "top common words" to display (e.g., top 3, top 10, etc.).  
# # - Make sure the program ignores case, punctuation, and handles large files efficiently.
import os

file_name = "sample.txt"

if not os.path.exists(file_name):
    user_text = input("Iltimos, fayl yaratish uchun biror matn kiriting:\n")
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(user_text)

try:
    top_n = int(input("Nechta eng ko'p o'qiladigan so'zlarni ko'rmoqchisiz? (masalan: 3, 5, 10): "))
    if top_n <= 0:
        top_n = 5
except ValueError:
    top_n = 5

punctuation = [".", ",", "!", "?", ";", ":", "-", "(", ")", "\n"]
word_counts = {}
total_words = 0

with open(file_name, "r", encoding="utf-8") as f:
    for line in f:
        cleaned_line = line.lower()
        for char in punctuation:
            cleaned_line = cleaned_line.replace(char, " ")
        
        for word in cleaned_line.split(" "):
            if word != "":
                total_words += 1
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1

sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
top_common = sorted_words[:top_n]

print(f"\nTotal words: {total_words}")
print(f"Top {len(top_common)} most common words:")
for word, count in top_common:
    times_word = "time" if count == 1 else "times"
    print(f"{word} - {count} {times_word}")

report_name = "word_count_report.txt"
with open(report_name, "w", encoding="utf-8") as report:
    report.write("Word Count Report\n")
    report.write(f"Total Words: {total_words}\n")
    report.write(f"Top {len(top_common)} Words:\n")
    for word, count in top_common:
        report.write(f"{word} - {count}\n")