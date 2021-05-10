#Ask for name
while True:
    name = input("enter your name : ")
    if name.isalpha():
        break
    print("please enter characters A-Z only")
#ask user if they want to read instructions
status = input("Do you want to read the instructions :{}?:  \na. Yes \nb. No \n=>".format(name))
# if user inputs No
if status == 'No' or status == 'no' or status == 'n' or status == 'N' :
   print("Welcome to General Knowledge quiz.")
# if user inputs yes
else :
    print("To play you will be ask how many rounds you would want to play.Once you have \nchosen your rounds you will recive questions to answer.Every question you get \ncorrect you will earn 1 point if you get any question incorrect you wont recive any points. Enjoy the game!")

