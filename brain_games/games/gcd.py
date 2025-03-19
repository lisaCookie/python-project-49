import math
import random

from brain_games.games.engine import ask_question, main, welcome_user

main()


def generate_random_gcd_queries(
    num_queries: int, 
    min_value: int = 10, 
    max_value: int = 100
):
    queries = []

    for _ in range(num_queries):
        a = random.randint(min_value, max_value)
        b = random.randint(min_value, max_value)
        gcd_value = math.gcd(a, b)
        queries.append((a, b, gcd_value))

    return queries


def play_generate_gcd():
    num_queries = 10  
    min_value = 1     
    max_value = 20   

    queries = generate_random_gcd_queries(num_queries, min_value, max_value)

    user_name = welcome_user()  
    print('Find the greatest common divisor of given numbers.')

    correct_answers = 0  

    for a, b, correct_answer in queries: 
        question = f"{a} {b}"  
        correct_answers = ask_question(
            user_name, 
            question, 
            correct_answer, 
            correct_answers
        )


if __name__ == "__main__":
    play_generate_gcd()