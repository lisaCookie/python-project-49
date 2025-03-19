import random

from brain_games.games.engine import main, welcome_user

main()


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def ask_question(user_name, question, correct_answer):
    while True:
        user_answer = input(
            f"Question: {question}\nYour answer: "
        ).strip().lower()
        
        if user_answer in ['yes', 'no']:
            return user_answer
        else:
            print('No, way!')
            exit()


def play_random_primes():
    user_name = welcome_user()  
    print('Answer "yes" if the given number is prime. Otherwise answer "no".')
    
    correct_answers = 0  

    for _ in range(3):
        num = random.randint(1, 20)  
        correct_answer = 'yes' if is_prime(num) else 'no'  
        
        user_answer = ask_question(user_name, num, correct_answer)  
        
        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(
                f"'{(user_answer)}' is the wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.\n"
                f"Let's try again, {user_name}!"
            )
            exit()
    print(f"Congratulations, {user_name}!")


if __name__ == "__main__":
    play_random_primes()









