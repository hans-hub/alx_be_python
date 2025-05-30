import random
counter = 0
while True:
    secret_number = random.randint(1,10) #Generate random numbers between 1 and 10
    guess = int(input("Guess number between 1 and 10: "))
    counter += 1
    match guess:
        case _ if guess == secret_number:
            print("Congratulations, you guessed it!")
            print (f"It took you {counter} guesses to get it right")
        case _  if guess > secret_number:
            print("Oops, your guess is a bit high")
        case _ if guess < secret_number:
            print("Nope, your guess is a bit low")
    play_again = input("Do you want to play again?(yes/no)")
    if play_again != "yes":
        print("Thanks for playing! Goodbye 👋")
        
        break
    