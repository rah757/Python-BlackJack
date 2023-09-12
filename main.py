############### Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

# Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
# Completed Blackjack project reference here: 
#   http://blackjack-final.appbrewery.repl.run

import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def start_game():
    computer = []
    human = []
    human_total = 0
    computer_total = 0

    draw(computer)             #draw first 2 cards each
    draw(computer)
    draw(human)
    draw(human)
    
    displaycard()
    
    for i in range(len(human)):
        human_total+=human[i]          #calculate current total to identify if its already 21
    
    if human_total > 21:   #in first draw, this only happens when both numbers are 11
        if 11 in human:
            human.pop()
            human.append(1)
    elif human_total == 21:
        end_game()          #if totals 21, then you dont need to draw anymore
    
    continues()  #check if human continues

    while continue_game == True:
        draw(human)
        print("You just drew a new card. Now: \n")
        displaycard()
        
        human_stillingame = checkoverflow() #check overflow returns true or false

        if human_stillingame:
            continues()
        else:
            losegame()  #directly loses the game - BUST!

def draw(x):
    x.append(random.choice(cards))

def displaycard():
    print(f"The dealer's first card is [{computer[-1]},#]")
    print("Your cards are", human)

def continues():  #checks if human continues to play - returns continue_game as true or false
    continues = input("\nWould you like to continue? Y or N: ").lower()
    if continues == "y":
      continue_game = True
    else:
      continue_game = False

start_game()