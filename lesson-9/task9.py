# # #### Task 1: Create a Library Management System with Custom Exceptions
# # 1. Create a Python program to manage a small library system. 
# # 2. Define custom exceptions for specific scenarios:
# #    - **`BookNotFoundException`**: Raised when trying to borrow a book that doesn’t exist in the library.
# #    - **`BookAlreadyBorrowedException`**: Raised when a book is already borrowed.
# #    - **`MemberLimitExceededException`**: Raised when a member tries to borrow more books than allowed.
# # 3. Implement classes for:
# #    - **`Book`**: Attributes include `title`, `author`, and `is_borrowed`.
# #    - **`Member`**: Attributes include `name`, `borrowed_books` (limit to 3 books per member).
# #    - **`Library`**: Manages books and members, including borrowing and returning books.
# # 4. Test your program with the following scenarios:
# #    - Adding books and members.
# #    - Borrowing and returning books.
# #    - Handling exceptions when rules are violated.

# class BookNotFoundException(Exception):
#     pass

# class BookAlreadyBorrowedException(Exception):
#     pass

# class MemberLimitExceededException(Exception):
#     pass

# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         self.is_borrowed = False

# class Member:
#     def __init__(self, name):
#         self.name  = name
#         self.borrowed_books = []

# class Library:
#     def __init__(self):
#         self.books = {}
#         self.members = {}
#     def add_book(self, book):
#         self.books[book.title] = book

#     def add_member(self, member):
#         self.members[member.name] = member

#     def borrow_book(self, member_name, book_title):
#         if book_title not in self.books:
#             raise BookNotFoundException(f'There is no book named {book_title} in the library.')
#         if self.books[book_title].is_borrowed:
#             raise BookAlreadyBorrowedException(f'{book_title} is already borrowed.')
#         if len(self.members[member_name].borrowed_books) >= 3:
#             raise MemberLimitExceededException('You have already borrowed three books.')
#         self.books[book_title].is_borrowed = True
#         self.members[member_name].borrowed_books.append(book_title)
#         print(f'"{book_title}" has been successfully borrowed by {member_name}.')
    
#     def return_book(self, member_name, book_title):
#         self.books[book_title].is_borrowed = False
#         self.members[member_name].borrowed_books.remove(book_title)
#         print(f'"{book_title}" has been successfully returned by {member_name}.')
# if __name__ == "__main__":
#     library = Library()

#     b1 = Book("O'tkan kunlar", "Abdulla Qodiriy")
#     b2 = Book("Sariq devni minib", "Xudoyberdi To'xtaboyev")
#     b3 = Book("Yulduzli tunlar", "Pirimqul Qodirov")
#     b4 = Book("Dunyoning ishlari", "O'tkir Hoshimov")

#     library.add_book(b1)
#     library.add_book(b2)
#     library.add_book(b3)
#     library.add_book(b4)

#     m1 = Member("Anvar")
#     library.add_member(m1)

#     try:
#         library.borrow_book("Anvar", "O'tkan kunlar")
#         library.borrow_book("Anvar", "O'tkan kunlar")
        
#     except BookNotFoundException as e:
#         print(f"Xatolik: {e}")
#     except BookAlreadyBorrowedException as e:
#         print(f"Xatolik: {e}")
#     except MemberLimitExceededException as e:
#         print(f"Xatolik: {e}")

# # ---

# # #### Task 2: Student Grades Management
# # 1. Create a CSV file named `grades.csv` with the following structure:
# #    csv
# #    Name,Subject,Grade
# #    Alice,Math,85
# #    Bob,Science,78
# #    Carol,Math,92
# #    Dave,History,74
   
# # 2. Write a Python program to:
# #    - Read data from `grades.csv` and store it in an appropriate data structure (e.g., a list of dictionaries).
# #    - Calculate the average grade for each subject.
# #    - Write a new CSV file named `average_grades.csv` with the following structure:
# #      csv
# #      Subject,Average Grade
# #      Math,88.5
# #      Science,78
# #      History,74
     
# # 3. Use the `csv` module for reading and writing the CSV files.
# import os
# import csv
# os.chdir('C:\\a62ab832e6d116c5594b4b3659421f\sh\python-homeworks\lesson-9')
# column = ['Name', 'Subject', 'Grade']
# columns =[['Alice', 'Math', '85'], ['Bob', 'Science', '78'], ['Carol', 'Math', '92'], ['Dave', 'History', '74']]
# with open('grades.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(column)
#     writer.writerows(columns)

# with open('grades.csv', 'r') as f:
#     rows = csv.DictReader(f)
#     rowd = [a for a in rows]

# subjects = list(set([rowd[i]['Subject'] for i in range(len(rowd))]))
# column1 = ['Subject', 'Average Grade']
# subdict = {i : [] for i in subjects}
# for i in range(len(rowd)):
#     (subdict[rowd[i]['Subject']]).append(int(rowd[i]['Grade']))
# average = {}
# for i, a in subdict.items():
#     average[i] = sum(a)/len(a)
# avlist = [[i,a] for i,a in average.items()]
# with open('average_grades.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(column1)
#     writer.writerows(avlist)


# # ---

# # ### **Task 3: JSON Handling**

# # #### **Load and Save Tasks (JSON)**
# # 1. Create a JSON file named `tasks.json` with the following structure:
# #    json
# #    [
# #        {"id": 1, "task": "Do laundry", "completed": false, "priority": 3},
# #        {"id": 2, "task": "Buy groceries", "completed": true, "priority": 2},
# #        {"id": 3, "task": "Finish homework", "completed": false, "priority": 1}
# #    ]
   
