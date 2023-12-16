import random

def result(computer,input) :
    if(computer == input) : 
        return 0
    if(computer == 1 and input == 3 or computer == 2 and input == 3):
        return 1
    if(computer == 2 and input == 3 or computer == 3 and input == 1) : 
        return 2
    

computer = random.randint(1,3)

intro = "Welcome To Rock-Paper-Scissor !!"
print(intro.center(100))
input = int(input("1-Rock, 2-Paper, 3-Scissor : "))
match computer : 
    case 1 : 
        print("\nI choose Rock".center(50))
    case 2 :
        print("\nI choose Paper".center(50))
    case 3 :
        print("\nI choose Scissor".center(50))
print("\nRock - Paper - Scissor - Shoot\n".center(50))
res = result(computer, input)

if(res==0) :
    print("It's a Draw !!".center(50))
elif(res==1) : 
    print("You Lose !!, Better Luck Next Time".center(50))
else : 
    print("You Win, But I won't Loose Again".center(50))

