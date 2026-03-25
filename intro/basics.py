# 1. count_digits: Returns the number of digits in a number
def count_digits(n):
    return len(abs(str))

# 2. count_words: Counts occurrences of each word in a string, ignoring commas and periods
def count_words(text):
    text = text.replace("," "").replace(".", "")
    word_count = {}
    for word in text.split():
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

# 3. even_squares: Returns squares of even numbers from a list
def even_squares(numbers):
    return list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))

# 4. students_avg_max: Prints average score for each student and finds the student with the highest single grade
def students_avg_max(students):
    students = {
        "Ivan": [10,9,6],
        "Anna": [10,7,12],
        "Alex": [7,7,2]
    }
    for name in students:
        avg = sum(students[name]) / len(students[name])
        print(name, "average:", avg)
    best_student = ""
    best_grade = 0
    for name in students:
        max_grade = max(students[name])
        if max_grade > best_grade:
            best_grade = max_grade
            best_student = name
    print("Best student is: ", best_student)

# 5. count_chars: Counts occurrences of each character in a string
def count_chars(word):
    result = {}
    for ch in word:
        if ch in result:
            result[ch] += 1
        else:
            result[ch] = 1
    return result

# 6. numbers_only: Returns a tuple containing only numbers from a mixed tuple
def numbers_only():
    data = (1,"Polo", 3, 5, "George")
    numbers = ()
    for instance in data:
        if type(instance) == int or type(instance) == float:
            numbers = numbers + (instance,)
    return numbers

# 7. sort_by_length: Returns list of strings sorted by their length
def sort_by_length(words):
    return sorted(words, key=len)

# 8. sort_employees: Sorts a list of employees by salary
def sort_employees():
    employees = [
        {"name": "Ivan", "position": "dev", "salary": 1000},
        {"name": "Anna", "position": "manager", "salary": 2000},
        {"name": "Oleg", "position": "tester", "salary": 1200}
    ]
    sorted_list = sorted(employees, key=lambda x: x["salary"])
    return sorted_list  

# 9. max_two: Returns the maximum of two numbers
max_two = lambda a,b: a if a > b else b

# 10. unique_elements: Returns unique elements from a list as a set
def unique_elements(lst):
    return set(lst)

# 11. sum_squares: Returns the sum of squares of numbers 1-10
def sum_squares():
    d = {}
    for i in range(1, 11):
        d[i] = i * i
    return sum(d.values())
print (sum_squares())

# 12. filter_numbers: Returns numbers greater than 10 and even from a list
def filter_numbers(numbers):
    result = []
    for num in numbers:
        if num > 10 and num % 2 == 0:
            result.append(num)
    return result

# 13. sum_tuple: Returns the sum of all numbers in a tuple
def sum_tuple(t):
    return sum(t)

# 14. is_positive: Checks if a number is positive
is_positive = lambda x: x > 0

# 15. older_people: Returns list of names of people older than given age
def older_people(people,age):
    return [name for name in people if people[name] > age]

# 16. min_max: Returns minimum and maximum from a tuple
def min_max(t):
    return min(t), max(t)

# 17. div_by_3: Returns numbers divisible by 3 from a list
def div_by_3(lst):
    return list(filter(lambda x: x % 3 == 0, lst))

# 18. char_index: Returns list of tuples (character, index) from a string
def char_index(s):
    result = []
    for i in range(len(s)):
        result.append((s[i], i))
    return result

# 19. limit_calls: Returns a wrapper that allows calling func at most n times
def limit_calls(func, n):
    count = 0
    def wrapper(*args):
        nonlocal count
        if count >= n:
            return "Limit exceeded"
        count += 1
        return func(*args)
    return wrapper

# 20. check_list: Returns a function that checks if a value is in the given list
def check_list(lst):
    def inner(x):
        return x in lst
    return inner

# 21. check_list: Duplicate: Returns a function that checks if a value is in the list
def check_list(lst):
    def inner(x):
        return x in lst
    return inner

# 22. formatter: Returns a function that formats a string according to the given template
def formatter(template):
    def inner(text):
        return template.format(text)
    return inner