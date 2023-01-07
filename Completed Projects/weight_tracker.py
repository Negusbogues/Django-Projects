#Weight tracking 
print("Welcome to your personal weight tracker.")
while True: 
    select = input('Would you like to view past Bio Data? ').lower()
    record = True
    weight_list = ''
    if select in 'yes':
        try:
            with open ("bio_data.txt", "r") as f:
                empty_user = []
                empty_weight = []
                empty_height = []
                for line in f.readlines():
                    data = line.rstrip()
                    user, weight, height = data.split("|")
                    empty_user.append(user)
                    empty_weight.append(weight)
                    empty_height.append(height)
                print(empty_user)
                count = 3
                while True:
                    selection = input('Which user\'s data would yu like to see? ').capitalize()
                    if len(selection) < 3:
                        print('Username must be longer than 3 characters long.')
                        continue
                    elif selection not in empty_user:
                        print('User not found.')
                        count -= 1
                        if count == 0:
                            print('Invalid entry.')
                            print('-----[Closing Bio Data Storage.]-----')
                            break
                        continue
                    for i in empty_user:
                        if selection == i:
                            pick = empty_user.index(i)
                            user = empty_user[pick]
                            weight = empty_weight[pick]
                            height = empty_height[pick]
                    display = input("Would you like to see results in standard or metric? ")
                    if display in 'standard':
                        k = 2.20462262185
                        weight = weight.split(",")
                        s_weight = round(float(weight[-1])*k) 
                        weight = weight[-1]
                        cm = 2.54
                        standard = (float(height)*100)/cm
                        feet = int(standard//12)
                        inches = round(standard%12)
                        s_height = f"{feet}'{inches}\""
                        print('-----[Latest Data]-----')
                        print(f"User: {user.capitalize()}| Weight: {s_weight}lbs| Height: {s_height}| BMI: " + str(round((float(weight)/(float(height)**2)), 2)))
                        print('-----[Closing Bio Data Storage.]-----')
                        break
                    else:
                        weight = weight.split(",")
                        weight = weight[-1]
                        print('-----[Latest Data]-----')
                        print(f"User: {user}| Weight: {weight}kg| Height: {height}m| BMI: " + str(round((float(weight)/(float(height)**2)), 2)))
                        print('-----[Closing Bio Data Storage.]-----')
                        break
        except FileNotFoundError:
            print("No Data Avalible.")
            pass
    while True:#user
        username = input("What is your username? ").capitalize()
        if len(username) < 3:
            print('Username must be longer than 3 characters.')
            continue
        with open ("bio_data.txt", "a") as f:
            f.read
        with open ("bio_data.txt", "r") as f:
            empty_user = []
            empty_weight = []
            empty_height = []
            for line in f.readlines():
                data = line.rstrip()
                user, weight, height = data.split("|")
                empty_user.append(user)
                empty_weight.append(weight)
                empty_height.append(height)
        for i in empty_user:
            if username == i:
                pick = empty_user.index(i)
                record = False
                height = empty_height[pick]
                weight_list += (empty_weight[pick])
        break
    while True:#weight
        raw_weight = input('What is your current weight? ')
        unit = input('Is that in pounds of kilograms? ').lower()
        if unit == 'pound' or unit == 'pounds' or unit == 'p':
            l = 0.45359237
            f_weight = str(round(float(raw_weight)* l,1))            
            print("You are " + f_weight +"kgs!")
            break
        elif unit == 'kilograms' or unit == "kilos" or unit == "k":
            k = 2.20462262185
            f_weight = raw_weight
            weight = round(float(f_weight)*k,1)
            print(f"That's about {weight}lbs.")
            break
        else:
            print('Please use a valid entry.')
            continue
    while record == True:#height
        try:
            raw_height = input("How tall are you?(ex. 6'1\" or 185) ")
            h_unit = input("Is that in feet and inches[f], or centimeters[cm]? ").lower()
            if h_unit == "f" or h_unit == 'feet':
                h = raw_height.split("'")
                feet = h[0]
                inches = h[1]
                inches = inches.rstrip('"')
                height = (float(feet) * 30.48) + (float(inches) * 2.54)
                f_height = round((height/100),2)
                print(f"You are {f_height}m tall!")
                break
            elif h_unit == 'cm' or h_unit == 'c':
                height = int(raw_height)
                f_height = round((height/100),2)
                print(f"You are {f_height}m tall!")
                break
            else:
                print('Please use a valid entry.')
                continue
        except IndexError:
            print("Please eneter height in the proper format [x'y\"]")
            continue
    empty_user = []
    empty_weight = []
    empty_height =[]
    new_lines = ''
    with open("bio_data.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, weight, height = data.split("|")
            empty_user.append(user)
            empty_weight.append(weight)
            empty_height.append(height)
    if username in empty_user:
        for i in empty_user:
            if username == i:
                with open("bio_data.txt", "r") as f:
                    lines  = f.readlines()
                    for line in lines:
                        if username not in line:
                            new_lines += f"{line}"
                with open("bio_data.txt", "w") as f:
                    f.write(new_lines)
    if len(weight_list) == 0:
        weight_list += f_weight
    else:
        weight_list += ","+(f_weight)
    weight_ = weight_list.split(",")
    for i in empty_user:
        if username == i:
            pick = empty_user.index(i)
            f_height = empty_height[pick]
    with open ("bio_data.txt", "a") as f: 
        f.write(username + "|" + str(weight_list[:]) + "|" + str(f_height) + "\n")
    display = input("Would you like to see results in standard or metric? ")
    if display in 'standard':
        k = 2.20462262185
        s_weight = round(float(weight_[-1])*k) 
        cm = 2.54
        standard = (float(f_height)*100)/cm
        feet = int(standard//12)
        inches = round(standard%12)
        s_height = f"{feet}'{inches}\""
        print(f"User: {username.capitalize()}| Weight: {s_weight}lbs| Height: {s_height}")
        if len(weight_)>=2:
            if float(weight_[-2]) > float(weight_[-1]):
                loss = float(weight_[-2])-float(weight_[-1])
                loss = (round(float(loss)*k, 1))
                print(f"You lost {loss}lbs")
            else:
                gain = round(float(weight_[-1])-float(weight_[-2]),1)
                gain = (round(float(gain)*k, 1))
                print(f"You gained {gain}lbs")
    else:
        print(f"User: {username}| Weight: {weight_[-1]}kg| Height: {height}m")
        if len(weight_)>=2:
            if float(weight_[-2])>float(weight_[-1]):
                loss = (round(float(weight_[-2])-float(weight_[-1]), 1))
                print(f"You lost {loss}kgs")
            else:
                gain = (round(float(weight_[-1])-float(weight_[-2]), 1))
                print(f"You gained {gain}kgs")
    bmi = round((float(weight_[-1])/(float(f_height)**2)), 2)
    print(f"Your current bmi is {bmi}")
    r = input("Is there anything else? ").lower()
    if r in "yes":#rerun program
        continue
    else:
        print('Have a good day.')
        break