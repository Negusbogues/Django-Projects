#weight conversion tool
class Kg():
#convert kilograms to pounds
    def __init__(self,val):
        self.res = val

    def c(self):
            k = 2.20462262185
            res = round(self.res*k,2)            
            print("You are " + str(res) +"lbs!")

class Lb():
#convert pounds to kilograms
    def __init__(self,val):
        self.res = val

    def c(self):
        l = 0.45359237
        res = round(self.res*l,2)            
        print("You are " + str(res) +"kgs!")

print("\nThis is your personal weight conversion calculator.")
converter_is_on = True
while converter_is_on == True:
    print('You can enter "Q" or "Quit" to close the weight conversion calculator.')
    weight = input("Is your weight in Pounds[P] or Kilograms[K]? ")
    pound_list = ["P","POUNDS","POUND","#"]
    kilo_list = ["K","KILOGRAMS","KILOS","KILO","KILOGRAM"]
    quit_list = ["Q","QUIT","END","STOP"]
    if weight.upper() in pound_list:
        while True:
            try:    
                result = Lb(float(input("How many Pounds do you weight? ")))
                result.c()
                again = input("Is that all? [Y]/[N]")
                if again.upper() == "Y":
                    print("""
Until next time...""")
                    converter_is_on = False
                    break
                elif again.upper() == "N":
                    break
                else:
                    print("Please enter [Y] or [N] next time. Goodbye!")
                    converter_is_on = False
                    break

            except ValueError:
                print("Please enter a number")
                continue
    elif weight.upper() in kilo_list:
        while converter_is_on == True:
            try:    
                result = Kg(float(input("How many Kilograms do you weight? ")))
                result.c()
                again = input("Is that all? [Y]/[N]")
                if again.upper() == "Y":
                    print("""
Until next time...""")
                    converter_is_on = False
                    break
                elif again.upper() == "N":
                    break
                else:
                    print("Please enter [Y] or [N] next time. Goodbye!")
                    converter_is_on = False
                    break

            except ValueError:
                print("Please enter a number")
                continue
    elif weight.upper() in quit_list:
        print("""
Shutting down the weight conversion calcultor

Until next time...
        """)
        converter_is_on = False
        break
    else:
        print("""
Please enter a [P] for Pound, a [K] for Kilogram, or you can press [Q] to Quit
""")