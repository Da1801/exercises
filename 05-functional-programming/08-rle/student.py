def rle_encode(data):
    if not data:
        return []
    
    data = iter(data)

    
    try:
        char = next(data)
        count = 1    
        for x in data:
            if x == char:
                count += 1

            else:
                yield(char,count)
                char = x
                count = 1
        yield (char,count)
        
    except StopIteration:
        pass
        
    

def rle_decode(data):
    decoded_string = ""
    for char, count in data:
        decoded_string += char * count
   
    return decoded_string
