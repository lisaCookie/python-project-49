import random

from brain_games.games.engine import ask_question, main


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_question_and_answer():
    num = random.randint(1, 20)
    correct_answer = 'yes' if is_prime(num) else 'no'
    question = f'{num}'
    return question, correct_answer


def play_random_primes():
    user_name = main()  
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    
    correct_answers = 0  

    for _ in range(3):
        question, correct_answer = get_question_and_answer()
        
        def game():
            return question, correct_answer

        correct_answers += ask_question(game, user_name)
            
        if correct_answers == 3:
            print(f'Congratulations, {user_name}!')
            exit()


if __name__ == "__main__":
    play_random_primes()  







