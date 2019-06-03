# includes all the items the player will interact with.


class Weapon:
    name = ''
    descripiton = ''
    damage = ''

    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects.")

    def __str__(self):
        return self.name


class Rock(Weapon):
    def __init__(self):
        self.name = 'Rock'
        self.descripiton = 'A fist-sized rock, suitable for bludgeoning.'
        self.damage = 5


class Dagger(Weapon):
    def __init__(self):
        self.name = 'Dagger'
        self.descripiton = 'A small dagger with some rust. Somewhat more' \
            ' dangerous than a rock.'
        self.damage = 10


class RustySword(Weapon):
    def __init__(self):
        self.name = 'Rusty Sword'
        self.descripiton = 'This sword is showing its age, but still ' \
            'has some fight in it.'
        self.damage = 20


class LightSaber(Weapon):
    def __init__(self):
        self.name = 'LightSaber'
        self.descripiton = 'This is the Weapon of Jedi Knights. ' \
            'It ''s hard to find, hard to use. You should have to ' \
            'trained to use that. So, are you?'
        self.damage = 100