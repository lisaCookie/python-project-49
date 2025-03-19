
def welcome_user():
    name = input("May I have your name? ")
    print(f'Hello, {name}!')
    return name


def ask_question(user_name, question, correct_answer, correct_answers):
    user_answer = input(f"Question: {question}\nYour answer: ").strip()
    
    try:
        user_answer = float(user_answer)  
        if user_answer == correct_answer:
            print('Correct!')
            correct_answers += 1  
            
            if correct_answers == 3:  
                print(f'Congratulations, {user_name}!')
                exit()  
            
            return correct_answers  
        else:
            print(f"{int(user_answer)} is the wrong answer ;(. Correct answer was '{correct_answer}'.")
            exit()  
    except ValueError:
        print("No, way!")
        exit()


def main():
    print('Welcome to the Brain Games!')


if __name__ == "__main__":
    main()
     