#User Details
#Using fuctions to greet the user
def greet():
    global name
    while True:
        name = input("What is your name? : ")
        if name.replace(' ','').isalpha():
            break
        print("Please enter only A-Z characters only")

                  
greet()
print("Hello!",name)
#Asking user to enter their age 
def age():
    while True:
        age=input("How old are you? : ")
        if age.replace(' ','').isnumeric():
            break
        print("this is not a valid data type.")
age()
