# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 11:37:25 2020

@author: fidelismwansa
"""


import random
import time
from os import system

def display_board(board, n):

    def row_counter(row, letter):
        #Iteration counter 
        i = 0
        # For every item in rows
        for x in rows:
            if letter in x:
                return int(i)
            else:
                i += 1

    def generate_ships(board,n):
        # Counter
        i = 0
        chance = n
        print (chance)        
        while n > 0 :
            # For debugging
            rng = random.randrange(0, 100)
            #print rng
            if rng == chance:
                print (rng, chance, i)
                # Maths
                cords = []
                #everything below 10 is the 0th index
                if i < 10:
                    cords = [0, i]
                    # Generate the ship 
                    print ("cords = ",cords)
                    board[cords[0]][cords[1]] = ':'
                    print ("Generating Ship at : {}, {}".format(cords[0], cords[1]))
                    n -= 1
                #everything about 10 has its own index ~ 
                elif i >= 10:
                    b = str(i).split()
                    print( b)
                    #tenth = str(b[0][0]) + str(0)
                    #Convert the value to our array structure int
                    if i > 100:
                        tenth = str(b[0][0]) + str(0)
                        print ("val : ", tenth)
                        tenth = int(tenth) / 10
                        nth = b[0][2]
                    else:
                        tenth = str(b[0][0]) + str(0)
                        tenth = int(tenth) / 10 
                        nth = b[0][1]
                    cords = [int(tenth), int(nth)]
                    # Generate the ship 
                    board[cords[0]][cords[1]] = ':'
                    print ("Generating Ship at : {}, {}".format(cords[0], cords[1]))
                    print ("\n\n")
                    #raw_input()

                    n -= 1
                    if i > 100:
                        i == 0
            else:                    
                i += 1
        return board
    # Set the number of ships we need to destroy in order to win
    alive_ships = n
    # Fill our board with lovely ships
    hidden_board = generate_ships(board, n)
    # Print Turns
    turns = 1
    # Print the board whilst true
    while True:
        print ("Turn : {}".format(turns))
        # Clear screen on new iteration
        system("clear")
        # Show Grid Positions
        rows = ['A', 'B', 'C ', 'D ', 'E ', 'F ', 'G ', 'H ', 'I ']
        rows = ['A', 'B', 'C ', 'D ', 'E ', 'F ', 'G ', 'H ', 'I ']
        # Iteration counter
        i = 1
        print (" O : ", rows)
        # Ouput the board
        for x in board:
            # Print each layer on a new line
            print ("\n {} :".format(i), x)
            i += 1
        # Ask for user input
        print ("Choose zone to target e.g 'A 10'")
        usr_in = input()
        xy = usr_in.split()
        print('Press enter to continue')
        input()
        # Find the value of their Chosen Letter
        y = row_counter(rows, xy[0])
        x = xy[1]
        x = int(x) -1
        #print y
        print ("Attacking {},{} !!".format(x, y))
        #print int(x), int(y)
        #raw_input()
        # Check if we hit a ship
        if hidden_board[int(x)][int(y)] == ":":
            print ("Target Hit")
            # Remove 1 ship
            alive_ships -= 1
            # Replace it with an o or something
            board[int(x)][int(y)] = "O"
            time.sleep(1)
        else:
            print ("Missed")
            # Replace targeted spot with an x
            board[int(x)][int(y)] = "X"
        # if all ships are destroyed end the game
        if alive_ships == 0:
            # Print message could include names and stuff
            print ("Congratulations you sunk them in {} turns!".format(turns))
            return
        turns += 1

new_board = []
n_ships = 5
# Creating a 10 by 10 grid
for i in range(10):
    new_board.append(['~'] * 10)
#start the game
display_board(new_board,n_ships)
raw_input()
