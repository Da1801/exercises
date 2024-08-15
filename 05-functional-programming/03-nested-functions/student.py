from util import count, indices_of

def count_older_than(people,min_age):
    def age(person):
        return person.age >= min_age
    
    return count(people,age)

def indices_of_cards_with_suit(cards,suit):
    def equal_suit(card):
        return card.suit == suit
    
    return indices_of(cards,equal_suit)