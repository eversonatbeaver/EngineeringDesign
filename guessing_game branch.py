import random
number = random.randint(-210,-190)
win = False
print ("I'm thinking of a number between -210 and -190")
while not win:
    guess = int(input("What number could it be?"))
    if guess == number:
        win = True
        print("Congratulations. You guessed the right number!")
    elif guess < number:
        print ("Too low")
    elif guess > number:
        print ("Too high")
print("You win! The number was {}". format(number))
