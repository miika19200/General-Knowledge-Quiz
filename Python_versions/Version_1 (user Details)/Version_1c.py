#User Details
#Using fuctions to greet the user
def greet():#using def function so i can use mutiple times without repeating
    global name#so name outside of def can be used
    while True: #using while True loop
        name = input("What is your name? : ")#ask user to input their name
        if name.replace(' ','').isalpha():#isaplha is used to track errors
            break#breaks loop
        print("Please enter only A-Z characters only")

                  
greet()#calling function
print("Hello!",name)
#Asking user to enter their age 
def age():#using def function so i can use mutiple times without repeating
    while True:#using while True loop
        age=input("How old are you? : ")#ask user to input their age
        if age.replace(' ','').isnumeric():#isnumeric is used to track errors
            break#breaks loop
        print("this is not a valid data type, please enter only numbers.")
age()#calling function
