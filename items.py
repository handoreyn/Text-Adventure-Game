# includes all the items the player will interact with.


class Weapon:
    name = ''
    descripiton = ''
    damage = 0
    value = 0

    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects.")

    def __str__(self):
        return self.name


class Rock(Weapon):
    def __init__(self):
        self.name = 'Rock'
        self.descripiton = 'A fist-sized rock, suitable for bludgeoning.'
        self.damage = 5
        self.value = 1


class Dagger(Weapon):
    def __init__(self):
        self.name = 'Dagger'
        self.descripiton = 'A small dagger with some rust. Somewhat more' \
            ' dangerous than a rock.'
        self.damage = 10
        self.value = 20


class RustySword(Weapon):
    def __init__(self):
        self.name = 'Rusty Sword'
        self.descripiton = 'This sword is showing its age, but still ' \
            'has some fight in it.'
        self.damage = 20
        self.value = 100


class LightSaber(Weapon):
    def __init__(self):
        self.name = 'LightSaber'
        self.descripiton = 'This is the Weapon of Jedi Knights. ' \
            'It ''s hard to find, hard to use. You should have to ' \
            'trained to use that. So, are you?'
        self.damage = 100
        self.value = 500


class Consumable:
    def __init__(self):
        raise NotImplementedError('Do not create raw Consumable objects.')

    def __str__(self):
        return '{} (+{} HP)'.format(self.name, self.healing_value)


class CrustyBread(Consumable):
    def __init__(self):
        self.name = 'Crusty Bread'
        self.healing_value = 10
        self.value = 12


class Apple(Consumable):
    def __init__(self):
        self.name = 'Apple'
        self.healing_value = 10
        self.value = 12


class SprintWater(Consumable):
    def __init__(self):
        self.name = 'Spring Water'
        self.healing_value = 12
        self.value = 13


class HealingPotion(Consumable):
    def __init__(self):
        self.name = 'Healing Potion'
        self.healing_value = 50
        self.value = 60


class NonPlayableCharacter():
    def __init__(self):
        raise NotImplementedError('Do not create raw NPC objects.')

    def __str__(self):
        return self.name


class Trader(NonPlayableCharacter):
    def __init__(self):
        self.name = 'Trader'
        self.gold = 100
        self.inventory = [items.CrustyBread(),
                          items.CrustyBread(),
                          items.CrustyBread(),
                          items.HealingPotion(),
                          items.HealingPotion()]
