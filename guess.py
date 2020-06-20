import random

number = random.randint(1, 10)
attempt = 3

while True:
    print(number)
    user_input = input("Guess the number between 1 and 10 ")
    if int(user_input) == number:
        print("you win!!!")
        break
    else:
        attempt -= 1
        print(f"sorry wrong number, try again, {attempt} attempts left")
        if attempt == 0:
            print("Game over")
            break
