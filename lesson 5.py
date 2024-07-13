# Task1
for number in range(1, 101):
    if number % 7 == 0:
        print(number)
# Task 2
summa = 0
count = 0
for number in range(1, 100):
    if number % 2 != 0:
        summa += number
        count += 1
print("Summa from 0 to 99:", summa)
print("Number of odd numbers from 1 to 99:", count)
# Task 3
i = 1
count = 0
while i <= 200:
    print(i, end=' ')
    count += 1
    if count == 5:
        print()
        count = 0
    i += 1
# Task 4
n = int(input("Enter number for factorial: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print("factorial number", n, "equals", factorial)
# Task 5
for i in range(1, 11):
    result = i * 5
    print(f"{i} x 5 = {result}")
# Task 6
height = int(input("Enter height: "))
width = int(input("Enter width: "))
for i in range(height):
    print('*' * width)
# Task 7
numbers = [0, 5, 2, 4, 7, 1, 3, 19]
count_odd = 0
for number in numbers:
    if number % 2 != 0:
        count_odd += 1
print("Number of odd numbers in the list:", count_odd)
# Task 8
import random
first_list = [random.randint(1, 100) for _ in range(4)]
second_list = first_list + [x * 2 for x in first_list]
print("First list:", first_list)
print("Second list:", second_list)
# Task 9
salaries = []
for month in range(1, 13):
    x = int(input(f"Enter your salary for month {month}: "))
    if x <= 0:
        print("Your salary cannot be zero or negative.")
        break
    salaries.append(x)
if len(salaries) == 12:
    average_salary = sum(salaries) / len(salaries)
    print(f"Your average salary over 12 months is: {average_salary:.2f}")
else:
    print("Salary input was interrupted.")
# Task 10
# Задаємо матрицю
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16] ]
print("Matrix:")
for row in matrix:
    print(row)
total_sum = sum(sum(row) for row in matrix)
print("Сума елементів матриці:", total_sum)
# Task 11
user_input = input("Enter numbers separated by commas: ")
original_list = [int(x) for x in user_input.split(",")]
reversed_list = original_list.copy()
reversed_list.reverse()
print("Original list:", original_list)
print("Reverse list:", reversed_list)