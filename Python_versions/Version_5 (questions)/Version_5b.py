#importing functions from python library  
from random import shuffle
#asking user how many round they would like to play
def get_range():#using def function so i can use mutiple times without repeating
    global num, total#global is used for using something outside of def
    while True:#using while True loop
        try:#block of code for errors
            num = int(input("Please enter the amount of rounds you'd like to play : "))
            if 0<num<=5:#if function is used
                total=num
                break#breaks loop
             #else function is used   
            else:#invalid input
                print("The max is 5")
        except:#repeats if invalid input
            pass
        
get_range()#calling function

#creating dictionary to store questions and the right answer and options
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

score = 0
while len(gkquiz)>0:
    data = gkquiz[0]
    q=data[0]
    data = data[1]
    answer = data['answer']
    option = data['option']

    print(q)
    print(option)

#score mechanics
    while True:#using while True loop
        user_answer = input("Please enter you answer here :")
        if user_answer == 'a' or user_answer == 'b' or user_answer == 'c':#if fuction is used
            if user_answer == answer:#if correct answer 
                print("**********************")
                print("Nailed it, keep it up!")
                print("**********************")
                score +=1#user earns a point
                print("**********************")
                print("Your score is", score)#data points displayed
                print("**********************")
            else:#if incorrect answer
                print("********************************************************************************")
                print("Wrong! Sorry but the option you have chosen is incorrect. The right answer is",answer)
                print("********************************************************************************")
            del gkquiz[0]#del function is used to not repeat the questions
            num-=1
            break#breaks loop
            #else function is used
        else:#invalid input
            print("Please enter your answer in a,b,c only")

