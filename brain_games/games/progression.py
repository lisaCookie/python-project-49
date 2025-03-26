import random

from brain_games.games.engine import my_game


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
    def game():
        question, correct_answer = get_question_and_answer()
        return question, correct_answer

    print('What number is missing in the progression?')
    my_game(game)


if __name__ == "__main__":
    play_progression()
