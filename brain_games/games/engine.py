
def welcome_user():
    name = input("May I have your name? ")
    print(f'Hello, {name}!')
    return name


def ask_question(game):
    question, correct_answer = game() 
    user_answer = input(f"Question: {question}\nYour answer: ").strip()

    if isinstance(correct_answer, (int, float)):
        user_answer_float = float(user_answer)
        if user_answer_float == correct_answer:
            print('Correct!')
            return True
    else:
        if user_answer.lower() == correct_answer.lower():
            print('Correct!')
            return True
    
    print(
        f"'{user_answer}' is the wrong answer ;(. "
        f"Correct answer was '{correct_answer}'."
    )
    exit()


def main():
    print('Welcome to the Brain Games!')
    return welcome_user()


if __name__ == "__main__":
    main() 