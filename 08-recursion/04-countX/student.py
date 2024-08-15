def countX(text):
    if not text:
        return 0
    
    count = 0

    if text[0] == "x":
        count += 1

    return count + countX(text[1:])