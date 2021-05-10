rounds = int(input("How many rounds would you like to play?"))
counter = 0
while counter <= rounds-1:
    while rounds not in range(1,5) :
        try:
            rounds = int(raw_input("Sorry! There is only 1 to 5 rounds. Try again:"))
        except: print("ERROR invalid input. Out of range or wrong type of data.")

import random
from random import shuffle
list1=["who discovered New Zealand?","What is the loudest animal on Earth?"
       ,"How many of Snow White’s seven dwarfs have names ending in the letter Y?",
       "Which bone are babies born without?" ,
       "How many hearts does an octopus have?",
       "What’s the most expensive home in the world?" ]
list2=["Abdel Tasman","Sperm Whale","5","kneecap", "3","Buckland Palace"]
ans=dict(zip(list1,list2,))
       
x=random.randint(0,len(list1)-1)
y=list1[x]
print(y)
your_answer =input(“Answer : ”)
If your_answer==ans[y]
       print(“You are correct, you get 1 point!”)
       score +=1
        print("your score is",score)
Else:
       print(”You are iincorrect, you get no points’)
        if score <=0:
            score =0
