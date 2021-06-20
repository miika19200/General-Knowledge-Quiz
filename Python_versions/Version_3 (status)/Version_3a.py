#asking user if they are ready to take the quiz
ready=input("Are you ready to take the quiz?: Press y to continue or x to exit:").lower()#.lower is used to make capital into lowercase
if ready == "y" or ready == "yes" : # using if function
    print("Let's continue!")  
elif ready == 'no' or ready == 'x': #using elif function
    print("See you later!")
    exit() #exits program
