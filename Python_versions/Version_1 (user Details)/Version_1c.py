#User Details
#Using fuctions to greet the user
def greet():
    global name#so name outside of def can be used
    while True:
        name = input("What is your name? : ")
        if name.replace(' ','').isalpha():#isaplha is used to track errors
            break#generates error
        print("Please enter only A-Z characters only")

                  
greet()#calling function
print("Hello!",name)
#Asking user to enter their age 
def age():
    while True:
        age=input("How old are you? : ")
        if age.replace(' ','').isnumeric():#isnumeric is used to track errors
            break#generates error
        print("this is not a valid data type.")
age()#calling function
