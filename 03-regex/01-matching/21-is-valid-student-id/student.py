# Write your code here
import re 

def is_valid_student_id(x):
    return re.fullmatch("[rsRS][0-9]{7}",x)