import random


# Defines each card with its rank and suit.
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

# Defines a stabdard deck of 52 cards.
class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]
        random.shuffle(self.cards)

# Deals a number range of cards from the deck.
    def deal(self, num_cards):
        return [self.cards.pop() for _ in range(num_cards)]

    def draw(self):
        return self.cards.pop()

# Deals a poker hand of 5 cards.
def deal_poker_hand():
    deck = Deck()  # Creates and shuffles the deck
    return deck.deal(5)  # Deals 5 cards to the player

# Replaces the cards in the hand with new cards from the deck.
def draw_new_cards(hand, deck, cards_to_replace):
    for i in cards_to_replace:
        hand[i] = deck.draw()
    return hand

# Prints the player's hand.
def print_hand(hand):
    print("Your hand:")
    for card in hand:
        print(card)

def main():
    # Step 1: Deals an initial hand of 5 cards.
    hand = deal_poker_hand()
    print_hand(hand)

    # Step 2: Asks the user which cards to replace.
    to_replace = input("Enter the numbers of the cards to replace (1-5), separated by commas (e.g., 1,3,5): ")
    to_replace = [int(x) - 1 for x in to_replace.split(",") if x.strip().isdigit()]

    # Step 3: Replaces the specified cards with new ones from the deck.
    deck = Deck()  # Creates a new deck to draw the new cards from.
    updated_hand = draw_new_cards(hand, deck, to_replace)

    # Step 4: Prints the updated hand after the draw.
    print("\nYour updated hand after drawing new cards:")
    print_hand(updated_hand)

if __name__ == "__main__":
    main()
