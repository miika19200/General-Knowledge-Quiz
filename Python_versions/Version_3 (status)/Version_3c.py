#asking user if they are ready to take the quiz
def status():#using def function so i can use mutiple times without repeating
    ready=input("Are you ready to take the quiz?: Press y to continue or any other key to exit:").lower()#.lower is used to allow capitals by converting capitals into lowercase
    #using if function
    if ready == "y" or ready == "yes" :#if user inputs yor yes program continues
        print("Let's continue!")  
    #using else function
    else:#if user input different characters program ends
        print("See you later!")
        exit()#exits program
status()#calling function 
