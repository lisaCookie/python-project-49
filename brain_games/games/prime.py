import random

from brain_games.games.engine import my_game


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_question_and_answer():
    number = random.randint(1, 20)
    question = str(number)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return question, correct_answer


def play_random_primes():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    def game():
        return generate_question_and_answer()

    my_game(game)


if __name__ == "__main__":
    play_random_primes()










