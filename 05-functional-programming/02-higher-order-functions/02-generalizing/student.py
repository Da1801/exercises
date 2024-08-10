def find(x,condition):
    for a in x:
        if condition(a):
            return a
    
    return None