# # 2. Write a Python program to:
# #    - Load the tasks from `tasks.json`.
# #    - Display all tasks with the following fields: ID, Task Name, Completed Status, Priority.
# #    - Save any changes back to the `tasks.json` file (e.g., after modifying a task).

# # #### **Calculate Task Completion Stats**
# # 1. Write a Python function to calculate the following statistics:
# #    - **Total tasks**: Count the total number of tasks.
# #    - **Completed tasks**: Count the number of completed tasks.
# #    - **Pending tasks**: Count the number of tasks that are not completed.
# #    - **Average priority**: Calculate the average priority level of all tasks.
   
# #    Display these statistics after loading the tasks.

# # #### **Convert JSON Data to CSV**
# # 1. Write a function to convert the task data in `tasks.json` to a CSV file named `tasks.csv`. The CSV should have the following columns:
# #    - ID
# #    - Task Name
# #    - Completed Status
# #    - Priority

# #    For example:
# #    csv
# #    ID,Task,Completed,Priority
# #    1,Do laundry,False,3
# #    2,Buy groceries,True,2
# #    3,Finish homework,False,1

# import json
# import csv
# import os

# JSON_FILE = 'tasks.json'
# CSV_FILE = 'tasks.csv'

# def initialize_json_file():
#     """Dastlabki json fayli mavjud bo'lmasa, uni yaratib oladi."""
#     initial_data = [
#         {"id": 1, "task": "Do laundry", "completed": False, "priority": 3},
#         {"id": 2, "task": "Buy groceries", "completed": True, "priority": 2},
#         {"id": 3, "task": "Finish homework", "completed": False, "priority": 1}
#     ]
#     if not os.path.exists(JSON_FILE):
#         with open(JSON_FILE, 'w', encoding='utf-8') as f:
#             json.dump(initial_data, f, indent=4)
#         print(f"--> {JSON_FILE} muvaffaqiyatli yaratildi.")

# def load_tasks():
#     """JSON fayldan ma'lumotlarni o'qiydi."""
#     try:
#         with open(JSON_FILE, 'r', encoding='utf-8') as f:
#             return json.load(f)
#     except (json.JSONDecodeError, FileNotFoundError):
#         print("Xatolik: JSON faylni o'qib bo'lmadi.")
#         return []

# def save_tasks(tasks):
#     """O'zgarishlarni JSON faylga saqlaydi."""
#     with open(JSON_FILE, 'w', encoding='utf-8') as f:
#         json.dump(tasks, f, indent=4)
#     print("--> O'zgarishlar JSON faylga saqlandi.")

# def display_tasks(tasks):
#     """Vazifalarni terminalda chiroyli jadval ko'rinishida chiqaradi."""
#     print("\n" + "="*60)
#     print(f"{'ID':<5} | {'Task Name':<20} | {'Completed':<10} | {'Priority':<8}")
#     print("="*60)
#     for task in tasks:
#         status = "True" if task['completed'] else "False"
#         print(f"{task['id']:<5} | {task['task']:<20} | {status:<10} | {task['priority']:<8}")
#     print("="*60)

# def calculate_stats(tasks):
#     """Vazifalar bo'yicha statistikani hisoblaydi."""
#     if not tasks:
#         print("Statistika hisoblash uchun vazifalar mavjud emas.")
#         return

#     total_tasks = len(tasks)
#     # List comprehension yordamida hisoblash
#     completed_tasks = sum(1 for task in tasks if task['completed'])
#     pending_tasks = total_tasks - completed_tasks
#     avg_priority = sum(task['priority'] for task in tasks) / total_tasks

#     print("\n--- TASK STATISTICS ---")
#     print(f"Total tasks: {total_tasks}")
#     print(f"Completed tasks: {completed_tasks}")
#     print(f"Pending tasks: {pending_tasks}")
#     print(f"Average priority: {avg_priority:.2f}")
#     print("-" * 23)

# def convert_json_to_csv(tasks):
#     """JSON ma'lumotlarini CSV fayliga o'giradi."""
#     if not tasks:
#         print("CSV ga o'tkazish uchun ma'lumot yo'q.")
#         return

#     headers = ['ID', 'Task', 'Completed', 'Priority']
    
#     try:
#         with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
#             writer = csv.writer(f)
#             # Sarlavhani yozamiz
#             writer.writerow(headers)
            
#             # Qatorlarni mos ravishda yozamiz
#             for task in tasks:
#                 writer.writerow([task['id'], task['task'], task['completed'], task['priority']])
#         print(f"--> Ma'lumotlar {CSV_FILE} fayliga muvaffaqiyatli o'tkazildi.")
#     except Exception as e:
#         print(f"CSV faylga yozishda xatolik yuz berdi: {e}")

# def main():
#     initialize_json_file()

#     tasks = load_tasks()

#     print("\n[Dastlabki yuklangan vazifalar]:")
#     display_tasks(tasks)

#     calculate_stats(tasks)

#     print("\n--- O'zgartirish kiritish jarayoni ---")
#     if tasks:
#         tasks[0]['completed'] = True 
#         print(f"ID {tasks[0]['id']} vazifa holati 'True' ga o'zgartirildi.")
        
#         save_tasks(tasks)
        
#         print("\n[Yangilangan vazifalar]:")
#         display_tasks(tasks)

#     print("\n--- CSV formatga o'tkazish ---")
#     convert_json_to_csv(tasks)

# if __name__ == "__main__":
#     main()