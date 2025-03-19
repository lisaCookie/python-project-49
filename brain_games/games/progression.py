import random
from brain_games.games.engine import ask_question, main, welcome_user

main()

def generate_arithmetic_progression(start, step, length):
    return [start + i * step for i in range(length)]

def play_progression():
    user_name = welcome_user()  
    print('What number is missing in the progression?')

    start = random.randint(1, 10)  
    step = random.randint(1, 5)     
    length = random.randint(5, 10)  
    
    progression = generate_arithmetic_progression(start, step, length)
    
    correct_answers = 0  

    for _ in range(3):  
        missing_index = random.randint(0, length - 1)  
        correct_answer = progression[missing_index]  
        progression[missing_index] = '..'  
        question = ' '.join(map(str, progression))  
        
        correct_answers = ask_question(user_name, question, correct_answer, correct_answers) 
        progression[missing_index] = correct_answer

if __name__ == "__main__":
    play_progression()