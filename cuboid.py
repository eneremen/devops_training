class Cuboid():
    """
    This class represents a cuboid which will have height, width and depth.
    """

    def __init__(self, height, width, depth):
        self.height = height
        self.width = width
        self.depth = depth

    def volume(self):
        """
        This method will calculate the volume of the cuboid.
        volume = height * width * depth
        >>> cuboid = Cuboid(2, 3, 4)
        >>> cuboid.volume()
        24
        """
        total_volume = self.height * self.width * self.depth
        return round(total_volume, 2)

    def surface(self):
        """
        This method will calculate the surface area of the cuboid.
        surface = 2(ab+ac+bc)
        >>> cuboid = Cuboid(2, 3, 4)
        >>> cuboid.surface()
        52
        """
        total_surface = 2 * (self.height*self.width + self.height*self.depth + self.width*self.depth)
        return round(total_surface, 2)
