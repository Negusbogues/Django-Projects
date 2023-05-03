import random
from string import ascii_letters
def make_password():
    while True:
        try:
            code = ''
            passcode = []
            Length = int(input('How long does your password need to be? '))
            Special = ["!","@","#","$","%","^","&","*","(",")","-","?"]
            while True:
                version = input('Are there any speacial characters(!,@,#)? [Y/N]').lower()
                if version == 'y':
                    for i in range(int(Length)):
                        if len(passcode) < (Length/3):
                            passcode.insert(random.randint(0, Length), random.choice(ascii_letters))
                        elif len(passcode) < ((Length/3)*2):
                            passcode.insert(random.randint(0, Length), (random.randint(0,10)))
                        else:
                            passcode.insert(random.randint(0, Length), random.choice(Special))
                    for i in passcode:
                        code = code + str(i)

                    return code
                elif version == 'n':
                    for i in range(int(Length)):
                        if len(passcode) < (Length/2):
                            passcode.insert(random.randint(0, Length), random.choice(ascii_letters))
                        else:
                            passcode.insert(random.randint(0, Length), (random.randint(0,10)))
                    for i in passcode:
                        code = code + str(i)

                    return code
                else:
                    print('Please enter Y or N.')
                    continue                
        except ValueError:
            print('Please enter a whole number.')
            continue