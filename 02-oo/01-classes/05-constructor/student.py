class Wall:
    def __init__(self,height,depth,width):
        self.height = height
        self.width = width
        self.depth = depth
        self.volume = height * width *depth