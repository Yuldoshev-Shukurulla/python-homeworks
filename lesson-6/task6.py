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
# os.chdir('C:\\a62ab832e6d116c5594b4b3659421f\sh\python-homeworks\lesson-6')
# def load_data():
#     if not os.path.exists('employees.txt'):
#         with open('employees.txt', mode = 'w') as f:
#             f.write('Employee ID, Name, Position, Salary\n')
#         return []
#     else: 
#         with open('employees.txt', 'r') as f:
#             lines = f.readlines()
#             return [line.strip().split(', ') for line in lines[1:] if line.strip()]
# def save_data(data):
#         with open('employees.txt', mode = 'w') as f:
#             f.write('Employee ID, Name, Position, Salary\n')
#             for record in data:
#                  f.write(', '.join(record) + '\n')

# while True:
#     print("\n1. Add new employee record\n2. View all employee records\n3. Search by ID\n4. Update employee info\n5. Delete employee record\n6. Exit")
#     choice = input("Select an option: ")
     
#     if choice == '1':
#          eid = input('Enter employee id: ')
#          data = load_data()
#          for x in data:
#               if x[0] == eid:
#                    print('There is an employee with this id.')
#                    break
#               else:
#                     name = input('Enter employee name: ')
#                     pos = input('Enter employee position: ')
#                     salary = input('Enter employee salary: ')
#                     with open('employees.txt', 'a') as f:
#                         f.write(f'{eid}, {name}, {pos}, {salary}\n')

#     elif choice == '2':
#          data = load_data()
#          for row in data:
#               print(row) 
#     elif choice == '3':
#          searchid = input('Enter employee id: ')
#          data = load_data()
#          emp = next((x for x in data if x[0] == searchid), None)
#          print(emp if emp else 'Employee not found.')
#     elif choice == '4':
#          upd = input('Enter employee id you want to update: ')
#          data = load_data()
#          update = False
#          for i, row in enumerate(data):
#               if row[0] == upd:
#                    data[i][1] = input('New Name: ')
#                    data[i][2] = input('New position: ')
#                    data[i][3] = input('New salary: ')
#                    update = True
#                    break
#          if update:
#              save_data(data)
#              print('Updated succesfully')
#          else:
#              print('Employee not found.')
#     elif choice == '5':
#          idd = input('Enter ID you want to delete: ')
#          data = load_data()
#          new_data = [x for x in data if x[0] != idd]
#          if len(new_data) < len(data):
#               save_data(new_data)
#               print('Deleted.')
#          else:
#               print('Employee not found.')   
#     elif choice == '6':
#          break      
         



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
   

# # **Bonus Task**:  
# # - Allow the user to specify how many "top common words" to display (e.g., top 3, top 10, etc.).  
# # - Make sure the program ignores case, punctuation, and handles large files efficiently. 