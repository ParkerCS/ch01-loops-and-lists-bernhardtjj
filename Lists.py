# Everything works.
# I like that you used the grid creator layout for the board.
# Glad to see you found a solution for the sieve.  

import random

# LISTS (35PTS TOTAL)
# In these exercises you write functions. Of course, you should not only write the functions,
# you should also write code to test them. For practice, you should also comment your
# functions as explained above.


# PROBLEM 1 (8-ball - 5pts)
# A magic 8-ball, when asked a question, provides a random answer from a list.
# The code below contains a list of possible answers. Create a magic 8-ball program that
# prints a random answer.
answer_list = ["It is certain", "It is decidedly so", "Without a doubt", "Yes, definitely", "You may rely on it",
               "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again",
               "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
               "Don ' t count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

input("What is your question? ")
print(answer_list.pop(random.randrange(len(answer_list))))
print()
# PROBLEM 2 (Shuffle - 5pts)
# A playing card consists of a suit (Heart, Diamond, Club, Spade) and a value (2,3,4,5,6,7,8,9,10,J,Q,K,A).
# Create a list of all possible playing cards, which is a deck.
# Then create a function that shuffles the deck, producing a random order.
card_values = ('Heart', 'Diamond', 'Club', 'Spade')
card_suits = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A')

sorted_deck = [(num, suit) for num in card_values for suit in card_suits]
# get it, cards are tuples because you can't change their names
# and suits, but the deck is a list because you can change that
print(sorted_deck)

shuffled_deck = []
while sorted_deck:
    shuffled_deck.append(sorted_deck.pop(random.randrange(len(sorted_deck))))

print(shuffled_deck)

# PROBLEM 3 (The sieve of Eratosthenes - 10pts)
print("""
 The sieve of Eratosthenes is a method to find all prime numbers between
 1 and a given number using a list. This works very well.""")
# Fill the list with the sequence of
# numbers from 1 to the highest number. Set the value of 1 to zero, as 1 is not prime.
sieve = [i for i in range(1, 1001)]
sieve[0] = 0
# Now loop over the list.
for num in sieve:
    # Find the next number on the list that is not zero, which, at the start, is the number 2.
    if not num:
        continue
    # Now set all multiples of this number to zero.
    for i in range(len(sieve)):
        if num != sieve[i] and not sieve[i] % num:
            sieve[i] = 0
            # Then find the next number on the list that is not zero, which is 3.
            # Set all multiples of this number to zero. Then the next number, which is 5
            # (because 4 has already been set to zero), and do the same thing again.

# Process all the numbers of the list in this way. When you have finished,
# the only numbers left on the list are primes.
# Use this method to determine all the primes between 1 and 1000.

print(" Here are the primes:", [i for i in sieve if i])

# PROBLEM 4 (Tic-Tac-Toe - 15pts)
# Write a Tic-Tac-Toe program that allows two people to play the game against each other.
# In turn, ask each player which row and column they want to play.
# Make sure that the program checks if that row/column combination is empty.
# When a player has won, end the game.
# When the whole board is full and there is no winner, announce a draw.
# This is a fairly long program to write (60 lines or so).
# It will definitely help to use some functions.
# I recommend that you create a function display_board() that gets the board
# as parameter and displays it,
# a function get_row_column() that asks for a row or a column (depending on a parameter)
# and checks whether the user entered a legal value,
# and a function winner() that gets the board as argument and checks if there is a winner.
# Keep track of who the current player is using a global variable player that you can
# pass to a function as an argument if the function needs it.
# I also use a function opponent(), that takes the player as argument and returns
# the opponent. I use that to switch players after each move.

tic_tac = [[' ' for i in range(3)] for n in range(3)]
marker = 'O'


def printer_function():
    """It prints the square again and again and again."""
    boxes = 3
    num = 1
    max_rows = num * boxes + boxes + 1
    for row in range(max_rows):
        if row % (max_rows // boxes):
            p1 = "|"
            p2 = tic_tac[boxes * row // max_rows]
        else:
            p1 = "+"
            p2 = ["-" for b in range(boxes)]
        for b in range(boxes):
            print(p1, end=' ')
            for i in range(num):
                print(p2[b], end=" ")
        print(p1)


def switch_player(m):
    if m == 'X':
        return 'O'
    if m == 'O':
        return 'X'


def check_for_winner(m):
    for i in range(len(tic_tac)):
        for n in range(len(tic_tac[i])):
            if tic_tac[n][i] != m:
                break
        else:
            return True
    else:
        for i in range(len(tic_tac)):
            for n in range(len(tic_tac[i])):
                if tic_tac[i][n] != m:
                    break
            else:
                return True
        else:
            for i in range(len(tic_tac)):
                if tic_tac[i][i] != m:
                    break
            else:
                return True
            for i in range(len(tic_tac)):
                if tic_tac[-1 * (i + 1)][i] != m:
                    break
            else:
                return True
            return False


def check_board_full():
    for i in tic_tac:
        if ' ' in i:
            break
    else:
        return True
    return False


def announce_winner(m):
    print("The winner is", m)


def announce_draw():
    print("It's a draw")


# The main program will be something along the lines of (in pseudo-pseudo-code):
printer_function()  # display board
while True:  # while True:
    row = int(input("Row = ")) - 1  # ask for row
    column = int(input("Column = ")) - 1  # ask for column
    if row > 2 or column > 2 or row < 0 or column < 0:
        print("That's not a location")
        continue
    if tic_tac[row][column] != ' ':  # if row/column already occupied:
        print("That space is already taken")  # display error
        continue
    tic_tac[row][column] = marker  # place player marker in row/col
    printer_function()  # display board
    if check_for_winner(marker):
        announce_winner(marker)
        break
    if check_board_full():
        announce_draw()
        break
    marker = switch_player(marker)

# CHALLENGE PROBLEM 5 (Battleship NO CREDIT, JUST IF YOU WANT TO TRY IT)
# Create a program that is a simplified version of the game “Battleship.”
# The computer creates (in memory) a grid that is 4 cells wide and 3 cells high.
# The rows of the grid are numbered 1 to 3, and the columns of the grid are labeled A to D.
# The computer hides a battleship in three random cells in the grid.
# Each battleship occupies exactly one cell.
# Battleships are not allowed to touch each other horizontally or vertically.
# Make sure that the program places the battleships randomly, so not pre-configured.
# The computer asks the player to “shoot” at cells of the grid.
# The player does so by entering the column letter and row number of the cell
# which she wants to shoot at (e.g., "D3").
# If the cell which the player shoots at contains nothing, the computer responds with “Miss!”
#  If the cell contains a battleship, the computer responds with “You sunk my battleship!”
# and removes the battleship from the cell (i.e., a second shot at the same cell is a miss).
# As soon as the player hits the last battleship, the computer responds with displaying
# how many shots the player needed to shoot down all three battleships, and the program ends.
# To help with debugging the game, at the start the computer should display the grid with
# O's marking empty cells and X's marking cells with battleships.
# Hint: If you have troubles with this exercise, start by using a board which has the
# battleships already placed.
# Once the rest of the code works, add a function that places the battleships at random,
# at first without checking if they are touching one another.
# Once that works, add code that disallows battleships touching each other.
# Maybe I will do this later if I have time.
