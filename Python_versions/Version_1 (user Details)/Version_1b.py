#User Details
#Using fuctions to greet the user
def greet():
    global name#so name outside of def can be used
    while True:
        name = input("What is your name? : ")#ask for users name
        if name.isalpha():#isaplha is used to track errors
            break#generates error
        print("Please enter only A-Z characters only")

                  
greet()#calling function 
print("Hello!",name)
#Asking user to enter their age 
def age():
    while True:
        age=input("How old are you? : ")#ask for users age
        if age.isnumeric():#isnumeric is used to track errors
            break#generates error
        print("this is not a valid data type.")
age()#calling function