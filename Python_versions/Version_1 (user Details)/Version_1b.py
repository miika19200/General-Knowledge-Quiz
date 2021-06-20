#User Details
#Using fuctions to greet the user
def greet():#using def function so i can use mutiple times without repeating
    global name#so name outside of def can be used
    while True:#using while True loop
        name = input("What is your name? : ")#ask for users name
        if name.isalpha():#isaplha is used to trap errors
            break#breaks loop
        print("Please enter only A-Z characters only")

                  
greet()#calling function 
print("Hello!",name)#printing name
#Asking user to enter their age 
def age():#using def function so I can use mutiple times without repeating the process
    while True:#using while True loop
        age=input("How old are you? : ")#ask for users age
        if age.isnumeric():#isnumeric is used to trap errors
            break#breaks loop
        print("this is not a valid data type.")
age()#calling function
