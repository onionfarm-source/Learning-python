answer = 5

print("Please guess a number between 1 and 10:")
guess = int(input())

if guess < answer:
    print("Please guess higher")
    guess = int(input())
    if guess == answer:
        print("Well done, you've guessed it")
    else:
        print("Sorry, you're out of tries")
elif guess > answer:
    print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you've guessed it")
    else:
        print("Sorry, you're out of tries")
else:
    print("You got it the first time")

