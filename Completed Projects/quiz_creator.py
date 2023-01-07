import random

def lock_write():#register login
    empty_list = []
    with open('login.txt', 'r') as f:
        f.read
    with open("login.txt", "r") as f:
             for line in f.readlines():
                data = line.rstrip()
                username, password = data.split("|")
                empty_list.append(username)
    if len(empty_list) == 0:
        with open('login.txt', "w") as f:
            username = input('Register Username: ')
            password = input('Register Password: ')
            f.write(username + "|" + password)
    else:
        lock()

def lock():#login for sensitive data
    empty_list = []
    count = 1
    with open("login.txt", "r") as f:
             for line in f.readlines():
                data = line.rstrip()
                username, password = data.split("|")
                empty_list.append(username)
    if len(empty_list) == 0:
        lock_write()
    else:
        while True:
            inputuser = input('Enter your Username: ')
            inputpass = input('Enter your Password: ')
            if count == 0:
                print("Username or Password was incorrect!")
                exit()
            elif not (username == inputuser and password == inputpass):
                print('Username or Password does not match!')
                count -= 1
                continue
            else:
                break            

def view():#displays a list quizzes, their questions, and answers. Or scores logged for each quiz.
    view = input('Would you like to view quizzes or scores? ').lower()
    empty_list =[]
    if view == 'quizzes' or view == 'quiz':
        with open("quizzes.txt", "r") as f:
            for line in f.readlines():
                data = line.rstrip()
                names, questions, answers = data.split("|")
                questions = questions.split(",")
                answers = answers.split(",")
                key =dict(zip(questions,answers))
                print("Quiz Title:", names, "| Answer key:", key)
    elif view == 'scores' or view == 'score':
        with open("quiz_score.txt", "r") as f:
            for line in f.readlines():
                data = line.rstrip()
                quiz_title, username, score = data.split("|")
                if quiz_title not in empty_list:
                    empty_list.append(quiz_title)
        print(empty_list)
        quiz = input('Which quiz would you like to see the scores for? ').capitalize()
        if quiz in empty_list:
            with open("quiz_score.txt", "r") as f:
                for line in f.readlines():
                    data = line.rstrip()
                    quiz_title, username, score = data.split("|")
                    if quiz == quiz_title:
                        print("Quiz Title: ", quiz_title.capitalize(), "| User: ", username.capitalize(), "\n| Score: ", score + "%")
        else:
            print('Invalid selection.')
    else:
        print('Please use a valid entry.')

def add():#adds a new quiz to the file
    pick = input("Do you want to make your own quiz? ").lower()
    if pick == "y" or pick == 'yes':
        try:        
            while True:
                names = []
                questions = []
                answers = []
                with open("quizzes.txt", "a") as f:
                    f.read
                with open("quizzes.txt", "r") as f:
                    for line in f.readlines():
                        data = line.rstrip()
                        name, question, answer = data.split("|")
                        names.append(name)
                        
                    name = input("Quiz Title: ").capitalize()
                    if len(name) < 3:
                        print("PLease enter a longer Name!")
                        continue
                    elif name in names:
                        print("That Name is already taken.")
                        continue
                    break
            num_of_questions = int(input('How many questions will there be ? '))
            q_list = []
            a_list = []
            q__list = ''
            a__list = ''
            while num_of_questions > 0:
                quest = input("\n" + "Question? ").capitalize()
                ans = input("\n" + "Answer: ")
                q_list.append(quest)
                a_list.append(ans)
                num_of_questions -= 1
                q__list = ','.join(q_list)
                a__list = ','.join(a_list)
            with open("quizzes.txt", "a+") as f:
                f.write(f'\n{name}|{q__list}|{a__list}')

        except ValueError:
            print("Invalid Input!")
    else:
        take()

def remove():# removes quiz from the file
    count = 2
    while True:
        new_lines = ""
        empty_list =[]
        if count == 0:
            break
        with open("quizzes.txt", "r") as f:
                    for line in f.readlines():
                        data = line.rstrip()
                        names, questions, answers = data.split("|")
                        empty_list.append(names)
        print(empty_list)
        name = input("Quiz title: ")
        if len(name) < 3:
            print('Quiz title too short.')
            count -= 1
            continue
        if (name or name.capitalize()) in empty_list:
            for i in empty_list:
                if name == i:
                    with open("quizzes.txt", "r") as f:
                        lines  = f.readlines()
                        for line in lines:
                            if name not in line:
                                    new_lines += f"{line}"
                    with open("quizzes.txt", "w") as f:
                        f.write(new_lines)
                        print(f'The {name} Account has been removed')
                        count = 0
        elif count == 0:
            break
        else:
            print('Account Name not found')
            count -= 1
            continue
        
def take():#loads a pre-made quiz
    playing = input('Are you ready? ').lower()
    points = 0
    empty_list = []
    if playing == 'yes' or playing == 'y':
        print("Ok let's begin.")
        try:
            while True:
                with open("quizzes.txt", "r") as f:
                            for line in f.readlines():
                                data = line.rstrip()
                                names, questions, answers = data.split("|")
                                empty_list.append(names)
                print(f'Quiz titles: {empty_list}')
                quiz = input("Which quiz would you like to use? ").capitalize()
                username = input("What is your Username? ")
                if quiz in empty_list:
                    for i in empty_list:
                        if quiz == i:
                            with open("quizzes.txt", "r") as f:
                                lines = f.readlines()
                                for line in lines:
                                    if quiz in line:
                                        data = line.rstrip()
                                        names, questions, answers = data.split("|")
                else:
                    print("Quiz not available")
                    break
                q_list = questions.split(",")
                a_list = answers.split(",")
                v = len(q_list)
                pairs = dict(zip(q_list, a_list))
                x = 1
                while v > 0:
                        pick = random.randint(0, len(q_list) -1)
                        y = q_list[pick]
                        print(f'\nQuestion #{x}: {y.capitalize()}?')
                        answer = input('Answer: ').lower()
                        if answer == pairs[y]:
                            points += 1
                        del q_list[pick]
                        v -= 1 
                        x += 1
                break
        finally:
            try:
                print("Total correct : " + str(points) + "\n" + f"{username.capitalize()} got " + str(round(((points/len(a_list))* 100), 2)) + "% right!") 
                store = input('Would you like to save your score?').lower()
                if store == 'yes' or 'y':
                    score = str(round(((points/len(a_list))* 100), 2))
                    with open("quiz_score.txt", "a") as f:
                        f.write(quiz + "|" + username + "|" + score + "\n")
                retake = input("Would you like to retake the quiz? ")
                if retake == "yes" or retake == "y":
                    take()
            except ZeroDivisionError:
                print("You cant use the value 0!")   
            except UnboundLocalError:
                print("0% Correct.")  
                    
    else: 
        print("Come back when you're ready")
    
try:
    while True:
        mode = input("Would you like to create a new quiz, or view existing quizzes (add, view, remove, take, or quit)? ").lower()
        if mode == "q" or mode == "quit":
            print("Closing quiz creator.\n")
            break
        if mode == "view":
            view()
        elif mode == "add":
            add()
        elif mode == "remove":
            remove()
        elif mode == "take":
            take()
        else:
            print("Invalid entry.")
            continue
except FileNotFoundError:
    write_key()