# Author : Pranit Ghag
# This program has a class Cards with different functions included that perform tasks on 
# a deck of cards

# Class definition
class Cards:
    # Constructor
    def __init__(self):
        print("Welcome to Cards")
        # Initializing variables
        self.sorted_deck = ["2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC", "AC", 
               "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD", "AD", 
               "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH", "AH", 
               "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS", "AS"] 
        self.player_deck = self.sorted_deck[:]
        self.count = 0
  
    # Function to return the value of the card at the top of the deck
    def deal(self):
        # Poping the first element of the list or the top of the deck
        dealed_card = self.player_deck.pop(0)
        # Keeping the count of the number of cards dealt
        self.count+=1
        # Returning the card
        return dealed_card

    # Function to return all the dealt cards to the deck and shuffles the deck
    def shuffle(self):
        # Importing random
        import random
        # Restoring the deck by adding the dealt cards
        self.player_deck = self.sorted_deck
        # Shuffling the deck
        random.shuffle(self.player_deck)
        print("Deck shuffled.")
        # Returning the deck
        return self.player_deck

    # Function to list the cards in the deck for top to bottom
    def fan(self):
        print("The cards in your deck are:")
        # Prints a list where the first element is the top card and so on
        print(self.player_deck)

    # Function to return the full deck of cards in order
    def Order(self):
        self.player_deck = self.sorted_deck[:]

    # Function to get the value of card that is a face card
    def value(self,letter):
        if(letter=="A"):
            return 1
        elif(letter=="J"):
            return 11
        elif(letter=="Q"):
            return 12
        elif(letter=="K"):
            return 13  

# Initiallizing variables
bank = 1000
# Object created from Cards class to play Acey Ducey
acey = Cards()
# Function used to shuffle the cards
acey.shuffle()
player_bal = 1000
game = True

# Using while loop to create an interactive menu
while(game):
    print("Your balance is : "+str(player_bal))
    print("The amount in the bank is : "+str(bank)+"\n")
    print("WELCOME TO ACEY DUCEY")
    # Giving options to play or quit the game
    print("1 or 2")
    print("1:Let's Play")
    choice = input("2:Exit\n")
    if(choice=="2"):
        game = False
        break
    elif(choice=="1"):
        print("We are in the game")
        # Using functions from class Cards to deal the top most card
        card1=acey.deal()
        # Using if statement to check if the card is a face card for first card
        if(card1[0]=="A" or card1[0]=="J" or card1[0]=="Q" or card1[0]=="K"):
            # Using function from class Cards to get value of face card
            val1=int(acey.value(card1[0]))
        else:
            val1=int(card1[0])
        card2=acey.deal()
        # Using if statement to check if the card is a face card
        if(card2[0]=="A" or card2[0]=="J" or card2[0]=="Q" or card2[0]=="K"):
            # Using function from class Cards to get value of face card
            val2=int(acey.value(card2[0]))
        else:
            val2=int(card2[0])
        print("The two cards dealt are "+card1+" and "+card2)
        print("Do you want to bet?")
        print("Yes:1")
        answer = input("No:2\n")
        middle = acey.deal()
        # Using if statement to ask if the player wants to bet
        if(answer=="1"):
            bet = int(input("How much money do you wanna bet?\n"))
            if(bet>player_bal):
                print("Can't make a bet greater than your balance.")
                print("Making a bet equal to your balance.")
                bet = player_bal
            # Using if statement to check if the card is a face card
            if(middle[0]=="A" or middle[0]=="J" or middle[0]=="Q" or middle[0]=="K"):
                # Using function from class Cards to get value of face card
                val3=int(acey.value(middle[0]))
            else:
                val3=int(middle[0])
            print("The third card is "+middle)
            # Using if statemnet to see if the third card is in between the first and second card
            if(val3>val1 and val3<val2):
                # Updating player balance and bank amount if player won the bet
                player_bal = player_bal+bet
                bank = bank-bet
                print("You won "+str(bet))
            else:
                # Updating player balance and bank amount if player lost the bet
                player_bal = player_bal-bet
                bank = bank+bet
                print("You lost "+str(bet))
            # If statement to check if the player balance is 0
            if(player_bal==0):
                # Terminating the game to check if the player balance is 0
                print("Your balance is 0 and you can't bet anymore so game over...Bye bye.")
                game = False
            # Using if statement to check if the bank amount is 0
            if(bank==0):
                # Terminating the game if bank amount is 0
                print("The bank has no money. It seems you won...by alot. We gracefully concede.")
                game = False
            # Using if statement to check if the number of cards in the deck are sufficient
            if(acey.count==48):
                # Giving an option to the player to shuffle the deck and continue or quit the game
                print("The deck is done. Do you want to shuffle the pack and try again?")
                print("1:Shuffle")
                ans = input("2:Quit\n")
                if(ans=="1"):
                    acey.shuffle()
                elif(ans=="2"):
                    game = False

print("\nGame Over")
print("Your balance is : "+str(player_bal))

        

        



    
        
