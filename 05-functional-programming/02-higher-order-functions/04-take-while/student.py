def take_while(xs,condition):
    x = 0
    while x< len(xs) and condition(xs[x]) :
        x+= 1
    return(xs[:x],xs[x:])
