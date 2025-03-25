import random

from brain_games.games.engine import ask_question, main


def generate_expression():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])
    
    expression = f"{num1} {operator} {num2}"
    return expression, eval(expression)


def play_calculator_game():
    num_queries = 3  
    user_name = main()
    print('What is the result of the expression?')

    correct_answers = 0  

    for _ in range(num_queries):
        question, correct_answer = generate_expression()
        
        def game():
            return question, str(correct_answer)

        if ask_question(game, user_name):
            correct_answers += 1

        if correct_answers == num_queries:
            print(f'Congratulations, {user_name}!')
            exit()


if __name__ == "__main__":
    play_calculator_game()



