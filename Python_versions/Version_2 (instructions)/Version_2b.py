#Asking user's if they want to read instructions
rules = input("Do you want to read the rules{}:?: \na. Yes \nb. No \n=>")#ask user if they want to read rules or not
#using if function
if rules == 'yes' or rules == 'y' or rules == 'a':#if user inputs yes, a or yes program prints rules
    print("To play you will be ask how many rounds you would want to play. Once you have \nchosen your rounds (1-5) you will recive questions to answer.Every question you answer \ncorrect you will earn 1 point if you get any question incorrect you wont recive any points. Enjoy the game!")
    #using else function
else:#if user inputs any other characters program continues
    print("You may continue without the rules.")
