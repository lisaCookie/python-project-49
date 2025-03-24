import random

from brain_games.games.engine import ask_question, main


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def play_random_primes():
    user_name = main()  
    print('Answer "yes" if the given number is prime. Otherwise answer "no".')
    
    correct_answers = 0  

    for _ in range(3):
        num = random.randint(1, 20)  
        correct_answer = 'yes' if is_prime(num) else 'no'  
        
        correct_answers = ask_question(
            user_name, 
            num, 
            correct_answer, 
            correct_answers
        )  


if __name__ == "__main__":
    play_random_primes()  








