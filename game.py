'''Module for game'''
class Enemy:
    '''
    class for Enemies
    >>> tabitha = Enemy("Tabitha", "An enormous spider with countless eyes and furry legs.")
    >>> tabitha.set_conversation("Sssss....I'm so bored...")
    >>> tabitha.describe()
    Tabitha is here !
    An enormous spider with countless eyes and furry legs.
    >>> dave = Enemy("Dave", "A smelly zombie")
    >>> dave.set_conversation("What's up, dude! I'm hungry.")
    >>> dave.set_weakness("cheese")
    >>> dave.describe()
    Dave is here !
    A smelly zombie
    '''
    def __init__(self, name, description, defeat = []) -> None:
        '''
        Inits class objects
        '''
        self.name = name
        self.description = description
        self.conversation = None
        self.weakness = None
        self.defeat = defeat
        self.chosen_fight = None
    def describe(self):
        '''
        Returns description of an enemy
        '''
        if self.name != None:
            vuvid = ''
            vuvid = vuvid + f'{self.name} is here !' + '\n'
            vuvid += f'{self.description}'
            print(vuvid)
    def set_conversation(self, phrase):
        '''
        Sets phrase for enemies conversation
        '''
        self.conversation = phrase
    def set_weakness(self, weakness):
        '''
        Sets weakness for enemy
        '''
        self.weakness = weakness

    def fight(self, fight_with):
        self.chosen_fight = fight_with
        if self.weakness == self.chosen_fight:
            self.defeat.append(1)
            self.name = None
            return True
        return False
    
    def get_defeated(self):
        '''
        Counts number of defeated enemies 
        '''
        return len(self.defeat)
    
    def talk(self):
        '''
        Returns enemies phrase
        '''
        print(self.conversation)

class Item:
    '''
    class for items
    >>> book = Item("book")
    >>> book.set_description("A really good book entitled 'Knitting for dummies'")
    >>> book.description
    "A really good book entitled 'Knitting for dummies'"
    >>> book.describe()
    The [book] is here - A really good book entitled 'Knitting for dummies'
    '''
    def __init__(self, name, description = None) -> None:
        '''
        Inits class objects
        '''
        self.name= name
        self.description = description
    def set_description(self, description):
        '''
        Sets item's description
        '''
        self.description = description
    def __repr__(self) -> str:
        '''
        Represents class
        '''
        return f"Item('{self.name}')"
    def describe(self):
        '''
        Describes item
        '''
        vuvid = f'The [{self.name}] is here - {self.description}'
        print(vuvid)    
    def get_name(self):
        '''
        Returns item's name
        '''
        return self.name

class Room:
    '''
    class for rooms
    >>> kitchen = Room("Kitchen")
    >>> kitchen.set_description("A dank and dirty room buzzing with flies.")
    >>> dining_hall = Room("Dining Hall")
    >>> dining_hall.set_description("A large room with ornate golden decorations on each wall.")
    >>> ballroom = Room("Ballroom")
    >>> ballroom.set_description("A vast room with a shiny wooden floor.\
 Huge candlesticks guard the entrance.")
    >>> book = Item("book")
    >>> book.set_description("A really good book entitled 'Knitting for dummies'")
    >>> dining_hall.set_item(book)
    >>> kitchen.link_room(dining_hall, "south")
    >>> kitchen.to_go
    [[Room("Dining Hall"), 'south']]
    >>> dining_hall.link_room(kitchen, "north")
    >>> dining_hall.link_room(ballroom, "west")
    >>> dining_hall.to_go
    [[Room("Kitchen"), 'north'], [Room("Ballroom"), 'west']]
    >>> dave = Enemy("Dave", "A smelly zombie")
    >>> dave.set_conversation("What's up, dude! I'm hungry.")
    >>> dining_hall.set_character(dave)
    >>> dining_hall.get_item()
    Item('book')
    '''
    def __init__(self, room, description = None, enemy = None) -> None:
        '''
        Inits class objects
        '''
        self.room = room
        self.item = None
        self.next_room = []
        self.to_go = []
        self.enemy = enemy
        self.description = description
    def __repr__(self) -> str:
        '''
        Represent class
        '''
        return f'Room("{self.room}")'
    def set_description(self, description):
        '''
        Returns description of the class
        '''
        self.description = description
    def set_character(self, monster):
        self.enemy = monster
    def link_room(self, to_go, to_turn)-> list:
        '''
        Returns list with available rooms to go
        '''
        self.next_room.append([self.room, to_go, to_turn])
        self.to_go = []
        for elem in self.next_room:
            if self.room in elem:
                self.to_go.append(elem[1:])

    def set_item(self, item):
        '''
        Sets available items for the room
        '''
        self.item = item
    def get_details(self):
        '''
        Returns details of each room 
        '''
        vuvid = ''
        vuvid += str(self.room) +'\n'
        vuvid += '----------------------------------------------------' +'\n'
        vuvid = vuvid+ str(self.description) + '\n'
        if self.to_go != []:
            for elem in self.to_go[:-1]:
                vuvid += f'The {elem[0].room} is {elem[1]}' + '\n'
            vuvid += f'The {self.to_go[-1][0].room} is {self.to_go[-1][1]}'
        print(vuvid)
    def get_character(self):
        '''
        Returns enemie's name
        '''
        return self.enemy
    def get_item(self):
        '''
        Returns item's name
        '''
        return self.item
    def move(self, command):
        '''
        Returns name of room to go
        '''
        for elem in self.to_go:
            if command in elem:
                return elem[0]


if __name__=="__main__":
    import doctest
    print(doctest.testmod())
