from random import shuffle
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
while len(gkquiz)>0:
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

