import random

from brain_games.games.engine import ask_question, main


def generate_progression():
    start = random.randint(1, 10)
    step = random.randint(1, 10)
    length = 10
    progression = [start + step * i for i in range(length)]
    return progression


def get_question_and_answer():
    progression = generate_progression()
    hid_index = random.randint(0, len(progression) - 1)
    correct_answer = progression[hid_index]
    progression[hid_index] = '..'
    question = ' '.join(map(str, progression))
    return question, str(correct_answer)


def play_progression():
    user_name = main()
    print('What number is missing in the progression?')

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
    play_progression()