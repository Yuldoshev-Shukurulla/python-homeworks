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
            "task_id:": self.task_id,
            "title:": self.title,
            "description:": self.description,
            "due_date:": self.due_date,
            "status:": self.status
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
        pass
    
    def load_tasks(self, filename):
        pass


