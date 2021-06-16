#question 1

print("\nQuestion: 1 | score: {}".format(score))
ans=input("who discovered New Zealand?\na.Captain Cook\nb.Abdel Tasman\nc.Aunty Cindy\n=>")
if ans == 'Abel Tasman' or ans == 'abdel tasman'or ans == 'B' or ans == 'b':
    print('Correct')
    score +=1
    print("your score is",score)

else:
    print('incorrect')

    if score <=0:
        score = 0
        print("Incorrect the answer is Abdel Tasman")

#question 2


    print("\nQuestion: 2 | score: {}".format(score))
    ans=input("What is the loudest animal on Earth?\na.The Sperm Whale\nb.Lion\nc.blue Whale\n=>")
    if ans == 'The Sperm Whale' or ans == 'the sperm whale'or ans == 'a' or ans == 'A':
        print('Correct')
        score +=1
        print("your score is",score)
    else:
        print('incorrect')
        if score <=0:
            score =0
        print("Incorrect the answer is The Sperm Whale")

#question 3


    print("\nQuestion: 3 | score: {}".format(score))
    ans=input("How many of Snow White’s seven dwarfs have names ending in the letter Y?\na.5\nb.6\nc.4\n=>")
    if ans == '5' or ans == 'five'or ans == 'a' or ans == 'A':
        print('Correct')
        score +=1
        print("your score is",score)
    else:
        print('incorrect')
        if score <=0:
            score =0
        print("Incorrect the answer is 5")

#question 4


    print("\nQuestion: 4 | score: {}".format(score))
    ans=input("Which bone are babies born without?\na.triceps\nb.hamstrings\nc.kneecap\n=>")
    if ans == 'Kneecap' or ans == 'kneecap'or ans == 'c' or ans == 'C':
        print('Correct')
        score +=1
        print("your score is",score)
    else:
        print('incorrect')
        if score <=0:
            score =0

        print("Incorrect the answer is kneecap")

        
#question 5


    print("\nQuestion: 5 | score: {}".format(score))
    ans=input("How many hearts does an octopus have?\na.1\nb.2\nc.3\n=>")
    if ans == '3' or ans == 'three'or ans == 'c' or ans == 'C':
        print('Correct')
        score +=1
        print("your score is",score)
    else:
        print('incorrect')
        if score <=0:
            score =0
        print("Incorrect the answer is 3")
       

