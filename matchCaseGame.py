import random
secret_number = random.randint(1,10) #Generate random numbers between 1 and 10
guess = int(input("Guess number between 1 and 10: "))
match guess:
    case _ if guess == secret_number:
        print("Congratulations, you guessed it!", secret_number)
    case _  if guess > secret_number:
        print("Oops, your guess is a bit high")
    case _ if guess < secret_number:
        print("Nope, your guess is a bit low")
