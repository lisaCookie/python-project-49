import math
import random

from brain_games.games.engine import my_game


def generate_random_gcd_queries(num_queries: int, min_value: int = 10, 
                                    max_value: int = 100):
    queries = []
    for _ in range(num_queries):
        a = random.randint(min_value, max_value)
        b = random.randint(min_value, max_value)
        queries.append((a, b))
    return queries


def get_question_and_answer(a, b):
    question = f"{a} {b}"
    correct_answer = str(math.gcd(a, b))
    return question, correct_answer


def play_generate_gcd():
    print('Find the greatest common divisor of given numbers.')
    num_queries = 3  
    min_value = 1     
    max_value = 20   

    queries = generate_random_gcd_queries(num_queries, min_value, max_value)
    
    def game():
        for a, b in queries:
            return get_question_and_answer(a, b)
    
    my_game(game)


if __name__ == "__main__":
    play_generate_gcd()


