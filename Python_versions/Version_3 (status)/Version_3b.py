#asking user if they are ready to take the quiz
ready=input("Are you ready to take the quiz?: Press y to continue or any other key to exit:").lower()#.lower is used to make capital into lowercase
if ready == "y" or ready == "yes" :#program continues 
    print("Let's continue!")  
else:#ends program
    print("See you later!")
    exit()#exits program
