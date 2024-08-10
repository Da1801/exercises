def merge_dictionaries(d1,d2,merge_function):
    result = {}

    for k ,v in d1.items():
        result[k]= v
        for l , n in d2.items():
            if k == l:
                result[k]= merge_function(result[k],n)
            else:
                result[l]= n

    return result
                