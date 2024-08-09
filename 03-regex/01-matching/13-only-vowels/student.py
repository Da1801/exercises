import re

def only_vowels(string):
    return re.fullmatch("[aieou]*",string)