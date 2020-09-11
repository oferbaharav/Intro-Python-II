# Write a class to hold player information, e.g. what room they are in
# currently.



class Player:
    def __init__(self, room):
        self.room = room
        self.items = set()

    def __str__(self):
        return str(self.__class__) + ": " +str(self.__dict__)

    def add_item(self, item):
        self.items.add(item)

    def remove_item(self, item):
        self.items.discard(item)
        
        