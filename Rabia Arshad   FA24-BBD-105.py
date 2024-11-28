
# Question 1: Simple Function
from datetime import datetime

def greet_with_time(name):
    current_time = datetime.now().time()
    print(f"Hello, {name}! The current time is {current_time}.")

greet_with_time("rabia arshad")
# Expected Output: Hello, rabia arshad! The current time is <current_time>

# Question 2: Function with Multiple Parameters
def calculate_average(num1, num2, num3):
    return (num1 + num2 + num3) / 3

average = calculate_average(10, 20, 30)
print(average)  # Expected Output: 20.0

# Question 3: Keyword Arguments
def print_info(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

# Example usage
print_info(name="rabia arshad", age=18, city="Lahore")
# Expected Output: Name: rabia arshad, Age: 18, City: Lahore

# Question 4: Variable-Length Arguments
def find_max(numbers):
    return max(numbers)

# Example usage
maximum = find_max([10, 20, 30, 5, 100])
print(maximum)  # Expected Output: 100

# Question 5: Recursive Function
def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case

# Example usage
result = factorial(5)
print(result)  # Expected Output: 120

# Question 6: Function as an Argument
def apply_function(func, numbers):
    return [func(num) for num in numbers]

# Example usage
result = apply_function(lambda x: x * 2, [1, 2, 3, 4])
print(result)  # Expected Output: [2, 4, 6, 8]

# Question 7: Lambda Function
square = lambda x: x ** 2

# Example usage
result = square(5)
print(result)  # Expected Output: 25

# Question 8: Higher-Order Function
def apply_operation(func, numbers):
    return [func(num) for num in numbers]

# Example usage
result = apply_operation(lambda x: x ** 2, [1, 2, 3, 4])
print(result)  # Expected Output: [1, 4, 9, 16]

# Question 9: Function Decorators
import time

def measure_time(func):
    def wrapper():
        start_time = time.time()
        func()  # Call the original function
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.4f} seconds")
    return wrapper

def say_hello():
    time.sleep(2)  # Simulating a delay of 2 seconds

# Applying the decorator manually
say_hello = measure_time(say_hello)

say_hello()
# Expected Output: Execution time: 2.0010 seconds (approximately)
