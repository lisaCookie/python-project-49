import random

from brain_games.games.engine import my_game


def generate_expression():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])
    
    expression = f"{num1} {operator} {num2}"
    correct_answer = str(eval(expression)) 
    return expression, correct_answer


def play_calculator_game():
    
    def game():
        question, correct_answer = generate_expression()
        return question, correct_answer
    
    print('What is the result of the expression?')
    my_game(game)
   

if __name__ == "__main__":
    play_calculator_game()