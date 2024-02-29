# Write your code here
def cakes(eggs,butter,flour):
    egg_cake = eggs // 5
    butter_cake = butter // 250
    flour_cake = flour // 250
    no_of_cake = min(egg_cake,butter_cake,flour_cake)

    return no_of_cake