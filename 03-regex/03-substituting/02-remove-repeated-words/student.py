# Write your code here
import re

def remove_repeated_words(string):
    return re.sub(r"(\b[A-Za-z0-9]+\b)( \1)+",r"\1",string)