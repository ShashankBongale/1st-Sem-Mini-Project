print(format("Start", '-^167'))
import random
from threading import Timer
c=1
p=0
print("\n")
print(format("Rules:", '^167'))
print("\n\bFirst Level Rules:")
print("\nIn this level you will be given singe numbers or alphabets or special characters to type and time limit to type is 3 seconds.If you cross the limit your answer will be considered as wrong.")
print("\n\bSecond Level Rules:")
print("\nIn this level you will be given combination of numbers,alphabets and special character to type and time limit to type is 10 seconds.If you cross the limit your answer will be considered as wrong.\n\n")
print("\n\bThird Level Rules")
print("\nIn this level you will given statements to type and time limit to type is 100 sec.If you cross the limit your answer will be considered as wrong.\n\n")
print("\bIf you have read the above rules properly press 1 to start the game.")
s=int(input())
print(format("", '-^167'))
if s==1:
    print("\n")
    print(format("\bQUICK MASTER WELCOMES YOU TO THE FIRST LEVEL OF GAME\n\n", '^167'))
    while(c<11):
        n=random.randint(48,123)
        n2=chr(n)
        print("Enter",chr(n),"in below given seconds")
        timeout=3
        t=Timer(timeout,print,[""])
        t.start()
        prompt=timeout
        answer=input(prompt)
        print(t)
        t.cancel()
        x=str(t)
        t1=x.split()
        if n2==answer and "stopped" not in t1:
            p=p+1
            print("\nResult=Correct\n")
        else:
            print("Result=Wrong\n")
        print(format("", '-^167'))
        c=c+1
    print("Point=",p)
    d=0
    if p>=7:
        print("\n\bYOU HAVE SUCCESSFULLY COMPLETED THE FIRST LEVEL")
        choice=int(input("\nEnter 0 if you do not want to proced or 1 if you want to continue\n"))
        if(choice):
            print("\n")
            print(format("\bQUICK MASTER WELCOMES YOU TO THE SECOND LEVEL OF THE GAME\n\n", '^167'))
            while(d<10):
                m1=random.randint(48,123)
                m1m=chr(m1)
                for i in range(0,5):
                    m2=random.randint(48,123)
                    m2m=chr(m2)
                    m1m=m1m+m2m
                print("Enter",m1m,"in below given seconds")
                timeout=10
                t=Timer(timeout,print,[""])
                t.start()
                prompt=timeout
                answer=input(prompt)
                print(t)
                t.cancel()
                x=str(t)
                t1=x.split()
                if m1m==answer and "stopped" not in t1:
                    p=p+1
                    print("\nResult=Correct\n")
                else:
                    print("Result=Wrong\n")
                print(format("", '-^167'))
                d=d+1
            print("Point=",p)
        else:
            print("Thank you for using our game\nYou are smart enough so please vist us again")
    else:
        print("Please try again \nyou have to get 7 or more than 7 points to go to next round")
    if p>=15:
         print("\n\bYOU HAVE SUCCESSFULLY COMPLETED THE SECOND LEVEL")
         choice=int(input("\nEnter 0 if you do not want to proced or 1 if you want to continue\n"))
         if(choice):
             p1=0
             d=0
             print("\n")
             print(format("\bQUICK MASTER WELCOMES YOU TO THE THIRD LEVEL OF THE GAME\n\n", '^167'))
             while(d<5):
                 s={1:"Computer science is fundamentally about computational problem solving",2:"An algorithm is a fi nite number of clearly described, unambiguous “doable” steps that can be systematically followed to produce a desired result for given input in a finite amount of time.",3:"It is essentaial that computer hardware be reliable and error free",4:"A byte is group of bits operated on as a single unit in a computer system",5:"The CPU is the brain of a computer system,containing digital logic circuitary able to interpret and execute instruction",6:"Computer software is a st of program instructions",7:"The syntax of a language is a set of characters and the acceptable sequences of those characters.",8:"The semantics of a language is the meaning associated with each syntactically correct sequence of characters",9:"Procedural programming and object-oriented programming are two major programming paradigms in use today",10:"Guido van Rossum is the creator of python",11:"The quick brown fox jumps over the lazy dog.",12:"All the faith he had had had had no effect on the outcome of his life.",13:" Read rhymes with lead, and read rhymes with lead, but read and lead don’t rhyme, and neither do read and lead.",14:"A purple pig and a green donkey flew a kite in the middle of the night and ended up sunburnt.",15:"Wednesday is hump but has anyone asked the \
 camel if he’s happy about it?",16:"A song can make or ruin a person’s \
 day if they let it get to them.",17:"Where do random thoughts come from?",18:"Lets all be unique together\
until we realise we are all the same.",19:"If I don’t like something,I’ll stay away from it.",20:"I love eating toasted cheese and tuna sandwiches.",
   21:"I want to buy a onesie… but know it won’t suit me.",22:"I currently have 4 windows open up… and I don’t know why",
   23:"This is the last random sentence I will be writing and I am going to stop mid-sent",
   24:"Is this bridge made of wood?",25:"Donald Trump is the 45th president of United states",26:"Like a Boss!",27:"You know nothing Jon Snow."}
                 n=random.randint(0,28)
                 print("Enter the sentence\n",s[n],"\nin given below second\n")
                 timeout=25
                 t=Timer(timeout,print,[""])
                 t.start()
                 prompt=timeout
                 answer=input(prompt)
                 print(t)
                 t.cancel()
                 x=str(t)
                 t1=x.split()
                 if s[n]==answer and "stopped" not in t1:
                     p1=p1+1
                     p=p+1
                     print("\nResult=Correct\n")
                     print(format("", '-^167'))

                 else:
                     print("Result=Wrong\n")
                     print(format("", '-^167'))
                 d=d+1
             print("Total Points=",p)
             print("Points in level 3=",p1)
             if(p1<6):
                 print("You have got only ",p1," points in level 3\nSo please try quick master once again")
             else:
                 print("You have successfully completed all the levels\nPlease visit us again to still improve your typing skills")

         else:
             print("Thank you for using our game\nYou are smart enough so please vist us again")

    else:
         print("Please try again \nYou have to get 15 or more than 15 points to go to next round")
else:
    print("You need to type 1 to start the game")
azzzzz=input()















