import random

from brain_games.games.engine import ask_question, main


def is_even(number):
    return number % 2 == 0


def play_even():
    user_name = main()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    
    correct_answers = 0

    for _ in range(3):
        number = random.randint(1, 50)  
        question = number  
        correct_answer = 'yes' if is_even(number) else 'no'  

        def game():
            return question, correct_answer  

        if ask_question(game): 
            correct_answers += 1
            
            if correct_answers == 3:
                print(f'Congratulations, {user_name}!')
                exit()


if __name__ == '__main__': 
    play_even()