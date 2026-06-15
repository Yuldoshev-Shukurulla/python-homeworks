# # ## Generalized `Vector` Class  

# # **Objective**: Create a Python class `Vector` that represents a mathematical vector in an n-dimensional space, capable of handling any number of dimensions.

# # ### **Task Description**

# # 1. **Create a `Vector` class** that represents a vector in an n-dimensional space.  
# #    - The class should support vectors of any number of dimensions, defined by an arbitrary number of components provided during initialization.

# # 2. The class should provide functionality to:
# #    - Perform vector operations such as addition, subtraction, and dot product.
# #    - Handle scalar multiplication.
# #    - Compute the magnitude (length) of the vector.
# #    - Normalize the vector (return the unit vector).

# # 3. The class should have methods for:
# #    - Representing the vector as a string for easy display.
# #    - Handling operations between vectors of the same dimension and raising appropriate errors when vectors of different dimensions are involved.

# # ### **Example Usage**
# # python
# # # Create vectors
# # v1 = Vector(1, 2, 3)
# # v2 = Vector(4, 5, 6)

# # # Print the vector
# # print(v1)          # Output: Vector(1, 2, 3)

# # # Addition
# # v3 = v1 + v2
# # print(v3)          # Output: Vector(5, 7, 9)

# # # Subtraction
# # v4 = v2 - v1
# # print(v4)          # Output: Vector(3, 3, 3)

# # # Dot product
# # dot_product = v1 * v2
# # print(dot_product) # Output: 32

# # # Scalar multiplication
# # v5 = 3 * v1
# # print(v5)          # Output: Vector(3, 6, 9)

# # # Magnitude
# # print(v1.magnitude())  # Output: 3.7416573867739413

# # # Normalization
# # v_unit = v1.normalize()
# # print(v_unit)      # Output: Vector(0.267, 0.534, 0.801)
import math

