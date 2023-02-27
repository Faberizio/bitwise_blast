# Documentation for Bitwise Blast

## Description

This code is a game called **_"Bitwise Blast"_**. The goal of the game is to correctly **guess the bits of a 5-bit binary number** while competing against the computer. Each round, a random bit (0 / 1) will be assigned to the player and the computer. The player has to **choose a bitwise operator** (&, |, ^) that will be applied to them. If the resulting bit matches one of the bits in the target number, the player scores a point. **If the player correctly guesses 3 bits before making 3 mistakes, they win the game**.

## How to Use

- Run the program.
  Follow the instructions printed on the screen to play the game.

- At the end of the game, the program will ask if you want to play again.

## Code Explanation

The `clear_console()` function clears the console screen. It uses the os module to call the cls command for _Windows_ or the clear command for _Unix-based_ systems.

The `play_game()` function is the **main** function that contains the **game logic**. It first generates a **random** 5-bit **binary number** and assigns it to `table_number`. It also generates random 1-bit binary numbers for the opponent and player, assigns them to `opponent_number` and `player_number`, respectively, and replaces all digits in table_number with asterisks.

The game then begins, and the program displays the opponent's number, the table number (with some digits replaced by asterisks), and the player's number on the screen. It asks the player to **choose a bitwise operator (&, |, ^)** that will be applied to the opponent's number and the player's number.

The operator _input is validated_, and if it is not one of the valid operators, the program prompts the player to choose again.

The chosen **operator is then applied to opponent_number and player_number**, and the resulting bit is **compared** to the corresponding bit in `table_number`.

If the result matches the corresponding bit in table_number, the program replaces the corresponding asterisk with the matched bit and informs the player that they guessed correctly. If there is a miss, the program replaces the corresponding asterisk with an X and informs the player that they guessed wrong.

After each guess, the program generates new random 1-bit binary numbers for the opponent and the player and displays the updated table number.

The game continues until the player has made **3 correct guesses** or 3 incorrect guesses.

If the player has made 3 correct guesses, the program informs the player that **they won** and displays the `table number`. If the player has made 3 incorrect guesses, the program informs the player that they lost and displays the table number.

The `play_again` variable is used to prompt the player if they want to play again. If the player inputs 'y', the game starts over. If the player inputs anything else, the program ends.
