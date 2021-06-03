from random import shuffle
#asking user how many round they would like to play
def rounds():
    global r, total
    while True:
        try:
            r = int(input("Please enter the amount of rounds you'd like to play : "))
            if 0<r<=5: #allowing only to answer 5 questions nothing over or below
                total=num
                break
            else:
                print("The max is 5")
        except:
            print("Please eneter only numbers 1-5")
        
rounds()
#creating_dictionary_for_question_and_the_right_answer
gkquiz=[
[
    "\nWho discovered New Zealand?",
    {'answer' : 'b', 'option' :'a)Captain Cook\nb.Abdel Tasman\nc.Aunty Cindy\n'}
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
while num>0:
    data = gkquiz[0]
    q=data[0]
    data = data[1]
    answer = data['answer']
    option = data['option']

    print(q)
    print(option)



#score_mechanics


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
            break
        else:
            print("Please enter your answer in a,b,c only")
#presenting_score_to_players
print("You got",score,"out of",total)
#endgame_summary
print("Well done player! You got",round(score/total*100))
print("That's the end of the quiz, if you want to play again just restart the quiz.\nGoodbye<3")

time.sleep(8) #program pauses for 8 secs till it kills.
exit()
