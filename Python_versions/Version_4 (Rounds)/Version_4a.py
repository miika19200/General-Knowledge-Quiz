#importing functions from python library  
from random import shuffle
#asking user how many round they would like to play
def get_range():#using def function so i can use mutiple times without repeating
    global num, total#global is used for using something outside of def
    while True:#using while True loop
        try:#blocks code for errors
            num = int(input("Please enter the amount of rounds you'd like to play rounds between 1-5 : "))
            if 0<num<=5:#using if function
                break #to break the loop
            #using else function
            else:#invalid input
                print("Please enter the rounds between 1-5")#question limits to 1-5 only
        except:#invalid input
            print('Please enter rounds in numbers only (the limit is 5)')#question limits to 1-5 only
    total=num#total number of rounds
        
get_range()#calling function           

#creating list and dictionary to store questions,answers and options.
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
while num>0:
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
        if user_answer == 'a' or user_answer == 'b' or user_answer == 'c':#using if function
            if user_answer == answer:#if user inputs correct answer
                print("**********************")
                print("Nailed it, keep it up!")
                print("**********************")
                score +=1#user earns 1 point if answer's correct
                print("**********************")
                print("Your score is", score)#prints how many user got correct
                print("**********************")
                #using else function
            else:#if user inputs wrong answer
                print("********************************************************************************")
                print("Wrong! Sorry but the option you have chosen is incorrect. The right answer is",answer)
                print("********************************************************************************")
            del gkquiz[0]#using del function to not repeat the questions.
            num-=1
            break#breaks loop
            #using else function
        else:#if user puts invalid input
            print("Please enter your answer in a,b,c only")
