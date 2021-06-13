#Asking user's if they want to read instructions
def rules():
    rules = input("Do you want to read the rules{}:?: \na. Yes \nb. No \n=>")#ask user if they want to read rules or not
    if rules == 'yes' or rules == 'y' or rules == 'a' or rules == 'YeS':#prints rules
        print("To play you will be ask how many rounds you would want to play. Once you have \nchosen your rounds (1-5) you will recive questions to answer.Every question you answer \ncorrect you will earn 1 point if you get any question incorrect you wont recive any points. Enjoy the game!")
    else:#continues program
        print("You may continue without the rules.")
rules()#calling function
