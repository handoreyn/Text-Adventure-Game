# includes all the items the player will interact with.


class Weapon:
    name = ''
    
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects.")

    def __str__(self):
        return self.name
