class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return str(self.__class__) + ": " +str(self.__dict__)