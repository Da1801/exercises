from util import group_by, partition

def group_by_suit(cards):
    suits = lambda card: card.suit

    return group_by(cards,suits)

def group_by_value(cards):
    values = lambda card: card.value

    return group_by(cards,values)

def partition_by_color(cards):
    suits = lambda card: card.suit in ["clubs","spades"]

    return partition(cards,suits)