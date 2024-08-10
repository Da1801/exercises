def indices_of(xs,condition):
    indice = []

    for index in range(len(xs)):
        if condition(xs[index]):
            indice.append(index)
    
    return indice