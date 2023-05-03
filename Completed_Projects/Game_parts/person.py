class person:

    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight
    
    def NewWeight(self,weight):
        self.weight = weight
        print(f"{self.name}'s weight has been updated to {self.weight}kgs.")
    
    def Bmi(self):
        return round((float(self.weight)/(float(self.height)**2)), 2)

    def StandardToMetricHeight(height):
        h = height.split("'")
        feet = h[0]
        inches = h[1]
        inches = inches.rstrip('"')
        height = (float(feet) * 30.48) + (float(inches) * 2.54)
        height = round((height/100),2)
        return height

    def StandardToMetricWeight(weight):
        lbsPerKg = 0.45359237
        weight = round(float(weight) * lbsPerKg,2)
        return weight

firstname = input("What is your name? ")
#Height and units
while True:
    unit = input("[standard] units (\"Feet, Inches, Pounds\")\n[Metric] units (\"Centimeters, Kilograms\")\n------Pick One------\n[Standard] or [Metric] ---> ").lower()
    if unit == "standard":
        height = input("How tall are you? ")
        height = person.StandardToMetricHeight(height)
        break
    elif unit == "metric":
        while True:
            height = float(input("How tall are you in meters? "))
            if 0.9 > height or height > 2.5:
                print(f"Are you sure you height is correct and in meters ---> {height}")
                check = input(" ").lower()
                if check == "yes":
                    break
                else:
                    continue
            else:
                break
        break
    else:
        print("That is invalid. Please enter \"standard\" or \"metric\".")
        continue
#Weight
while True:
    if unit == "standard":
        weight = input("How much do you weight? ")
        weight = person.StandardToMetricWeight(weight)
        break
    elif unit == "metric":
        weight = input("How much do you weight? ")
        break
user = person(firstname, height, weight)
print(f"New user created\nWelcome {user.name}, your BMI as of today is {user.Bmi()}")



