# Write your code here
def median(xs):
    sorted_list= sorted(xs)
    index = len(xs)//2
    if len(sorted_list) %2 == 0:
        return (sorted_list[index-1] + sorted_list[index])/2
    else:
        return sorted_list[index]