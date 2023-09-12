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
    continue_game = True

    draw(computer)             #draw first 2 cards each
    draw(computer)
    draw(human)
    draw(human)
    
    displaycard(computer,human)
    
    human_total = sum(human)     #calculate current total to identify if its already 21
    
    if human_total > 21:   #in first draw, this only happens when both numbers are 11
        if 11 in human:
            human.pop()
            human.append(1)     #replace an 11 (ace) with a 1 (ace)
    elif human_total == 21:
        end_game()    #if totals 21, then you dont need to draw anymore
    
    continue_game = continues()  #check if human continues

    while continue_game == True:
        draw(human)
        print("You just drew a new card. Now: \n")
        displaycard(computer,human)
        
        human_stillingame = checkoverflow(human) #check overflow returns true or false

        if human_stillingame:
            continue_game = continues()
        else:  #directly loses the game - BUST!
            continue_game = False   

def draw(x): #draw a random card from cards and append
    x.append(random.choice(cards))

def sum(x): #sum of array of cards
    tot = 0
    for i in range(len(x)):
        tot+=x[i]
    return tot

def displaycard(computer,human):
    print(f"The dealer's first card is [{computer[-1]},#]")
    print("Your cards are", human)

def continues():  #checks if human continues to play - returns continue_game as true or false
    continues = input("\nWould you like to continue? Y or N: ").lower()
    if continues == "y":
      return True
    elif continues == "n":
      return False

def checkoverflow(x): #check for card values exceeding 21. If exceed, check for ace and adjust accordingly. Then return true or false to the response to see if human is still in game.
    total = sum(x)
    if total > 21:
        for i in range(len(x)):
            if x[i] == 11:          #if ace encountered, replace with 1 value ace
                x[i] = 1
    if total < 21:
        return True
    elif total == 21: 
        end_game()
    else:
        losegame() #bust

def losegame(): #directly lose the game due to bust
    print("BUST, you lost!")

# def end_game(): # if totals 21, then you dont need to draw anymore
    

start_game()