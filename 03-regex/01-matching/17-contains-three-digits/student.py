import re

def contains_three_digits(string):
    return re.search("[0-9\s*]{3,}",string)