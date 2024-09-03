import random
import math
#Taking inputs as lower bound
lower=int(input("Enter Lower bound: "))

#taking input as upper bound
upper=int(input("Enter Upper bound: "))

#generating a random number between the lower bound and upper bound
x=random.randint(lower,upper)
total_chances= math.ceil(math.log(upper-lower + 1,2))
print("\n\tYou've only ", total_chances, " chances to guess the number!\n")

#initializing the number of guess
count=0
flag=False

while count<total_chances:
    count +=1
    guess=int(input("Guess a numer: "))

    if x==guess:
        print("Congratulations you guessed in ", count," try")
        #once guessed loop will break
        flag=True
        break
    elif x>guess:
        print("You guessed too small!")
    elif x<guess:
        print("You guessed too large!")

#If guessing is more than required guesses,
# show this output
if not flag:
    print("\nThe number is %d" % x)
    print("\nBetter Luck Next Time!")