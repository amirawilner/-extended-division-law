#חוק הפילוג המורחב רמה קלה

import random
from sympy import symbols, expand, sympify

# create the symbols
x, y = symbols('x y')

def generate_problem():
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    c = random.randint(-10, 10)
    d = random.randint(-10, 10)
    problem_type = random.randint(1, 3)

    if problem_type == 1:
        problem_str = f"({x}+{a})({a}+{b})"
        solution = expand((x+a)*(a+b))
    elif problem_type == 2:
        problem_str = f"({a*x}+{b})({x}+{c})"
        solution = expand((a*x+b)*(x+c))
    else:
        problem_str = f"({a*x}+{b})({c*y}+{d})"
        solution = expand((a*x+b)*(c*y+d))
    
    return problem_str, solution

def format_solution(expression):
    # Get the string representation of the expression and remove the * sign
    return str(expression).replace('*', '')

def main():
    problems = []
    answers = []

    while True:
        problem, solution = generate_problem()
        print(f"Solve the following problem: {problem}")
        answer = input("Enter your answer (or 'quit' to exit): ")

        if answer.lower() == 'quit':
            break

        problems.append((problem, solution))

        try:
            user_solution = sympify(answer)
            is_correct = user_solution == solution
            answers.append(is_correct)
            solution_str = format_solution(solution)

            if is_correct:
                print("Your solution was correct!")
            else:
                print(f"Your solution was incorrect. The correct answer is {solution_str}")
        except:
            print("Invalid input. Please enter a valid algebraic expression.")
            answers.append(False)

    print("\nHere are the correct answers:")
    for (problem, solution), correct in zip(problems, answers):
        print(f"\nFor problem {problem}:")
        if correct:
            print("Your solution was correct!")
        else:
            solution_str = format_solution(solution)
            print(f"The correct answer is {solution_str}")

if __name__ == "__main__":
    main()

















