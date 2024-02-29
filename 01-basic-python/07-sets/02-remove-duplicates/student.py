# Write your code here
def remove_duplicates(xs):
    checker = set()
    r = []
    for x in xs:
        if x not in checker:
            r.append(x)
            checker.add(x)
    return r