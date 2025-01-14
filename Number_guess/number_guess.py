from random import randint

target = randint(1,100)
tries = 0

while True:

    try:

        user_input = int(input("Guess a number: "))

        if user_input == target:
            print (f"You won with {tries} failed attempts")
            break

        elif user_input > target:
            print ("The number we are looking for is lower")
            tries += 1
        else:
            print ("The number we are looking for is higher")
            tries += 1

    except ValueError:
        print("that was bs, Try again")
        tries += 1
        continue
