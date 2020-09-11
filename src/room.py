# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = set(items)

    def __str__(self):
        return str(self.__class__) + ": " +str(self.__dict__)
    
    def add_item(self, item):
        self.items.add(item)

    def remove_item(self, item):
        self.items.discard(item)