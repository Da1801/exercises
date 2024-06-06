def countX(text):
    if not text:
        return 0
    first_of_x = 0
    if text[0]== "x":
        first_of_x += 1
    

    return first_of_x + countX(text[1:])