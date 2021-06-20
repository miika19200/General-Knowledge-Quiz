#question 1

print("\nQuestion: 1 | score: {}".format(score))#display data
ans=input("who discovered New Zealand?\na.Captain Cook\nb.Abel Tasman\nc.Aunty Cindy\n=>")#questions and options
if ans == 'Abel Tasman' or ans == 'abel tasman'or ans == 'B' or ans == 'b':#correct answer 
    print('Correct')
    score +=1#user gets 1 point
    print("your score is",score)#display points

else:#incorrect answer 
    print('incorrect')

    if score <=0:
        score = 0#user gets no points
        print("Incorrect the answer is Abdel Tasman")

#question 2


    print("\nQuestion: 2 | score: {}".format(score))#display score
    ans=input("What is the loudest animal on Earth?\na.The Sperm Whale\nb.Lion\nc.blue Whale\n=>")#questions and options
    if ans == 'The Sperm Whale' or ans == 'the sperm whale'or ans == 'a' or ans == 'A':#correct answer
        print('Correct')
        score +=1#user gets a point for correct answer
        print("your score is",score)
    else:#incorrect answer 
        print('incorrect')
        if score <=0:
            score =0#user gets no points
        print("Incorrect the answer is The Sperm Whale")

#question 3


    print("\nQuestion: 3 | score: {}".format(score))#data display 
    ans=input("How many of Snow White’s seven dwarfs have names ending in the letter Y?\na.5\nb.6\nc.4\n=>")#questions and options
    if ans == '5' or ans == 'five'or ans == 'a' or ans == 'A':#correct answer 
        print('Correct')
        score +=1#user recives a point for correct answer
        print("your score is",score)#display data points
    else:#incorrect answer
        print('incorrect')
        if score <=0:
            score =0#user earns no points
        print("Incorrect the answer is 5")

#question 4


    print("\nQuestion: 4 | score: {}".format(score))#data display
    ans=input("Which bone are babies born without?\na.triceps\nb.hamstrings\nc.kneecap\n=>")#question and option
    if ans == 'Kneecap' or ans == 'kneecap'or ans == 'c' or ans == 'C':#correct answer
        print('Correct')
        score +=1#user earns a point for correct answer
        print("your score is",score)#display data points
    else:#incorrect answer
        print('incorrect')
        if score <=0:
            score =0#user earns no points

        print("Incorrect the answer is kneecap")

        
#question 5


    print("\nQuestion: 5 | score: {}".format(score))#data display
    ans=input("How many hearts does an octopus have?\na.1\nb.2\nc.3\n=>")#questions and options
    if ans == '3' or ans == 'three'or ans == 'c' or ans == 'C':#correct answer
        print('Correct')
        score +=1#user recieves a point for correct answer
        print("your score is",score)#display data points
    else:#incorrect answer 
        print('incorrect')
        if score <=0:
            score =0#user doesn't earn any points
        print("Incorrect the answer is 3")
       

