'''
    CS 5001, 
    Fall 2023
    HW4 
    Kayser Raei
'''

import random

def create_deck():
    """Makes a list of 52 playing cards."""
    suits = ['s', 'h', 'd', 'c']  # The 4 card suits
    values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    
    deck = []  # Empty list to store the cards
    
    # Loop to make each card and add it to the deck
    for value in values:
        for suit in suits:
            card = value + suit  # Combine the value and suit to make a card
            deck.append(card)  # Add the card to the deck
    
    return deck  # Return the complete deck of cards

def shuffle(cards):
    """Mix up the deck of cards."""
    shuffled = cards.copy()  # Copy of the original cards
    
    # Loop to swap each card with another random card
    for i in range(len(shuffled)):
        j = random.randint(0, len(shuffled) - 1)
        temp = shuffled[i]  # Temporary storage for the current card
        shuffled[i] = shuffled[j]  # Swap the current card with the random card
        shuffled[j] = temp
    
    return shuffled  # Return the shuffled cards

def deal(number_of_hands, number_of_cards, cards):
    """Give cards to the players."""
    all_hands = []  # Empty list to store each player's cards
    
    # Loop to give cards to each player
    for _ in range(number_of_hands):
        hand = []  # Empty list to store a player's cards
        for _ in range(number_of_cards):
            card = cards.pop()  # Take the top card from the deck
            hand.append(card)  # Add the card to the player's hand
        all_hands.append(hand)
    
    return all_hands