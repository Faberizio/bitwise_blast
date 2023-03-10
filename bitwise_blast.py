import random
import os


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def play_game():

    clear_console()

    # Generate random 5 bits binary number and name it as table number
    table_number = bin(random.randint(0, 31))[2:].zfill(5)

    # Generate random 1 bit binary number for opponent and player
    opponent_number = bin(random.randint(0, 1))[2:]
    player_number = bin(random.randint(0, 1))[2:]

    # Replace table_number with asterisks for initial display
    displayed_table_number = "*" * len(table_number)

    # Keep track of number of matches and misses
    matches = 0
    misses = 0

    # These are the rules for the game.
    print("Welcome to Bitwise Blast!")
    print("")
    print("The goal of the game is to correctly guess the bits of a 5-bit binary number while competing against the computer.")
    print("Each round, a random bit (0 / 1) will be assign to you and the computer.")
    print("You have to choose a bitwise operator (&, |, ^) that will be applyed to them.")
    print("If the resulting bit matches one of the bits in the target number, you will score a point.")
    print("If you correctly guess 3 bits before making 3 mistakes, you win!")
    print("")

    # Loop until there are 3 matches or 3 misses
    while matches < 3 and misses < 3:

        # Display opponent number, player number, and table number (with some digits replaced by asterisks)
        print(f"Opponent number: {opponent_number}")
        print("")
        print(f"Table number: {displayed_table_number}")
        print("")
        print(f"Player number: {player_number}")
        print("")

        # Get the player's choice of bitwise operator
        operator = input("Choose a bitwise operator (&, |, ^): ")
        print("")
        while operator not in ("&", "|", "^"):
            print("Invalid operator. Please try again.")
            print("")
            operator = input("Choose a bitwise operator (&, |, ^): ")
            print("")

        # Apply the chosen operator to the opponent number and player number
        result = eval(f"{opponent_number} {operator} {player_number}")

        # Check if the result matches the corresponding bit in the table number
        bit_index = len(table_number) - (matches + misses + 1)
        if result == int(table_number[bit_index]):
            # If there is a match, replace the corresponding asterisk with the matched bit
            displayed_table_number = displayed_table_number[:bit_index] + str(
                table_number[bit_index]) + displayed_table_number[bit_index+1:]
            print(f"Correct! The bit was {table_number[bit_index]}")
            print("")
            matches += 1

        else:
            # If there is a miss, replace the corresponding asterisk with an X
            displayed_table_number = displayed_table_number[:bit_index] + \
                "X" + displayed_table_number[bit_index+1:]
            print(f"Wrong! The bit was {table_number[bit_index]}")
            print("")
            misses += 1

        # Generate new random 1 bit binary number for opponent and player and display the updated table number
        opponent_number = bin(random.randint(0, 1))[2:]
        player_number = bin(random.randint(0, 1))[2:]

    if matches >= 3:
        print("Congratulations! You won!")
        print("")
        print("Table number was: ", table_number)
        print("")
    else:
        print("Sorry, you lost. Better luck next time!")
        print("")
        print("Table number was: ", table_number)
        print("")


play_again = 'y'
while play_again.lower() == 'y':
    play_game()
    play_again = input(
        "Do you want to play again? (y = yes / any other key to quit)")
    print("")
