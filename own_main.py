from own_game import *
import time
# Main hero
main_character = Hero('UCUshnik')

# All available monsters

dementor = MediumMonster('Dementor')
dementor.set_attack_rate(18)
dementor.set_health(20)
dementor.set_description('Dementors are dark, ominous creatures \
that drain the souls of their victims by \
giving them the worst case of depression \
they\'ve ever experienced. \nIt\'s like talking\
 to an ex after a bad break-up – but instead of\
 just emotionally draining you, they\'ll also\
 suck your soul out!')
kiss = Weapon('Kiss')
dementor.set_weapon(kiss)


piglin = StartMonster('Piglin')
piglin.set_attack_rate(7)
piglin.set_health(10)
piglin.set_description('Minecraft\'s piglins: \
think greedy, gold-obsessed goblins who somehow \
wound up in the nether.')
gold_sword = Weapon('Gold sword')
gold_sword.set_attack_rate(4)
piglin.set_weapon(gold_sword)


killjoy = StartMonster('KillJoy')
killjoy.set_attack_rate(6)
killjoy.set_health(8)
killjoy.set_description('When life gives you lemons, Killy Joy shoots them with her turrets.')
turret = Weapon('Turret')
turret.set_attack_rate(10)
killjoy.set_weapon(turret)

moonlord = FinalBoss('Moon lord')
moonlord.set_attack_rate(25)
moonlord.set_health(50)
moonlord.set_description('Moonlord is a towering behemoth \
with eyes that glow like the fires of hell and tentacles \
that writhe with insatiable hunger. None who have faced \
him have lived to tell the tale...except for one brave \
adventurer who managed to defeat him with nothing but a \
stick of gum and a yoyo.')
spheres = Weapon('Phantasmal Spheres')
spheres.set_attack_rate(15)
moonlord.set_weapon(spheres)

print(dementor.get_description())

# All locations information
pasichna = Room('Pasichna street')
pasichna.set_enemy(killjoy)
pasichna.set_description('That is great street with big plans for future... Btw, there are too many valorant players here!')
vandal = Weapon('Vandal')
vandal.set_attack_rate(35)
vandal.set_description('One shot to the head and you are dead!')
pasichna.set_weapon(vandal)

zelena = Room('Zelena street')
zelena.set_description('This street if full of green colors. And Minecraft players. Maybe, you will try to find a fried here?')
diamond_sword = Weapon('Diamond Sword')
diamond_sword.set_attack_rate(11)
diamond_sword.set_description('There is a myth, that gold sword is faster... Nah, try this...')
zelena.set_weapon(diamond_sword)
zelena.set_enemy(piglin)

shevschenka = Room('Shevchenka street')
shevschenka.set_description('I am feeling here like in Harry Potter novel! Interesting why...')
shevschenka.set_enemy(dementor)
magic_stick = Weapon('Magic stick')
magic_stick.set_description('This thing has helped to beat Voldemort. Maybe its useful.')
magic_stick.set_attack_rate(21)
shevschenka.set_weapon(magic_stick)

kozelnytska = BossRoom('Kozelnytska street')
kozelnytska.set_description('While there is day on the other streets, kozelnytska is covered with darkness. Be careful here!')
kozelnytska.set_enemy(moonlord)
help = Item('Help book')
help.set_description('Take some luck with you, because you will need that!')

# kozelnytska.

# All connections between locations

shevschenka.link_rooms('forward', zelena)
zelena.link_rooms('backward', shevschenka)

zelena.link_rooms('forward', kozelnytska)
kozelnytska.link_rooms('backward', zelena)

zelena.link_rooms('right', pasichna)
pasichna.link_rooms('left', zelena)

# Current room

current_room = shevschenka

# Goodluck

main_character.set_item(help)

while not main_character.dead:
    print('\n')
    inhabitant = current_room.get_enemy()
    current_room.get_info()
    input_data = input('> ')

    if input_data == 'talk':
        pass
    elif input_data in {'forward', 'backward', 'right', 'left'}:
        if input_data in current_room.get_rooms():
            current_room = current_room.go_to_room(input_data)
        else:
            print('You can\'t go here ')
    elif input_data == 'fight':
        print()
        if current_room.get_enemy() != None:
            while current_room.get_enemy().get_health() > 0 and main_character.get_hp() > 0:
                if main_character.get_weapons():
                    print(f'In your backpack you have {[(", ").join([element for element in main_character.get_weapons()])]}.')
                    weapon = input('Choose your weapon from backpack: ')
                    if weapon in [element for element in main_character.get_weapons()]:
                        weapon = main_character.get_weapons()[weapon]
                        current_room.get_enemy().lose_health(weapon.get_attack_rate())
                        if current_room.get_enemy().get_health() > 0:
                            main_character.lose_health(current_room.get_enemy().get_attack())
                            print(f'You have gained {current_room.get_enemy().get_attack()} damage')
                        print('Enemy has gained ' + str(weapon.get_attack_rate()) + ' damage.')
                        if current_room.get_enemy().get_health() > 0:
                            print(current_room.get_enemy().get_name() + ' health is ' + str(current_room.get_enemy().get_health()) + '\n')
                        else:
                            print(current_room.get_enemy().get_name() + ' is dead!')
            if current_room.get_enemy().get_health() <= 0:
                current_room.set_enemy(None)
            else:
                main_character.dead = True
        else:
            print('There is no one to fight with')

    elif input_data == "take":
        if current_room.get_weapon() is not None:
            print("You put the " + current_room.get_weapon().get_name() + " in your backpack")
            if isinstance (current_room.get_weapon(), Weapon):
                main_character.set_weapon(current_room.get_weapon())
                current_room.set_weapon(None)

        else:
            print("There's nothing to take here!")
    elif input_data == 'info':
        main_character.describe()
    time.sleep(5)
