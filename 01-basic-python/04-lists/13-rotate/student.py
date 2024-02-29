# Write your code here
def rotate(xs,n):
    for k in range(n):
        x = xs.pop(0)
        xs.append(x)