from random import shuffle
import time
#User Details
#User name
def greet():
    global name
    while True:
        name = input("What is your name? : ")
        if name.isalpha():
            break
        print("Please enter only A-Z characters only")

                  
greet()
print("Hello!",name)
#Asking user to enter their age 
def age():
    while True:
        age=input("How old are you? : ")
        if age.isnumeric():
            break
        print("this is not a valid data type.")
age()

print("********************Welcome to my GENERAL KNOWLEDGE QUIZ!********************")

#Asking user's if they want to read instructions
def rules():
    rules = input("Do you want to read the rules{}:?: \na. Yes \nb. No \n=>")
    if rules == 'yes' or rules == 'y' or rules == 'a':
        print("To play you will be ask how many rounds you would want to play. Once you have \nchosen your rounds (1-5) you will recive questions to answer.Every question you answer \ncorrect you will earn 1 point if you get any question incorrect you wont recive any points. Enjoy the game!")
    else:
        print("You may continue without the rules.")

    
rules()

#asking user if they are ready to take the quiz
ready=input("Are you ready to take the quiz?: Press y to continue or x to exit:").lower()
if ready == "y" or ready == "yes" :
    print("Let's continue!")  
else:
    print("See you later!")
    exit()

#asking user how many round they would like to play
def get_range():
    global num, total
    while True:
        try:
            num = int(input("Please enter the amount of rounds you'd like to play : "))
            if 0<num<=5:
                total=num
                break
            else:
                print("The max is 5")
        except:
            pass
        
get_range()

#creating dictionary for question and the right answer
gkquiz=[
[
    "\nWho discovered New Zealand?",
    {'answer' : 'b', 'option' :'a)Captain Cook\nb.Abel Tasman\nc.Aunty Cindy\n'}
    ],
[
    "\nWhat is the loudest animal on earth",
    {'answer' : 'a', 'option' :'a)The Sperm Whale\nb)Lion\nc)Blue Whale\n'}
    ],
[
    "\nHow many of Snow White’s seven dwarfs have names ending in the letter Y?",
    {'answer' : 'a', 'option' :'a)5\nb)6\nc)4\n'}
    ],
[
    "\nWhich bone are babies born without?",
    {'answer' : 'c', 'option' :'a)Triceps\nb)Hamstrings\nc)Kneecaps\n'}
    ],
[
    "\nHow many hearts does an octopus have?",
    {'answer' : 'c', 'option' :'a)1\nb)2\nc)3\n'}
    ],
]
shuffle(gkquiz)

score = 0
while len(gkquiz)>0 and num!=0:
    data = gkquiz[0]
    q=data[0]
    data = data[1]
    answer = data['answer']
    option = data['option']

    print(q)
    print(option)
    
#score mechanics
    while True:
        user_answer = input("Please enter you answer here :")
        if user_answer == 'a' or user_answer == 'b' or user_answer == 'c':
            if user_answer == answer:
                print("**********************")
                print("Nailed it, keep it up!")
                print("**********************")
                score +=1
                print("**********************")
                print("Your score is", score)
                print("**********************")
            else:
                print("********************************************************************************")
                print("Wrong! Sorry but the option you have chosen is incorrect. The right answer is",answer)
                print("********************************************************************************")
            del gkquiz[0]
            num-=1
            break
        else:
            print("Please enter your answer in a,b,c only")
#score mechanics
print("You got",score,"out of",total)
print("The percentage of the score you got is",round(score/total*100))

#endgame_summary
print("Well done player! You got",round(score/total*100))
print("That's the end of the quiz, if you want to play again just restart the quiz.\nGoodbye<3")

time.sleep(8) #program pauses for 8 secs till it kills.
exit()
