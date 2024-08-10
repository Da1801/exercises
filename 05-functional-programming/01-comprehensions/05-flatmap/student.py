from util import Card

def actors(movies):
    return {actor for movie in movies for actor in movie.actors}

def genres(movies):
    return {genre for movie in movies for genre in movie.genres}

def repeat_consecutive(xs,n):
    return [element for element in xs for times in range(n)]

def repeat_alternating(xs,n):
    return [element for times in range(n) for element in xs]

def cards(values,suits):
    return {Card(value,suit) for value in values for suit in suits}