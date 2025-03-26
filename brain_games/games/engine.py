def welcome_user():
    name = input("May I have your name? ")
    print(f'Hello, {name}!')
    return name


def main():
    print('Welcome to the Brain Games!')


def ask_question(game, user_name):
    question, correct_answer = game() 
    user_answer = input(f"Question: {question}\nYour answer: ").strip()

    if user_answer.lower() == correct_answer.lower():
        print('Correct!')
        return True
    else:
        print(
            f"'{user_answer}' is the wrong answer ;(. "
            f"Correct answer was '{correct_answer}'.\n"
            f"Let's try again, {user_name}!"
        )
        return False 
    

main()
user_name = welcome_user()


def my_game(game):
    
    correct_answers = 0
    num_queries = 3  

    for _ in range(num_queries):
        if not ask_question(game, user_name):
            break 
        correct_answers += 1

    if correct_answers == num_queries:
        print(f'Congratulations, {user_name}!')


if __name__ == "__main__":
    user_name = main()