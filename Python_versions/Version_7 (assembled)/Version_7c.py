#This General Knowledge Quiz is developed by Malaika Ali
#importing functions from python library  
from random import shuffle
import time

#User Details for user name input
def greet():#using def function so i can use mutiple times without repeating
    global name#allows us to use name outside of def
    while True: #using while True loop
        name = input("What is your name? : ")
        if name.replace(' ','').isalpha(): #.replace() allows space, using .isalpha() to trap errors
            break #to break the loop
        print("Please enter only A-Z characters only")                
greet()#calling function

print("Hello!",name)#printning name


#User Details for user age input 
def age(): #using def function so i can use mutiple times without repeating
    while True: #using while True loop
        age=input("How old are you? : ")
        if age.replace(' ','').isnumeric():#question repeats if incorrect characters have been entered, using .isnumeric() to trap errors
            break #to break the loop
        print("this is not a valid data type, please only enter numbers.")
age()#calling function

print("********************Welcome to my GENERAL KNOWLEDGE QUIZ!********************")

#Asking user's if they want to read instructions
def rules():#using def function so i can use mutiple times without repeating
    rules = input("Do you want to read the rules{}:? If yes enter: a or Yes or yes or y, If no enter: b or No or n or N. \na. Yes \nb. No \n=>")
    if rules == 'yes' or rules == 'y' or rules == 'a':#using if function
        #prints rules
        print("To play you will be ask how many rounds you would want to play. Once you have \nchosen your rounds (1-5) you will recive questions to answer.Every question you answer \ncorrect you will earn 1 point if you get any question incorrect you wont recive any points. Enjoy the game!")
    else:#using else function
        print("You may continue without the rules.")

    
rules()#calling function

#asking user if they are ready to take the quiz
print("================= READY TO START? ================= ")
def status():#using def function so i can use mutiple times without repeating the process
    ready=input("Are you ready to take the quiz?: Press y to continue or any other key to exit:").lower()#.lower is used to make capital into lowercase
    if ready == "y" or ready == "yes" :#using if function
        print("******************** LETS CONTINUE! ********************") 
    else:#using else function
        print("******************** See you later! ********************")
        exit()#exits program
status()#calling function 

#asking user how many round they would like to play
def get_range():#using def function so i can use mutiple times without repeating
    global num, total#allows us to use name outside of def
    while True:#using while True loop
        try:#using try function
            num = int(input("Please enter the amount of rounds you'd like to play rounds between 1-11: "))
            if 0<num<=11:#using if function
                break #to break the loop
            else:#using else function
                print("Please enter the rounds between 1-11")
        except:#using except function
            print('please enter rounds in numbers only (the limit is 11)')
           
    total=num
        
get_range()#calling function

#creating dictionary to store questions and the right answer and options
gkquiz=[
[
    "\nWho discovered New Zealand?",
    {'answer' : 'b', 'option' :'a.Captain Cook\nb.Abel Tasman\nc.Aunty Cindy\n'}
    ],
[
    "\nWhat is the loudest animal on earth",
    {'answer' : 'a', 'option' :'a)The Sperm Whale\nb)Lion\nc)Blue Whale\n'}
    ],
[
    "\nHow many of Snow White’s seven dwarfs have names ending in the letter Y?",
    {'answer' : 'a', 'option' :'a.5\nb.6\nc.4\n'}
    ],
[
    "\nWhich bone are babies born without?",
    {'answer' : 'c', 'option' :'a.Triceps\nb.Hamstrings\nc.Kneecaps\n'}
    ],
[
    "\nHow many hearts does an octopus have?",
    {'answer' : 'c', 'option' :'a.1\nb.2\nc.3\n'}
    ],
[
    "\nWhat's the national flower of Japan?",
    {'answer' : 'b', 'option' :'a.Daisy\nb.Cherry Bloss Meom\nc.Pink Rose\n'}
    ],
[
    "\nWhat is the slang name for New York City, used by locals?",
    {'answer' : 'a', 'option' :'a.Gotham\nb.The Big Apple\nc.The Small Apple\n'}
    ],
[
    "\nWhich famous graffiti artist come from Bristol?",
    {'answer' : 'a', 'option' :'a.Bansky\nb.Bensky\nc.Bunsky\n'}
    ],
[
    "\nWhat city do The Beatles come from?",
    {'answer' : 'c', 'option' :'a.Germany\nb.Endgame\nc.Liverpool\n'}
    ],
[
    "\nHow many keys does a classic piano?",
    {'answer' : 'b', 'option' :'a.99\nb.88\nc.77\n'}
    ],
[
    "\nName Disney's first film?",
    {'answer' : 'c', 'option' :'aThe Three Caballeros(1944)\nb.Make Mine Music(1946)\nc.Snow White(1937)\n'}
    ],
]
shuffle(gkquiz)#Shuffling the questions

score = 0 #starting score
while num>0:
    data = gkquiz[0]
    q=data[0]
    data = data[1]
    answer = data['answer']
    option = data['option']

    print(q)#printing questions
    print(option)#printing options
    
#score mechanics
    while True:#using while True loop
        user_answer = input("Please enter you answer here : ")
        if user_answer == 'a' or user_answer == 'b' or user_answer == 'c':#using if function
            if user_answer == answer:#using if function
                print("**********************")
                print("Nailed it, keep it up!")
                print("**********************")
                score +=1#user earns a point
                print("**********************")
                print("Your score is", score)#prints users score
                print("**********************")
            else:#using else function
                print("********************************************************************************")
                print("Wrong! Sorry but the option you have chosen is incorrect. The right answer is",answer)
                print("********************************************************************************")
            del gkquiz[0] #using del function to not repeat the questions.
            num-=1
            break #to break the loop
        else:
            print("Please enter your answer in a,b,c only")
#score mechanics
print("You got",score,"out of",total)#printing final score

#endgame_summary
print("Well done player! You got",round(score/total*100,2),"%") #printing final score with percentage
print("That's the end of the quiz, if you want to play again just restart the quiz.\nGoodbye!") #endgame summary 

time.sleep(8) #program pauses for 8 secs till it kills.

exit() #Exits the program
