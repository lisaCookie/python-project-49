import random

from brain_games.games.engine import my_game


def is_even(number):
    return number % 2 == 0


def generate_question_and_answer():
    number = random.randint(1, 50)  
    question = str(number)  
    correct_answer = 'yes' if is_even(number) else 'no'
    return question, correct_answer


def play_even():

    def game():
        return generate_question_and_answer()
    
    print('Answer "yes" if the number is even, otherwise answer "no".')
    my_game(game)


if __name__ == '__main__': 
    play_even()


