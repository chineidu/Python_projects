import random


def guess_num(num: int) -> None:
    """ This function is used to guess the computer's number.
    Arguments:
    ----------
    num -- An integer that's greater than 1.

    Returns:
    --------
    None
    """
    random_num = random.randint(1, num)

    active = True
    while active:
        guess = int(input(f"Guess a number between 1 and {num}: "))
        if guess < random_num:
            print("The number is too low!")
        elif guess > random_num:
            print("The number is too high!")
        elif guess == random_num:
            active = False

    print(f"Congrats fam! You guessed the number {random_num} correctly!.")



def guess_num_mod(num: int) -> None:
    """ This function is used to guess the computer's number given 3 turns.
    Arguments:
    ----------
    num -- An integer that's greater than 1.

    Returns:
    --------
    None
    """
    random_num = random.randint(1, num)

    counter = 0
    threshold = 3
    while counter < threshold:
        guess = int(input(f"Guess a number between 1 and {num}: "))
        counter += 1

        if guess != random_num:
            if guess < random_num:
                print("The number is too low!")
            elif guess > random_num:
                print("The number is too high!")

        if counter == threshold - 1:
            print("\nLast chance!")

        if counter == threshold and guess != random_num:
            print(f"Gameover Loser! The number was: '{random_num}'")
            break
            
        elif guess == random_num:
            print(f"Congrats fam! You guessed the number '{random_num}' correctly!.")
            break

            
def computer_guess_my_num() -> None:
    """ This function is used by the computer to guess the user's number given 3 turns.
    Arguments:
    ----------

    Returns:
    --------
    None
    """
    import time

    low = 1
    high = 15
    counter = 0
    threshold = 4
    msg = "Enter a number between 1 and 15: "

    while counter < threshold:
        num = input(msg)
        if not num.isdigit():
            continue

        while True:
            num = int(num)
            counter += 1

            print("Guess the number in my mind: ")
            time.sleep(1)
            guess = random.randint(low, high)
            print(f"Computer guessed ==> {guess}")

            if guess != num:
                prompt = input(f"Enter 'H' if {guess} is too high or 'L' if it's too low. \n").upper()
                if prompt == "H":
                    high = guess - 1 
                elif prompt == "L":
                    low = guess + 1

            if counter == threshold and guess != num:
                print(f"Gameover Loser! The number was: '{num}'")
                break
        
            elif guess == num:
                print(f"Congrats fam! You guessed the number '{num}' correctly!.")
                break
        break


if __name__ == "__main__":
    num = 15
    guess_num_mod(num)
    # computer_guess_my_num()
