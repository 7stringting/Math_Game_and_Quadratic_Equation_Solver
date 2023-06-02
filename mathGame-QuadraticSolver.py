# COMP2152 Assignment 2
# Made By Ali Al Aoraebi 101386021
# Michael Murphy
# Youtube Video: https://youtu.be/Ue8izQ8L4Os

import math
import random

# Part A
# check if score file exists, if not, set score to 0
file_path = "C:/Users/Alaa/PycharmProjects/pythonProject6/Score.txt"
try:
    with open(file_path, 'r') as f:
        score = int(f.read())
        print(f"I am happy to meet you again! Your last score was {score}!")
except FileNotFoundError:
    print("Welcome to your Math Game!")
except ValueError:
    score = 0
    print("Score file is empty. Starting a new game!")


# function to generate random question and get user's answer
def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])
    question = f"What is the result of {num1} {operator} {num2}?: "
    answer = eval(f"{num1} {operator} {num2}")
    return question, answer


# game loop
while True:
    question, answer = generate_question()
    user_answer = input(question)

    if str(answer) == user_answer.strip():
        print("Congratulations! You are Pro!")
        score += 1
    else:
        print(f"The correct answer is {answer}. Let's try another question :)")
        score -= 1

    # ask if user wants to continue
    continue_game = input("Type Y to continue, or any other character to calculate quadratic equations)")
    if continue_game.lower() != 'y':
        break
9
# write the final score to file
with open(file_path, "w") as f:
    f.write(str(score))

# Part B


def quadratic_equation():
    print("The Quadratic Equation is: ax^2 + bx + c = 0")
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))

    equation_str = f"Your Quadratic Equation is: {a}X^2 + {b}X + {c} = 0\n"

    discriminant = calculate_discriminant(a, b, c)

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        result_str = f"We got two real solutions, which are {x1:.2f}, and {x2:.2f}\n"
    elif discriminant == 0:
        x1 = -b / (2*a)
        result_str = f"We got one real solution, which is {x1:.2f}\n"
    else:
        result_str = "The Discriminant is negative, we got a pair of Complex solutions.\n"

    with open("QuadEqu.txt", "w") as f:
        f.write(equation_str)
        f.write(result_str)

    print(equation_str.strip())
    print(result_str.strip())


def calculate_discriminant(a, b, c):
    return b**2 - 4*a*c


quadratic_equation()

