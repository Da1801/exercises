def closest(points, target_point):
    def distance_between_two_points(point):
        x , y = point
        return (x - a)**2 + (y-b)**2
    
    a,b = target_point
    
    return min(points,key=distance_between_two_points)