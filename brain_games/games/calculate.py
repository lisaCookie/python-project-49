import random

from brain_games.games.engine import ask_question, main, welcome_user

main()


def generate_expression():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])
    
    expression = f"{num1} {operator} {num2}"
    return expression, eval(expression)


def play_calculator_game():
    user_name = welcome_user()  
    print('What is the result of the expression?')

    correct_answers = 0  

    for _ in range(3):  
        question, correct_answer = generate_expression()
        correct_answers = ask_question(user_name, question, correct_answer, correct_answers) 
            

if __name__ == "__main__":
    play_calculator_game()
