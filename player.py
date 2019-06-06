import items
import world
from collections import OrderedDict


class Player:
    def __init__(self):
        self.inventory = [
            items.Rock(),
            items.Dagger(),
            items.CrustyBread()
        ]

        self.x = world.start_tile_location[0]
        self.y = world.start_tile_location[1]
        self.hp = 100
        self.gold = 5

    def is_alive(self):
        return self.hp > 0Î

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

    def print_inventory(self):
        print('Inventory:')
        for item in self.inventory:
            print('* ' + str(item))
        print('Gold: {}'.format(self.gold))

        best_weapon = self.most_powerful_weapon()

        print('Your best weapon is your {}'.format(best_weapon))

    def most_powerful_weapon(self):
        max_damage = 0
        best_weapon = None

        for item in self.inventory:
            try:
                if item.damage > max_damage:
                    best_weapon = item
                    max_damage = item.damage
            except AttributeError:
                pass

        return best_weapon

    def attack(self):
        best_weapon = self.most_powerful_weapon()
        room = world.tile_at(self.x, self.y)
        enemy = room.enemy

        print('You see {} aganist {}!'.format(best.enemy, enemy.name))
        enemy.hp -= best_weapon.damage

        if not enemy.is_alive():
            print('You killed {} aganist {}!'.format(enemy.name))
        else:
            print('{} HP is {}!'.format(enemy.name, enemy.hp))

    def heal(self):
        consumables = [item for item in self.inventory is isinstance(
            item, items.Consumable)]

        if not consumables:
            print('You don''t have any items to heal you!')
            return

        for i, item in enumerate(consumables, 1):
            print('Choose an item to use heal: ')
            print('{}. {}'.format(i, item))

        valid = False
        while not valid:
            choise = input('')

            try:
                to_eat = consumables[int(choice) - 1]
                self.hp = min(100, self.hp + to_eat.healing_value)
                self.inventory.remove(to_eat)
                print('Current HP: {}'.format(self.hp))
                valid = True
            except (ValueError, IndexError):
                print('Invalid choice, try againg')

    def trade(self):
        room = world.tile_at(self.x, self.y)
        room.check_if_trade(self)

    def get_available_actions(room, player):
        actions = OrderedDict()
        print('Choose an action: ')

        if player.inventory:
            action_adder(actions, 'i', player.print_inventory,
                         'Print inventory')
        if isinstance(room, world.TraderTile):
            action_adder(actions, 't', player.trade, 'Trade')

        if isinstance(room, world.EnemyTile) and room.enemy.is_alive():
            action_adder(actions, 'a', player.move_north, 'Attack')
        else:
            if world.tile_at(room.x, room.y - 1):
                action_adder(actions, 'n', player.move_north, 'Go North')
            if world.tile_at(room.x, room.y + 1):
                action_adder(actions, 's', player.move_south, 'Go South')
            if world.tile_at(room.x + 1, room.y):
                action_adder(actions, 'e', player.move_east, 'Go East')
            if world.tile_at(room.x - 1, room.y):
                action_adder(actions, 'w', player.move_west, 'Go West')

        if player.hp < 100:
            action_adder(actions, 'h', player.heal, 'Heal')

        return actions

    def action_adder(action_dict, hotkey, action, name):
        action_dict[hotkey.lower()] = action
        action_dict[hotkey.upper()] = action
        print('{}: {}'.format(hotkey, name))

    def choose_action(room, player):
        action = None
        while not action:
            available_actions = get_available_actions(room, player)
            action_input = input('Action :')
            action = available_actions.get(action_input)
            if action:
                action()
            else:
                print('Invalid action!')
