from cryptography.fernet import Fernet
from password_gen import make_password

def write_key():#writes the enryption key.
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():#loads key to decrypt file.
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

def view():#displays a list of user names and passwords.
    with open("passwords.txt", "r") as f:
            for line in f.readlines():
                data = line.rstrip()
                user, pwd = data.split("|")
                print("User:", user, "| password:", fer.decrypt(pwd.encode()).decode())

def add():#adds a user name and either a personal or random password to file.
    pick = input("Do you want to make your own password? ").lower()
    if pick == "y" or pick == 'yes':
        while True:
            user = ''
            with open("passwords.txt", "a") as f:
                f.read
            with open("passwords.txt", "r") as f:
                for line in f.readlines():
                    data = line.rstrip()
                    user, pwd = data.split("|")
                name = input("Account Name: ").capitalize()
                if len(name) < 5:
                    print("PLease enter a longer Account Name!")
                    continue
                elif name == user:
                    print("That Account Name is already taken.")
                    continue
                break
        pwd = input("Password: ")
        with open("passwords.txt", "a") as f:
            f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
    else:
        while True:
            print('Random Password Generator')
            user = ''
            with open("passwords.txt", "a") as f:
                f.read
            with open("passwords.txt", "r") as f:
                for line in f.readlines():
                    data = line.rstrip()
                    user, pwd = data.split("|")
                name = input("Account Name: ").capitalize()
                if len(name) < 5:
                    print("PLease enter a longer Account Name!")
                    continue
                elif name == user:
                    print("That Account Name is already taken.")
                    continue
                break
        pwd = make_password()
        print(f'Password is: {pwd}')
        with open("passwords.txt", "a") as f:
            f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

def remove():#removes the user name and password from file.
    count = 3
    while True:
        new_lines = ""
        empty_list =[]
        if count == 0:
            break
        with open("passwords.txt", "r") as f:
                    for line in f.readlines():
                        data = line.rstrip()
                        user, pwd = data.split("|")
                        empty_list.append(user)
        print(empty_list)
        name = input("Account Name: ").capitalize()
        if len(name) < 3:
            print('Account Name too short.')
            count -= 1
            if count == 0:
                break
            continue
        elif name in empty_list:
            for i in empty_list:
                if name == i:
                    with open("passwords.txt", "r") as f:
                        lines  = f.readlines()
                        for line in lines:
                            if name not in line:
                                    new_lines += f"{line}"
                    with open("passwords.txt", "w") as f:
                        f.write(new_lines)
                        print(f'The {name} Account has been removed')
                        count = 0
        else:
            print('Accont Name not found')
            count -= 1
            continue
        
try:
    key = load_key()
    fer = Fernet(key)
    while True:
        mode = input("Would you like to add a new password, or veiw existing passwords (add, view, remove, or quit)? ").lower()
        if mode == "q" or mode == "quit":
            print("Closing password storage.\n")
            break
        if mode == "view":
            view()
        elif mode == "add":
            add()
        elif mode == "remove":
            remove()
        else:
            print("Invalid entry.")
            continue
except FileNotFoundError:
    write_key()