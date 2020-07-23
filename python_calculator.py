

# defining functions and lists for BASIC choice
user_functions = ["Add", "Multiply", "Divide", "Subtract"]

def basic_input():
    num_prompt = float(input("Please enter a number: "))
    num_prompt_2 = float(input("Please enter another number: "))
    user_function = input("What woud you like to do? (Add/Multiply/Divide/Subtract) ")
    if user_function in user_functions:
        basic_calculation(user_function, num_prompt, num_prompt_2)
    else:
        print("I'm sorry, you've entered something incorrectly - try again!")
        return basic_input()

def basic_calculation(user_function, num_prompt, num_prompt_2):
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
            print("The result of these two numbers divided is", subtract)
        
#defining functions and lists for ADVANCED choice
adv_functions = ["Power", "Square Root"]
import math

def adv_input():
    num_prompt = float(input("Please enter a number: "))
    num_prompt_2 = float(input("Please enter another number:\n(if you want to use the square root funtion, please enter '0'.)"))
    adv_function = input("What woud you like to do? (Power/Square Root) ")
    if adv_function in adv_functions:
        adv_calculation(adv_function, num_prompt, num_prompt_2)
    else:
        print("I'm sorry, you've entered something incorrectly - try again!")
        return adv_input()

def adv_calculation(adv_function, num_prompt, num_prompt_2):
        if adv_function == "Power":
            power = float(pow(num_prompt, num_prompt_2))
            print("The result of the first number to the power of the second number is", power)
        if adv_function == "Square Root":
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
    print("WELCOME TO THE PYTHON CALCULATOR\n\nYOUR SELECTIONS:\nBasic (+, -, *, /)\nAdvanced (power, square root)\nBMI\nMortgage\nTrip\n")
    selection = input("What type of Calculator would you like to use? (NB: Case sensitive): ")

    if selection == "Basic":
        basic_input()
    if selection == "Advanced":
        adv_input()
    if selection == "BMI":
        imp_or_met = input("Do you prefer to use metric or imperial units? (Metric/Imperial): ")
        if imp_or_met == "Metric":
            bmi_met()
        elif imp_or_met == "Imperial":
            bmi_imp()
    if selection == "Mortgage":
        mort_calc()
    if selection == "Trip":
        trip_calc()

begin()
#restart calculator
restart = input("Would you like to use the calculator again?\n1: Yes, 2: No\n")
if restart == "1":
    begin()
else:
    print("Thank you for using the calculator!")