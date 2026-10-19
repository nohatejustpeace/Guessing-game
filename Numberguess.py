import random
print("Guessing game")

def main():
    retries = 3
    game_number = random.randint(1, 100)
    while retries > 0:
        choice = int(input("Guess: "))
        if game_number == choice:
            print("You got the guessed correctly")
            break
        else:
            print(f"Wrong. You have {retries} left!")
            print("Click enter to retry")
            input()
            retries -= 1
            
main()