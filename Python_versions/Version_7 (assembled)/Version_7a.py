#gk_quiz
#User Details
def greet():#using def function
    global name#To use name out of def
    while True:#creating while True loop
        name = input("What is your name? : ")
        if name.isalpha():#using if function
            break#breaks loop
        print("Please enter only A-Z characters only")                  


greet()#calling the function
print("Hello!",name)#printing name
#Asking user to enter their age 
def age():#using def function
    while True:#creating while True loop
        age=input("How old are you? : ")
        if age.isnumeric():#using if function
            break#breaks loop
        print("this is not a valid data type.")
age()#calling the function

#Asking user's if they want to read instructions
rules = input("Do you want to read the rules{}:?: \na. Yes \nb. No \n=>")
if rules == 'yes' or rules == 'y' or rules == 'a':#using if function
    print("To play you will be ask how many rounds you would want to play. Once you have \nchosen your rounds (1-5) you will recive questions to answer.Every question you answer \ncorrect you will earn 1 point if you get any question incorrect you wont recive any points. Enjoy the game!")#printing rules
elif rule == 'no' or rule == 'x':#using elif function
    print("You may continue without the rules.")

#asking user if they are ready to take the quiz
ready=input("Are you ready to take the quiz?: Press y to continue or x to exit:").lower()
if ready == "y" or ready == "yes" :#using if function
    print("Let's continue!")  
elif ready == 'no' or ready == 'x':#using elif function
    print("See you later!")
    exit()#calling the function 

# assigning variables to the right answers   
Q1 = 'Abel Tasman'
Q2 = 'The Sperm Whale'
Q3 = '5'
Q4 = 'Kneecaps'
Q5 = '3'
score = 0#starting score

#set of questions that are asked
#question 1

print("\nQuestion: 1|score:{}".format(score))#formating score
ans=input("\nWhat is the loudest animal on earth\na)The Sperm Whale\nb)Lion\nc)Blue Whale : ")
if ans == 'shape of you' or ans == 'Shape of you' or ans =='A' or ans == 'a':#using if function
    print("Correct")
    score+=1#user earns a point
    print("Your score is",score)#printing score
else:#using else function
    print("Oops incorrect the correct answer is :" ,Q1)
    if score <=0:#using if function
        score = 0
        print("Your score is",score)#printing score

#question 2
print("\nQuestion: 2|score:{}".format(score))#formating score
ans=input("\nWho discovered New Zealand?a)Captain Cook\nb.Abel Tasman\nc.Aunty Cindy : ")
if ans =='C' or ans == 'c':#Checking answers
    print("Correct")
    score+=1 #adding score
    print("Your score is",score)
else:#using else function
    print("Oops incorrect the correct answer is :" ,Q2)
    if score <=0:
        score = 0
        print("Your score is",score)

#question 3
print("\nQuestion: 3|score:{}".format(score))
ans=input("\nHow many of Snow White’s seven dwarfs have names ending in the letter Y?\na5\nb.6\nc.4 : ")
if ans =='A' or ans == 'a':#Checking answers
    print("Correct")
    score+=1 #adding score
    print("Your score is",score)
else:
    print("Oops incorrect the correct answer is :" ,Q3)
    if score <=0:
        score = 0
        print("Your score is",score)

#question 4
print("\nQuestion: 4|score:{}".format(score))
ans=input("\nWhich bone are babies born without?\na.Triceps\nb.Hamstrings\nc.Kneecaps : ")
if ans =='C' or ans == 'c':#Checking answers
    print("Correct")
    score+=1 #adding score
    print("Your score is",score)
else:
    print("Oops incorrect the correct answer is :" ,Q4)
    if score <=0:
        score = 0
        print("Your score is",score)

#question 5
print("\nQuestion: 5|score:{}".format(score))
ans=input("\nHow many hearts does an octopus have?\na.1\nb.2\nc.3 : ")
if ans =='C' or ans == 'c':#Checking answers
    print("Correct")
    score+=1 #adding score
    print("Your score is",score)
else:
    print("Oops incorrect the correct answer is :" ,Q5)
    if score <=0:
        score = 0
        print("Your score is",score)



        
