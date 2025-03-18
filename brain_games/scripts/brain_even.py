import random

from brain_games.cli import welcome_user


def is_even(number):
    return number % 2 == 0


def get_correct_answer(name_user):
    
    correct_answers = 0
    while correct_answers < 3:
        number = random.randint(1, 20)
        print(f'Question: {number}')
        user_answer = input("Your answer: ").strip().lower()

        if user_answer not in ['yes', 'no']:
            print('No, way!')
            return 

        correct_answer = 'yes' if is_even(number) else 'no'
        
        if user_answer == correct_answer:
            correct_answers += 1
            print('Correct!')
        elif user_answer == 'yes' != is_even(number):
            print(f"'yes' is wrong answer ;(. Correct answer was 'no'. Let's try again, {name_user}.")
            exit()
        else:
            return
        
    print(f'Congratulations, {name_user}.')


def main():

    print('Welcome to the Brain Games!')
    name_user = welcome_user()  
    print('Answer "yes" if the number is even, otherwise answer "no".')
    get_correct_answer(name_user)


if __name__ == '__main__':
    main()