import random
rn=random.randint(1,9)

print("--------Number guessing game-------")
name=input("enter your name: ")
print("Hello",name,"!!""Okay lets see what are your chances of success")
guesses_number=0
while guesses_number<5:
    gn=int(input("your guess: "))
    guesses_number+=1
    if gn<rn:
        print("your number",gn,"is too low, try again")
    elif gn>rn:
        print("your number",gn,"is too high,try again")
    elif gn==rn:
        break
if gn==rn:
    print("you guessed the number",gn," correctly in",int(guesses_number),"tries")
    print("----play again soon----")
else:
    print("you didnt guess the number right, its:",rn,"\nbadluck heh, Don't lose hope")
    print("Better luck next time :)")