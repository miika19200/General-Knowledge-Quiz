Q1 = 'Abel Tasman'
Q2 = 'The Sperm Whale'

score = 0

#set of questions that are asked
#question 1

print("\nQuestion: 1|score:{}".format(score))#formating score
ans=input("\nWhat is the loudest animal on earth\na)The Sperm Whale\nb)Lion\nc)Blue Whale : ")
if ans == 'A' or ans == 'a':
    print("Correct")
    score+=1
    print("Your score is",score)
else:
    print("Oops incorrect the correct answer is :" ,Q1)
    if score <=0:
        score = 0
        print("Your score is",score)

#question 2
print("\nQuestion: 2|score:{}".format(score))
ans=input("\nWho discovered New Zealand?\n.)Captain Cook\nb.Abel Tasman\nc.Aunty Cindy : ")
if ans =='B' or ans == 'b':#Checking answers
    print("Correct")
    score+=1 #adding score
    print("Your score is",score)
else:
    print("Oops incorrect the correct answer is :" ,Q2)
    if score <=0:
        score = 0
        print("Your score is",score)
