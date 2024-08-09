import re

def is_dna(string):
    return re.fullmatch("[AGTC]*",string)