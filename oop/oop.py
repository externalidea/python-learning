# -----------------------------
# 1. Book class
# -----------------------------
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # Accessors (getters)
    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_pages(self):
        return self.pages

    # Info method
    def info(self):
        return f"Book: '{self.title}', Author: {self.author}, Pages: {self.pages}"

    # Check if pages > 300
    def is_large(self):
        return self.pages > 300


# -----------------------------
# 2. Caching decorator
# -----------------------------
def cache_method(func):
    cache = {}

    def wrapper(self, *args):
        key = (func.__name__, args)
        if key in cache:
            print("Returning cached result")
            return cache[key]
        result = func(self, *args)
        cache[key] = result
        return result

    return wrapper


# -----------------------------
# 3. Book + Library classes
# -----------------------------
class Library:
    def __init__(self):
        self.books = []

    # Add book (operator +)
    def __add__(self, book: Book):
        self.books.append(book)
        return self

    # Remove book by id (operator -)
    def __sub__(self, book_id: int):
        self.books = [b for b in self.books if getattr(b, "id", None) != book_id]
        return self

    # Search by title
    def search_by_title(self, title):
        for b in self.books:
            if b.title.lower() == title.lower():
                return b.info()
        return None


# -----------------------------
# 4. Student + StudentDatabase
# -----------------------------
import json

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def average_grade(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0

class StudentDatabase:
    def __init__(self, filename="students.json"):
        self.filename = filename

    # Add student to file
    def add_student(self, student: Student):
        students = self.load_students()
        students.append({
            "name": student.name,
            "age": student.age,
            "grades": student.grades
        })
        with open(self.filename, "w") as f:
            json.dump(students, f)

    # Load students from file
    def load_students(self):
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    # Find student by name
    def find_student(self, name):
        students = self.load_students()
        for s in students:
            if s["name"].lower() == name.lower():
                return s
        return None


# -----------------------------
# Example usage
# -----------------------------
if __name__ == "__main__":
    # 1. Book
    b1 = Book("War and Peace", "Leo Tolstoy", 1225)
    b2 = Book("Python Basics", "John Doe", 200)
    print(b1.info(), "Large:", b1.is_large())
    print(b2.info(), "Large:", b2.is_large())

    # 3. Library
    lib = Library()
    lib + b1 + b2
    print(lib.search_by_title("Python Basics"))
    lib - getattr(b1, "id", 0)  # remove b1 by id if set

    # 4. Student DB
    db = StudentDatabase()
    s1 = Student("Alice", 20, [9, 10, 8])
    s2 = Student("Bob", 21, [7, 6, 9])
    db.add_student(s1)
    db.add_student(s2)
    print(db.load_students())
    print(db.find_student("Alice"))