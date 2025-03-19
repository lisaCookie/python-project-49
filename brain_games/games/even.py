import random

from brain_games.games.engine import main, welcome_user

main()


def is_even(number):
    return number % 2 == 0


def play_even():
    user_name = welcome_user()  
    print('Answer "yes" if the number is even, otherwise answer "no".')
    
    correct_answers = 0
    while correct_answers < 3:
        number = random.randint(1, 20)
        print(f'Question: {number}')
        user_answer = input("Your answer: ").strip().lower()

        if user_answer not in ['yes', 'no']:
            print('No, way!')
            exit()  

        correct_answer = 'yes' if is_even(number) else 'no'
        
        if user_answer == correct_answer:
            correct_answers += 1
            print('Correct!')
        else:
            print(
                f"'{user_answer}' is the wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.\n"
                f"Let's try again, {user_name}!"
            )
            return 
        
    print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    play_even()