# Write your code here
def card_value(string):
    if str(string).lower() == "ace":
        return 1
    elif str(string).lower() == "jack":
        return 11
    elif str(string).lower() == "queen":
        return 12
    elif str(string).lower() == "king":
        return 13
    elif isinstance(string, int):
        if 2 <=string<= 10:
            return string

