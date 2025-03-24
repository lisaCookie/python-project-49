
def welcome_user():
    name = input("May I have your name? ")
    print(f'Hello, {name}!')
    return name


def ask_question(user_name, question, correct_answer, correct_answers):
    user_answer = input(f"Question: {question}\nYour answer: ").strip()
    
    if isinstance(correct_answer, (int, float)):
        try:
            user_answer_float = float(user_answer)  
            if user_answer_float == correct_answer:
                print('Correct!')
                correct_answers += 1
                
                if correct_answers == 3:
                    print(f'Congratulations, {user_name}!')
                    exit()  
                
                return correct_answers  
            else:
                print(
                    f"'{int(user_answer_float)}' is the wrong answer ;(. "
                    f"Correct answer was '{correct_answer}'.\n"
                    f"Let's try again, {user_name}!"
                )
                exit()  
        except ValueError:
            print("No, way!")  
            exit() 
    else:
        try:
            if user_answer == correct_answer:
                print('Correct!')
                correct_answers += 1
            
                if correct_answers == 3:
                    print(f'Congratulations, {user_name}!')
                    exit()  
            
                return correct_answers  
            else:
                print(
                    f"'{user_answer}' is the wrong answer ;(. "
                    f"Correct answer was '{correct_answer}'.\n"
                    f"Let's try again, {user_name}!"
                )
                exit()
        except ValueError:
            print("No, way!")  
            exit()


def main():
    print('Welcome to the Brain Games!')
    return welcome_user()


if __name__ == "__main__":
    main() 