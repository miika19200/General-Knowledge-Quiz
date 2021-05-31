#asking user if they are ready to take the quiz
ready=input("Are you ready to take the quiz?: Press y to continue or any other key to exit:").lower()
if ready == "y" or ready == "yes" :
    print("Let's continue!")  
else:
    print("See you later!")
    exit()