class Vector:
    def __init__(self, *components):
        self.components = tuple(components)

    def __len__(self):
        return len(self.components)

    def __str__(self):
        return f"Vector{self.components}"

    def __repr__(self):
        return str(self)

    def _check_dimensions(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimensions")

    def __add__(self, other):
        self._check_dimensions(other)
        return Vector(*(a + b for a, b in zip(self.components, other.components)))

    def __sub__(self, other):
        self._check_dimensions(other)
        return Vector(*(a - b for a, b in zip(self.components, other.components)))

    def __mul__(self, other):
        if isinstance(other, Vector):
            self._check_dimensions(other)
            return sum(a * b for a, b in zip(self.components, other.components))
        elif isinstance(other, (int, float)):
            return Vector(*(a * other for a in self.components))
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def magnitude(self):
        return math.sqrt(sum(a ** 2 for a in self.components))

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector")
        return Vector(*(round(a / mag, 3) for a in self.components))
# # ---

# # ## Employee Records Manager (OOP Version)
# # **Objective**: Create a program to manage employee records using classes and file handling.

# # ### **Tasks and Requirements**

# # 1. **Class Design**  
# #    - Create a class `Employee` to represent individual employees with the following attributes:
# #      - `employee_id`
# #      - `name`
# #      - `position`
# #      - `salary`
# #    - Create a class `EmployeeManager` to handle operations such as adding, viewing, searching, updating, and deleting employee records. This class will manage the file **"employees.txt"**.

# # 2. **File Handling**  
# #    - All employee records should be stored in **"employees.txt"**.  
# #    - Each operation (add, view, update, delete) should interact with the file to ensure data persistence.

# # 3. **Menu Options**  
# #    Implement a menu within the `EmployeeManager` class with the following options:
   
# #    1. Add new employee record
# #    2. View all employee records
# #    3. Search for an employee by Employee ID
# #    4. Update an employee's information
# #    5. Delete an employee record
# #    6. Exit
   

# # 4. **Functional Requirements**  
# #    - **Option 1**: Add a new employee by creating an `Employee` object and appending it to **"employees.txt"**.  
# #    - **Option 2**: Read all records from **"employees.txt"** and display them.  
# #    - **Option 3**: Search for an employee by **Employee ID** and display their details.  
# #    - **Option 4**: Update an employee's information (name, position, or salary) based on the Employee ID.  
# #    - **Option 5**: Delete an employee's record from the file using the Employee ID.  
# #    - **Option 6**: Exit the program.


# # ### **Example Usage**  
# # plaintext
# # Welcome to the Employee Records Manager!
# # 1. Add new employee record
# # 2. View all employee records
# # 3. Search for an employee by Employee ID
# # 4. Update an employee's information
# # 5. Delete an employee record
# # 6. Exit

# # Enter your choice: 1
# # Enter Employee ID: 1001
# # Enter Name: John Doe
# # Enter Position: Software Engineer
# # Enter Salary: 75000
# # Employee added successfully!

# # Enter your choice: 2
# # Employee Records:
# # 1001, John Doe, Software Engineer, 75000

# # Enter your choice: 3
# # Enter Employee ID to search: 1001
# # Employee Found:
# # 1001, John Doe, Software Engineer, 75000

# # Enter your choice: 6
# # Goodbye!


# # ### **Additional Instructions**
# # 1. Use the `Employee` class to encapsulate individual employee data and functionality (e.g., a `__str__` method for displaying employee details).  
# # 2. Use the `EmployeeManager` class for managing operations such as file handling, record searching, and updates.  
# # 3. Ensure your code is modular, with methods for each operation (e.g., `add_employee`, `view_all_employees`).  


# # ### **Bonus Challenge**
# # 1. Add validation to ensure unique Employee IDs.  
# # 2. Implement error handling for invalid inputs and file operations.  
# # 3. Allow users to sort employee records (e.g., by salary or name) before displaying them.  
import os

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = float(salary)

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {int(self.salary)}"


class EmployeeManager:
    def __init__(self, filename="employees.txt"):
        self.filename = filename
        self._init_file()

    def _init_file(self):
        if not os.path.exists(self.filename):
            with open(self.filename, "w", encoding="utf-8") as f:
                f.write("Employee ID, Name, Position, Salary\n")

    def _load_records(self):
        records = []
        if not os.path.exists(self.filename):
            return records
        with open(self.filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines[1:]:
                if line.strip():
                    parts = [p.strip() for p in line.split(",")]
                    if len(parts) == 4:
                        records.append(Employee(parts[0], parts[1], parts[2], parts[3]))
        return records

    def _save_records(self, records):
        with open(self.filename, "w", encoding="utf-8") as f:
            f.write("Employee ID, Name, Position, Salary\n")
            for emp in records:
                f.write(str(emp) + "\n")

    def add_employee(self):
        records = self._load_records()
        eid = input("Enter Employee ID: ").strip()
        
        if any(emp.employee_id == eid for emp in records):
            print("Error: Employee ID must be unique.")
            return

        name = input("Enter Name: ").strip()
        pos = input("Enter Position: ").strip()
        try:
            sal = float(input("Enter

# # ---

# # ## To-Do Application

# # **Objective**: Create a flexible To-Do application to manage tasks with support for different file storage formats (e.g., CSV, JSON). The application should be designed such that adding support for a new file format requires minimal changes to the code.


# # ### **Task Description**

# # #### 1. Functional Requirements:
# # Your To-Do application should provide the following features:
# # 1. **Add a task**: Allow users to add tasks with the following details:
# #    - `Task ID`
# #    - `Title`
# #    - `Description`
# #    - `Due Date` (optional)
# #    - `Status` (e.g., Pending, In Progress, Completed)
# # 2. **View tasks**: Display all tasks with their details.
# # 3. **Update a task**: Allow users to modify a task's details using its Task ID.
# # 4. **Delete a task**: Remove a task by its Task ID.
# # 5. **Filter tasks**: Filter tasks by status (e.g., Pending or Completed).
# # 6. **Save and load tasks**: Save tasks to a file and load them from the file on startup.

# # #### 2. Design Requirements:
# # 1. **Separation of Concerns**:
# # 2. **Support for Multiple Formats**:
# # 3. **Minimal Code Changes**:

# # #### 3. Example Usage:
# # plaintext
# # Welcome to the To-Do Application!
# # 1. Add a new task
# # 2. View all tasks
# # 3. Update a task
# # 4. Delete a task
# # 5. Filter tasks by status
# # 6. Save tasks
# # 7. Load tasks
# # 8. Exit

# # Enter your choice: 1
# # Enter Task ID: 101
# # Enter Title: Finish Homework
# # Enter Description: Complete math and science homework.
# # Enter Due Date (YYYY-MM-DD): 2024-12-31
# # Enter Status (Pending/In Progress/Completed): Pending
# # Task added successfully!

# # Enter your choice: 2
# # Tasks:
# # 101, Finish Homework, Complete math and science homework., 2024-12-31, Pending

# # ### **Deliverables**
# # 1. Python scripts with classes and methods implemented as described.
# # 2. Clear comments and documentation.
# # 3. A brief explanation of how you ensured minimal code changes when adding support for new file formats.
from abc import ABC, abstractmethod
import csv
import json
import os

class Task:
    """Represents a single task in the application."""
    def __init__(self, task_id, title, description, due_date="N/A", status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date if due_date else "N/A"
        self.status = status

    def to_dict(self):
        """Converts task attributes to a dictionary format."""
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data):
        """Creates a Task instance from a dictionary."""
        return cls(
            task_id=data["task_id"],
            title=data["title"],
            description=data["description"],
            due_date=data.get("due_date", "N/A"),
            status=data.get("status", "Pending")
        )

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"


class StorageStrategy(ABC):
    """Abstract Base Class serving as the contract for storage formats."""
    @abstractmethod
    def save_tasks(self, filename, tasks):
        pass

    @abstractmethod
    def load_tasks(self, filename):
        pass


class CSVStorage(StorageStrategy):
    """Handles persistent storage using CSV file format."""
    def save_tasks(self, filename, tasks):
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["task_id", "title", "description", "due_date", "status"])
            writer.writeheader()
            for task in tasks:
                writer.writerow(task.to_dict())

    def load_tasks(self, filename):
        tasks = []
        if not os.path.exists(filename):
            return tasks
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                tasks.append(Task.from_dict(row))
        return tasks


class JSONStorage(StorageStrategy):
    """Handles persistent storage using JSON file format."""
    def save_tasks(self, filename, tasks):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump([task.to_dict() for task in tasks], f, indent=4)

    def load_tasks(self, filename):
        if not os.path.exists(filename):
            return []
        with open(filename, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
                return [Task.from_dict(item) for item in data]
            except json.JSONDecodeError:
                return []


class TaskManager:
    """Manages business operations on tasks and utilizes a structural storage strategy."""
    def __init__(self, filename, storage_strategy: StorageStrategy):
        self.filename = filename
        self.storage = storage_strategy
        self.tasks = []
        self.load_from_file()

    def add_task(self, task):
        if any(t.task_id == task.task_id for t in self.tasks):
            print("Error: Task ID must be unique.")
            return False
        self.tasks.append(task)
        print("Task added successfully!")
        return True

    def view_tasks(self, task_list=None):
        target_list = task_list if task_list is not None else self.tasks
        if not target_list:
            print("No tasks found.")
            return
        print("\nTasks:")
        for task in target_list:
            print(task)

    def update_task(self, task_id):
        task = next((t for t in self.tasks if t.task_id == task_id), None)
        if not task:
            print("Task not found.")
            return
        
        print(f"Current details: {task}")
        new_title = input("Enter New Title (leave blank to keep current): ").strip()
        new_desc = input("Enter New Description (leave blank to keep current): ").strip()
        new_date = input("Enter New Due Date (YYYY-MM-DD, leave blank to keep current): ").strip()
        new_status = input("Enter New Status (Pending/In Progress/Completed, leave blank to keep current): ").strip()

        if new_title: task.title = new_title
        if new_desc: task.description = new_desc
        if new_date: task.due_date = new_date
        if new_status: task.status = new_status
        print("Task updated successfully!")

    def delete_task(self, task_id):
        initial_len = len(self.tasks)
        self.tasks = [t for t in self.tasks if t.task_id != task_id]
        if len(self.tasks) < initial_len:
            print("Task deleted successfully!")
        else:
            print("Task not found.")

    def filter_tasks_by_status(self, status):
        filtered = [t for t in self.tasks if t.status.lower() == status.lower()]
        self.view_tasks(filtered)

    def save_to_file(self):
        self.storage.save_tasks(self.filename, self.tasks)
        print(f"Tasks saved successfully to {self.filename}!")

    def load_from_file(self):
        self.tasks = self.storage.load_tasks(self.filename)


def main():
    print("Select Storage Format:\n1. CSV\n2. JSON")
    fmt_choice = input("Enter choice (1/2): ").strip()
    
    if fmt_choice == '2':
        manager = TaskManager("todo_tasks.json", JSONStorage())
    else:
        manager = TaskManager("todo_tasks.csv", CSVStorage())

    print("\nWelcome to the To-Do Application!")
    while True:
        print("\n1. Add a new task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Filter tasks by status")
        print("6. Save tasks")
        print("7. Load tasks")
        print("8. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            tid = input("Enter Task ID: ").strip()
            title = input("Enter Title: ").strip()
            desc = input("Enter Description: ").strip()
            date = input("Enter Due Date (YYYY-MM-DD): ").strip()
            status = input("Enter Status (Pending/In Progress/Completed): ").strip()
            if not status: status = "Pending"
            
            manager.add_task(Task(tid, title, desc, date, status))

        elif choice == '2':
            manager.view_tasks()

        elif choice == '3':
            tid = input("Enter Task ID to update: ").strip()
            manager.update_task(tid)

        elif choice == '4':
            tid = input("Enter Task ID to delete: ").strip()
            manager.delete_task(tid)

        elif choice == '5':
            status = input("Enter status to filter by (Pending/In Progress/Completed): ").strip()
            manager.filter_tasks_by_status(status)

        elif choice == '6':
            manager.save_to_file()

        elif choice == '7':
            manager.load_from_file()
            print("Tasks loaded from file.")

        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid alternative selection. Try again.")

if __name__ == "__main__":
    main()