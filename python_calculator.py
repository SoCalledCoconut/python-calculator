user_functions = ["Add", "Multiply", "Divide", "Subtract"]

def basic_input():
    num_prompt = float(input("Please enter a number: "))
    num_prompt_2 = float(input("Please enter another number: "))
    user_function = input("What woud you like to do? (Add/Multiply/Divide/Subtract) ")
    if user_function.capitalize() in user_functions:
        basic_calculation(user_function, num_prompt, num_prompt_2)
    else:
        print("I'm sorry, you've entered something incorrectly - try again!")
        return basic_input()

def basic_calculation(user_function, num_prompt, num_prompt_2):
    user_function = user_function.capitalize()
    if user_function == "Add":
        addition = float(num_prompt + num_prompt_2)
        print("The result of these two numbers added together is", addition)
    if user_function == "Multiply":
        multiply = float(num_prompt  * num_prompt_2)
        print("The result of these two numbers multiplied is ", multiply)
    if user_function == "Divide":
        divide = float(num_prompt / num_prompt_2)
        print("The result of these two numbers divided is", divide)
    if user_function == "Subtract":
        subtract = float(num_prompt - num_prompt_2)
        print("The result of these two numbers substracted is", subtract)
        
#defining functions and lists for ADVANCED choice
adv_functions = ["Power", "Square Root"]
import math

def adv_input():
    num_prompt = float(input("Please enter a number: "))
    num_prompt_2 = float(input("Please enter another number:\n(if you want to use the square root funtion, please enter '0'.)"))
    adv_function = input("What woud you like to do? (Power/Square Root) ")
    if adv_function.capitalize() in adv_functions:
        adv_calculation(adv_function, num_prompt, num_prompt_2)
    else:
        print("I'm sorry, you've entered something incorrectly - try again!")
        return adv_input()

def adv_calculation(adv_function, num_prompt, num_prompt_2):
        if adv_function.capitalize() == "Power":
            power = float(pow(num_prompt, num_prompt_2))
            print("The result of the first number to the power of the second number is", power)
        if adv_function.capitalize() == "Square Root":
            square = float(math.sqrt(num_prompt))
            print("The square root of ", num_prompt, " is ", square)

#defining functions for BMI calculation
def bmi_met():
    height_met = float(input("Please enter your height in centimetres: "))
    weight_met = float(input("Please enter your weight in kgs: "))
    bmi_met_res = (weight_met/(height_met*height_met))*10000

    if bmi_met_res <= 18.5:
        print("Your BMI is ", bmi_met_res, " which is considered underweight.")
    elif bmi_met_res <= 25:
        print("Your BMI is ", bmi_met_res, " which is considered healthy.")
    elif bmi_met_res <= 30:
        print("Your BMI is ", bmi_met_res, " which is considered overweight.")
    elif bmi_met_res >= 30.1:
        print("Your BMI is ", bmi_met_res, " which is considered obese.") 

def bmi_imp():
    height_imp = 2.205*float(input("Please enter your height in feet (use decimals): " ))
    weight_imp = 30.48*float(input("Please enter your weight in pounds: "))
    bmi_imp_res = weight_imp/(height_imp*height_imp)

    if bmi_imp_res <= 18.5:
        print("Your BMI is ", bmi_imp_res, " which is considered underweight.")
    elif bmi_imp_res <= 25:
        print("Your BMI is ", bmi_imp_res, " which is considered healthy.")
    elif bmi_imp_res <= 30:
        print("Your BMI is ", bmi_imp_res, " which is considered overweight.")
    elif bmi_imp_res >= 30.1:
        print("Your BMI is ", bmi_imp_res, " which is considered obese.")  


# CALCULATING CALORIES - added only for metric units
def calories(): 
    weight = float(input("Enter your weight(in kgs): "))
    height = float(input("Enter your height(in metres): "))
    age = int(input("Enter your age: "))
    gender = input("Enter your gender(M/F): ")

    # BEE stands for basal energy expenditure
    BEEm = 66.5 + (13.75 * weight) + (5.003 * height*100) - (6.775 * age) #for males
    BEEf = 655.1 + (9.563 * weight) + (1.850 * height*100) - (4.676 * age) #for females
    actlvl =  int(input("What is your activity level:\n1. Little or no exercise\n2. Light exercise/sports\n3. Medium exercise/sports\n4. Hard exercise/sports\n5. Intense exercise/sports\n"))

    actlvl_ratios = {1:1.2, 2:1.375, 3:1.55, 4:1.1725, 5:1.9} # a dict containing ratios to multiply with the respective BEE for calculating calories

    if gender.lower() == 'm':
        calorie_intake = BEEm * actlvl_ratios.get(actlvl)
        print(f"Your daily required calories is {calorie_intake}")
    elif gender.lower() == 'f':
        calorie_intake = BEEf * actlvl_ratios.get(actlvl)
        print(f"Your daily required calories is {calorie_intake}")
    else:
        print("Error: Invalid inputs!")
    



#defining functions for Mortgage calculation
def mort_calc():
    print("Please enter the following:\n")
    principal = float(input("Principal: £"))
    n_payment = float(input("Number of payments: "))
    interest = float(input("Interest rate: "))
    interest = (interest/100)/12

    mnth_payment = principal*((interest*pow((1+interest), n_payment))/(pow((1+interest), n_payment)-1))

    print("Monthly payment: ", mnth_payment)

#defining functions and lists for Trip calculation
def trip_calc():
    print("Please provide the following details: \n\n")
    distance = float(input("Distance in miles: "))
    fuel_effic = float(input("Fuel efficiency (mpg): "))
    litre_price = float(input("Price per litre: "))
    speed = float(input("Speed (m/h): "))

    while speed >= 60 and fuel_effic <= 0:
        fuel_effic = fuel_effic - (2*(speed-60))
    
    trip = (litre_price*4.5)*(distance/fuel_effic)
    time = distance/speed

    print("Your trip will take ", round(float(time), 2), "hours, and cost £", round(float(trip),2))

         
        


#Calculator Selection

def begin():
    print("WELCOME TO THE PYTHON CALCULATOR\n\nYOUR SELECTIONS:\nBasic (+, -, *, /)\nAdvanced (power, square root)\nBMI\nCalories\nMortgage\nTrip\n")
    selection = input("What type of Calculator would you like to use?: ")
    selection = selection.capitalize()
    if selection == "Basic":
        basic_input()
    elif selection == "Advanced":
        adv_input()
    elif selection.upper() == "BMI":
        imp_or_met = input("Do you prefer to use metric or imperial units? (Metric/Imperial): ")
        if imp_or_met.capitalize() == "Metric":
            bmi_met()
        elif imp_or_met.capitalize() == "Imperial":
            bmi_imp()
    elif selection == "Calories":
        calories()
    elif selection == "Mortgage":
        mort_calc()
    elif selection == "Trip":
        trip_calc()
    else:
        print("Invalid input!")


if __name__ == "__main__":
    begin()
    #restart calculator
    restart = input("Would you like to use the calculator again?\n1: Yes\n2: No\n")
    if restart == "1":
        begin()
    else:
        print("Thank you for using the calculator!")
