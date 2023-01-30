class Orders():
    """Class that defines the properties for a orders object"""

    # Write the __init__ method here
    def __init__(self, id, metal_id, size_id, style_id, timestamp):
        self.id = id
        self.metalId = metal_id
        self.sizeId = size_id
        self.styleId = style_id
        self.timestamp = timestamp
        self.style = None
        self.metal = None
        self.size = None