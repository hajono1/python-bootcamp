from random import choice


def create_deck() -> list[str]:
    ranks = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
    suits = ("Hearts", "Diamonds", "Clubs", "Spades")
    deck = [f"{rank} of {suit}" for rank in ranks for suit in suits]
    return deck
def draw_top(deck: list[str], count: int=1)-> list[str]:
    return deck.pop(0)
def draw_bottom(deck: list[str], count: int=1) -> list[str]:
    return deck.pop(-1)
def draw_random(deck: list[str], count: int=1) -> list[str]:
    option = choice(deck)
    deck.remove(option)
    return option
def show(deck):
    print(deck)
deck = create_deck()
print(deck)