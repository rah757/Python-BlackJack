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
        print("\nYou got 21! The dealer will draw now.\n")
        draw_computer(computer,human)    #if totals 21, then you dont need to draw anymore
        
    continue_game = continues()  #check if human continues

    while continue_game == True:
        draw(human)
        print("\nYou just drew a new card.")
        human_stillingame = checkoverflow(human,computer,human) #check overflow returns true or false

        displaycard(computer,human)
            

        if human_stillingame:
            continue_game = continues()
        else:  # End game and draw for dealer
            draw_computer(computer,human) #draws for dealer and ends game

    if continue_game == False:
        draw_computer(computer,human)
    



def draw(x): #draw a random card from cards and append
    x.append(random.choice(cards))

def sum(x): #sum of array of cards
    tot = 0
    for i in range(len(x)):
        tot+=x[i]
    return tot

def displaycard(computer,human):
    print(f"\nThe dealer's first card is [{computer[0]},#]")
    print("Your cards are", human)

def continues():  #checks if human continues to play - returns continue_game as true or false
    continues = input("\nWould you like to continue? Y or N: ").lower()
    if continues == "y":
      return True
    elif continues == "n":
      return False

def checkoverflow(x,computer,human): # check for card values exceeding 21. If exceed, check for ace and adjust accordingly. 
    total = sum(x)                   # Then return true or false to the response to see if human is still in game.
    if total > 21:                   # inputs x-> to check overflow 2nd and 3rd inputs to excecute the draw_computer()
        for i in range(len(x)):
            if x[i] == 11:          #if ace encountered, replace with 1 value ace
                x[i] = 1
                total = sum(x)  
                break
    if total == 21: 
        if x == human:
            print("\nYou got 21! The dealer will draw now.\n")
        draw_computer(computer,human)
    elif total < 21:
        return True
    else:
        losegame(human) #bust

def check_ace_pc(computer):
    total = sum(computer)                   
    if total > 21:                   
        for i in range(len(computer)):
            if computer[i] == 11:          
                computer[i] = 1
                return False  #overflow not exist
        return True #overflown
    

def losegame(human): #directly lose the game due to bust
    print(f"\nYour cards are: {human}\n")
    print("BUST, you lost!")
    exit()

def draw_computer(computer, human): # draws for computer. And gives power to end_game() depending upon the conclusion.
    print(f"\nThe cards are currently: ")
    print(f"Dealer: {computer}")
    print(f"Human: {human}\n")
    compsum = sum(computer)
    if compsum > 21:
        wingame(computer)
    elif compsum >= 17:
        end_game(computer,human)
    else:
        draw(computer)
        print("*The dealer draws*")
        overflow = check_ace_pc(computer)
        if overflow == True:
            wingame(computer)
        draw_computer(computer,human)

def wingame(computer): #dealer got bust, human wins
    print(f"\nThe dealer's cards are: {computer}\n")
    print("The dealer got BUST! You won!")
    exit()

def end_game(computer,human):
    dealer_total = sum(computer)
    human_total = sum(human)
    if dealer_total > human_total:
        print("The dealer won!")
        exit()
    elif human_total > dealer_total:
        print("\nYou won, congrats!")
        exit()
    elif dealer_total == human_total:
        print("It's a draw!")
        exit()

start_game()