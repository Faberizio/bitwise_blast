import random


def generate_secret_number():
    """Generate a random binary number represented as a string of asterisks"""
    secret_number = bin(random.randint(0, 255))[2:].zfill(8)
    return "".join("*" if b == "0" else b for b in secret_number)


def apply_operator(operator, number):
    """Apply a bitwise operator to a binary number"""
    if operator == "&":
        return bin(int(number, 2) & random.randint(0, 255))[2:].zfill(8)
    elif operator == "|":
        return bin(int(number, 2) | random.randint(0, 255))[2:].zfill(8)
    elif operator == "^":
        return bin(int(number, 2) ^ random.randint(0, 255))[2:].zfill(8)
    else:
        raise ValueError("Invalid operator")


def reveal_bits(secret_number, player_number):
    """Compare the bits of the secret number and the player number, revealing the matching bits"""
    revealed_number = ""
    for i in range(len(secret_number)):
        if secret_number[i] == player_number[i]:
            revealed_number += secret_number[i]
        else:
            revealed_number += "*"
    return revealed_number


# Main game loop
while True:
    secret_number = generate_secret_number()
    player_number = bin(random.randint(0, 255))[2:].zfill(8)
    print("Secret number:", secret_number)
    print("Player number:", player_number)
    operator = input("Enter a bitwise operator (&, |, ^): ")
    player_number = apply_operator(operator, player_number)
    revealed_number = reveal_bits(secret_number, player_number)
    print("Revealed number:", revealed_number)
    if revealed_number == secret_number:
        print("You win! Sercret number was:", secret_number)
        break
    else:
        input("Press Enter to continue...")
#
