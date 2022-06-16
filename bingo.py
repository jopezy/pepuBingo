# Original code by Helana Brock
# from https://codereview.stackexchange.com/questions/229872/python-bingo-game-that-stores-card-in-a-dictionary
# heavily machete'd by Johannes Vahala for ALM Partners PePu Arvonta

import random

random_draw_list = random.sample(range(1, 76), 75)
#dont need this

def generate_card():
    """
    Generates a bingo card and stores the numbers in a dictionary.
    """
    # just start with a plain dictionary, random.sample
    # returns a new list, so no need to pre-allocate lists
    # you won't be using in the future
    card = {}

    # min and max are builtin functions, so use
    # underscores to avoid name shadowing
    _min = 1
    _max = 15

    for letter in 'BINGO':
        card[letter] = random.sample(range(_min, _max), 5)
        _min += 15
        _max += 15

    # You know which letter this needs to be, no need for the if block
    card["N"][2] = "X" # free space!
    return card


def print_card(card, playername):
    """
    Prints the bingo card.

    Arguments:
        card (dictionary): The card to be printed out.
    """
    print(playername)
    for x in (0,1,2,3,4):
        for letter in card:
            print (card[letter][x], end=" ")
        print(" ")

def draw(card, number):
    """
    Pops a number off a list of random numbers. Using the pop method ensures no duplicate
    numbers will be drawn.

    Arguments:
        card (dictionary): The card to to check for the number that was drawn.
        list (list): The list of random numbers to be drawn from.
    """
    for letter in card:
        i = 0
        for x in card[letter]:
            if x == number:
                card[letter][i] = "X"
            i += 1

def check_win(card):
    """
    First checks for diagonal wins, then four-corner, then horizontal, and finally, vertical.

    Arguments:
        card (dictionary): The card to check for a win.
    """
    win = False
    if card["B"][0] == "X" and card["I"][1] == "X" and card["N"][2] == "X" and card["G"][3] == "X" and card["O"][4] == "X":
        win = True
    elif card["O"][0] == "X" and card["G"][1] == "X" and card["N"][2] == "X" and card["I"][3] == "X" and card["B"][4] == "X":
        win = True
    elif card["B"][0] == "X" and card["O"][4] == "X" and card["B"][4] == "X" and card["O"][0] == "X":
        win = True
    for letter in card:
        if(len(set(card[letter]))==1):
            win = True
    for i in range(5):
        cnt = 0
        for letter in card:
            if card[letter][i] == "X":
                cnt += 1
        if cnt == 5:
            win = True
            break
    return win

def main():
    """
    Main method for the program. Generates a card, prints it, and loops through drawing
    and printing until the check_win method returns True or the user enters "quit".
    """
    print("Enter playername or Q")
    players = []
    while True:
        newPlayer = input("Playername:")
        if newPlayer == 'Q':
            break
        else:
            players.append(newPlayer)
    
    cards = {}
    for player in players:
        cards[player] = generate_card()
    
    for player in cards:
        print_card(cards[player], player)
    
    input("press to continue")

    while True:
        #number_drawn = random_draw_list.pop()
        try:
            number_drawn = int(input("Numero: "))
        except:
            print("ei numero")
            continue
        print(f"\nNumber drawn: {number_drawn}.")
        for player in cards:
            draw(cards[player], number_drawn)
            print_card(cards[player], player)


        for player in cards:
            win = check_win(cards[player])
            if win:
                print(f"\nBingo! Winner: " + player)
                quit()



main()
