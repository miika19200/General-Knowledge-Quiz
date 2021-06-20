#importing functions from python library  
from random import shuffle

#creating_dictionary to store questions, the right answer and options
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
shuffle(gkquiz)#randomize questions 

score = 0#starting score
while len(gkquiz)>0:
    data = gkquiz[0]
    q=data[0]
    data = data[1]
    answer = data['answer']
    option = data['option']

    print(q)
    print(option)



#score_mechanics


    while True:#using while True loop
        user_answer = input("Please enter you answer here :")
        if user_answer == 'a' or user_answer == 'b' or user_answer == 'c':
            if user_answer == answer:#correct answer
                print("**********************")
                print("Nailed it, keep it up!")
                print("**********************")
                score +=1#user earns a point
                print("**********************")
                print("Your score is", score)#display score 
                print("**********************")
            else:#incorrect answer
                print("********************************************************************************")
                print("Wrong! Sorry but the option you have chosen is incorrect. The right answer is",answer)
                print("********************************************************************************")
            del gkquiz[0]#using del function to not repeat the questions.
            break#breaks loop
        else:#invalid input
            print("Please enter your answer in a,b,c only")
print("You got",score,"out of 5")#display endgame summary  
print("The percentage of the score you got is",round(score/5*100),"%")

