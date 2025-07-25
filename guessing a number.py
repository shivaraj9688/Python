import random
print("Welcome")
low=int(input("starting number= "))
high=int(input("last number= "))
print("You have 7 tries to guess the number between",[low],"and",[high])
i=7
num=random.randint(low,high)
guess_count=0
while guess_count<i:
    guess_count+=1
    guess=int(input("Enter your guess= "))
    if guess==num:
        print("Congratulation your guess is right"[guess],[num])
        break
    elif(guess>high or guess<low):
        print("Enter a proper guess between",[low],[high] )
    elif guess<num:
        print("Guess number is Small")
    elif guess>num:
        print("Guess number is Big")
print("Thanks for playing")
print("Come again")

