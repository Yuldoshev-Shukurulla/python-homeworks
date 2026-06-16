# Generalized Vector Class
# import math

# class Vector:
#     def __init__(self, *args):
#         self.components = args
    
#     def __len__(self):
#         return len(self.components)
    
#     def _check_dimensions(self, other):
#         if len(self) != len(other):
#             raise ValueError("Vectors must have the same dimensions")
    
#     def __str__(self):
#         return f'Vector{self.components}'
    
#     def __add__(self, other):
#         self._check_dimensions(other)
#         return Vector(*(a+b for a,b in zip(self.components, other.components)))
    
#     def __sub__(self, other):
#         self._check_dimensions(other)
#         return Vector(*(a-b for a,b in zip(self.components, other.components)))
    
#     def __mul__(self, other):
#         if isinstance(other, Vector):
#             self._check_dimensions(other)
#             return sum(a*b for a, b in zip(self.components, other.components))
#         elif isinstance(other, (int, float)):
#             return Vector(*(a * other for a in self.components))
#         else: 
#             return NotImplemented
        
#     def __rmul__(self, other):
#         return Vector.__mul__(self, other)
    
#     def magnitude(self):
#         return math.sqrt(sum(a**2 for a in self.components))
    
#     def normalize(self):
#         return Vector(*(round(a / Vector.magnitude(self), 3) for a in self.components))


# v1 = Vector(1, 2, 3)
# v2 = Vector(4, 5, 6)
# v3 = v1 + v2
# print(v3)
# v4 = v2 - v1
# print(v4) 
# dot_product = v1 * v2
# print(dot_product) 
# v5 = 3 * v1
# print(v5)  
# print(v1.magnitude())
# v_unit = v1.normalize()
# print(v_unit)

## To-Do Application
from abc import ABC, abstractmethod
import csv
import json
import os

os.chdir('C:\\a62ab832e6d116c5594b4b3659421f\sh\python-homeworks\lesson-7')

class Task:
    def __init__(self, task_id, title, description, due_date = "N\A", status = "Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date if due_date else "N\A"
        self.status = status
    
    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            task_id = data['task_id'],
            title = data['title'],
            description = data['description'],
            due_date = data['due_date'],
            status  =data['status']
            )
    
    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"
    

class StorageStrategy(ABC):
    @abstractmethod
    def save_tasks(self, filename, tasks):
        pass

    @abstractmethod
    def load_tasks(self, filename):
        pass

class CSVStorage(StorageStrategy):
    def save_tasks(self, filename, tasks):
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['task_id', 'title', 'description', 'due_date', 'status'])
            writer.writeheader()
            for task in tasks:
                writer.writerow(task.to_dict())
            
    def load_tasks(self, filename):
        tasks  = []
        if not os.path.exists(filename):
            return tasks
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                tasks.append(Task.from_dict(row))
        return tasks
class JSONStorage(StorageStrategy):
    def save_tasks(self, filename, tasks):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump([task.to_dict() for task in tasks], f, indent = 4)
    
    def load_tasks(self, filename):
        if not os.path.exists(filename):
            return []
        with open(filename, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
                return[Task.from_dict(task) for task in data]
            except json.JSONDecodeError:
                return []

class TaskManager:
    def __init__(self, filename, storage_strategy: StorageStrategy):
        self.filename = filename
        self.storage = storage_strategy
        self.tasks = []
        self.load_from_file()
    
    def add_task(self, task):
        if any(t.task_id == task.task_id for t in self.tasks):
            print('Task ID must be unique.')
            return False
        self.tasks.append(task)
        print('Task added succesfully')
        return True
    
    def view_tasks(self,task_list=None):
        target_list = task_list if task_list is not None else self.tasks
        if not target_list:
            print('No tasks found.')
            return
        print('\nTasks:')
        for task in target_list:
            print(task)
        
    def update_task(self, task_id):
        task = next((t for t in self.tasks if t.task_id  == task_id), None)
        if not task:
            print('Task not found.')
            return
        
        print(f'Current details: {task}')
        new_title = input('Enter new title (leave blank to keep current): ').split()
        new_description = input('Enter new description (leave blank to keep current): ').split()
        new_due_date = input('Enter new due date (leave blank to keep current): ').split()
        new_status = input('Enter new status (leave blank to keep current): ').split()
        
        if new_title: task.title = new_title
        if new_description: task.description = new_description
        if new_due_date: task.due_date = new_due_date
        if new_status: task.status = new_status
        print('Updated succesfully.')

    def delete_task(self, task_id):
        initial_len = len(self.tasks)
        self.tasks = [t  for t in self.tasks if t.task_id != task_id]
        if len(self.tasks) <initial_len:
            print('Task deleted succesfully')
        else:
            print('Task not found')
    
    def filter_tasks_by_status(self, status):
        filtered = [t for t in self.tasks if t.status.lower() == status.lower()]
        self.view_tasks(filtered)

    def save_to_file(self):
        self.storage.save_tasks(self.filename, self.tasks)
        print(f'Tasks saved to {self.filename}.')
    
    def load_from_file(self):
        self.tasks = self.storage.load_tasks(self.filename)

def main():
        print('Select storage format: \n1. CSV\n2.JSON')
        fmt_choice = input('Enter choice: ')
        if fmt_choice == '2':
            manager = TaskManager('todo_tasks.json', JSONStorage())
        else:
            manager = TaskManager('todo_tasks.csv', CSVStorage())

        print('Welcome to the To-Do Application!')
        while True:
            print('''Choose your choice:
                    1. Add a new task
                    2. View all tasks
                    3. Update a task
                    4. Delete a task
                    5. Filter tasks by status
                    6. Save tasks
                    7. Load tasks
                    8. Exit''')
            
            choice = input('Enter your choice: ')

            if choice == '1':
                tid = input('EEnter Task ID: ').strip()
                title = input('Enter Title: ').strip()
                desc = input('Enter Description:: ').strip()
                due = input('Enter Due Date (YYYY-MM-DD): ').strip()
                status = input('Enter Status (Pending/In Progress/Completed): ').strip()
                if not status: status = 'Pending'

                manager.add_task(Task(tid, title, desc, due, status))

            elif choice == '2':
                manager.view_tasks()
            
            elif choice == '3':
                tid = input('Enter task ID you want to update: ').strip()
                manager.update_task(tid)
            
            elif choice == '4':
                tid = input('Enter a task ID you want to delete: ').strip()
                manager.delete_task(tid)

            elif choice == '5':
                status_input = input('Enter status to filter (Pending/In Progress/Completed): ').strip()
                manager.filter_tasks_by_status(status_input)
            
            elif choice == '6':
                manager.save_to_file()
            
            elif choice == '7':
                manager.load_from_file()
            
            elif choice == '8':
                print("Goodbye!")
                break
            else:
                print("Invalid alternative selection. Try again.")

if __name__ == "__main__":
    main()

        
    



