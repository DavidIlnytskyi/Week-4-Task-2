'''This module contains classes for a game'''
class Room:
    def __init__(self, name):
        self._description = None
        self._linked_rooms = dict()
        self.enemies = []
        self._name = name
        self._item = None
        self._weapon = None

    def get_name(self):
        return self._name

    def set_description(self, description):
        self._description = description

    def get_description(self):
        return self._description

    def link_rooms(self, location, room):
        self._linked_rooms[location] = room

    def get_rooms(self):
        return self._linked_rooms.keys()

    def go_to_room(self, place):
        if place in self._linked_rooms:
            return self._linked_rooms[place]
        else:
            return 'You can\'t go in that way'

    def set_enemy(self, enemy):
        self._enemy = enemy

    def get_enemy(self):
        return self._enemy

    def get_info(self):
        print(self._name + '\n' + '------------------' + '\n' + self._description +'\n' + '------------------' + '\n' + 'You can go here: ')
        if self._linked_rooms:
            for location in self._linked_rooms:
                print(f'Write {location} to go to the {self._linked_rooms[location].get_name()}')
        if self.get_weapon() is not None:
            print('------------------')
            self.get_weapon().describe()
        if self.get_enemy() != None:
            print('------------------' + '\n' + 'Located enemy:')
            print(self.get_enemy().get_name() + '\n' + self.get_enemy().get_description() + '\n' + f'Attack rate is: {self.get_enemy().get_attack_rate()}')
            self.get_enemy()

        print('\nYou have next abilities: \nfight \ntake \nwalk(using specific commands)\ninfo')


    def get_weapon(self):
        return self._weapon

    def set_weapon(self, weapon):
        self._weapon = weapon

    def get_item(self):
        return self._item

class BossRoom(Room):
    def __init__(self, name):
        super().__init__(name)

    def quest(self):
        pass



class Hero:
    def __init__(self, name):
        self._description = None
        self._weapon = None
        self._item = None
        self.dead = False
        self._health = 100
        self._attack_rate = 1
        self._name = name
        self._weapons = dict()

    def set_weapon(self, weapon):
        self._weapon = weapon
        self._weapons[weapon.get_name()] = weapon

    def get_weapon(self):
        return self._weapon

    def get_weapons(self):
        return self._weapons

    def set_description(self, description):
        self._description = description

    def lose_health(self, lose):
        self._health = self._health - lose

    def get_description(self):
        return self._description

    def set_item(self, item):
        self._item = item

    def get_hp(self):
        return self._health

    def describe(self):
        print(f'My hp is: {self.get_hp()}' + '\n' + f'My weapon is {self._weapon}' + '\n' f'I have {([{element} for element in self._weapons] + [self._item.name])} in my backpack.')


class Friend(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.advices = list()

    def set_advise(self, advise):
        self.advices.append(advise)

    def get_advise(self):
        return




class StartMonster:
    def __init__(self, name):
        self._name = name
        self._health = 10
        self._attack_rate = 5
        self._description = None

    def get_name(self):
        return self._name

    def set_weapon(self, weapon_name):
        self._attack_rate += weapon_name.get_attack_rate()
        self._weapon = weapon_name

    def get_weapon(self):
        return self._weapon

    def set_health(self, health_points):
        self._health = health_points

    def lose_health(self, lose):
        self._health = self._health - lose

    def get_health(self):
        return self._health

    def set_attack_rate(self, attack_rate):
        self._attack_rate = attack_rate

    def get_attack_rate(self):
        return self._attack_rate

    def set_description(self, desc):
        self._description = desc

    def get_description(self):
        return self._description

    def get_attack(self):
        return self._attack_rate

class MediumMonster(StartMonster):
    def __init__(self, name):
        super().__init__(name)

    def set_second_weapon(self, second_weapon):
        self._second_weapon = second_weapon

    def get_second_weapon(self):
        return self._second_weapon

class FinalBoss(MediumMonster):
    def __init__(self, name):
        super().__init__(name)

    def set_ult(self, ult_name, damage):
        self._ult_name = ult_name
        self._ult_damage = damage

    def get_ult(self):
        return (self._ult_name, self._ult_damage)

class Item:
    '''This class represents an item'''
    def __init__(self, name):
        '''This function contains variables'''
        self.name = name
        self.description = ''

    def set_description(self, description):
        '''This function sets description for item'''
        self.description = description

    def describe(self):
        '''This function describes an item'''
        return f'The [{self.name}] is here - {self.description}'

    def get_name(self):
        '''This function gets name of an item'''
        return self.name

class Weapon(Item):
    def __init__(self, name):
        super().__init__(name)
        self._attack_rate = 10

    def set_attack_rate(self, attack_rate):
        self._attack_rate = attack_rate

    def get_attack_rate(self):
        return self._attack_rate

    def describe(self):
        '''This function describes a weapon'''
        print(f'The [{self.name}] is here - {self.description}\nAttack Rate: {self._attack_rate}')


    def __repr__(self):
        return self.get_name()
