#Variables
health = 80
troll = 60
turn = 1
potion = 2
tpotion = 1
Attack = 15
Exp = 0
bonus = 0
Total = 80
Level = 1
battle =  1
buy = 2
money = 200
sword = 0
enemy = "Troll"
outside = 1
gal = 1
eattack = 20
backup = 20
potionv =  25
tpotionv =  20
balls = 1
armour = 0
maxp = 1
flash = 1
skip = 3
bought = 1
mp = 0
lol = 0
lol2 = 0
bonus2 = 10000
buying = 1
spell1 = "Nothing Equipped"
spell2 = "Nothing Equipped"
fire = "unequipped"
ice = "unequipped"
poison = "unequipped"
sharpen = "unequipped"
harden = "unequipped"
tempa = 0
tempd = 0

#Intro
print "Hello, brave adventurer.  Welcome to Furry's World, home to fearsome creatures."
name = raw_input("What's your name?: ")
print "Prepare yourself, " + name + "."
raw_input()
print "You find yourself in a dark room.  You look around, but can't see anything."
raw_input()
print "Suddenly, light fills the room and a figure looms before you."
raw_input()

while 1:
    print enemy + " Aproaches!"
    raw_input()

#Battle:
    #Start
    if 1:
        inven = ["Potion","Potion", "Max Potion", "Back"]
        turn = 1
        health = 80 + bonus
        base = health
        mp = 40 + bonus2
        troll = 60 + bonus * 2
        tpotion = 1
        eattack = eattack - armour
        estatus = "healthy"
        tempa = 0
        tempd = 0
        if eattack < 10:
            eattack = 10
        copy4 = str(Level)
        copy8 = str(potionv)
        copy9 = str(mp)
        print "Level " + copy4
        while troll > 0 and health > 0:
            copy3 = str(Attack + sword + tempa)
            if turn == 1 and health > 0 and lol == 0:
                copy1 = str(health)
                print name + "'s Turn"
                print "HP " + copy1
                print "MP " + copy9
                dbug1 = raw_input()
                if dbug1 == "die":
                    troll = 0
                else:
                    pass

    #Your Turn---------------------------------------------------------------
                do = raw_input("| Attack | Item | Magic |: ")
                do = do.lower()
                if do == "attack":
                    turn = 2
                    troll = troll - Attack - sword - tempa
                    if skip != 3:
                        skip = skip + 1
                    else:
                        pass
                    print copy3 + " damage to " + enemy
                    raw_input()
        
                elif do == "item":
                    use = raw_input("| Potion " * potion + "| Max Potion " * maxp + "| Flash Bomb " * flash + " | Back |: ")
                    use = use.lower()
                    if use == "potion" and potion > 0:
                        health = health + potionv
                        potion = potion - 1
                        if skip != 3:
                            skip = skip + 1
                        else:
                            pass
                        print name + " recovered " + copy8 + " HP"
                        raw_input()
                        if health > base:
                            health = base
                            turn = 2
                        else:
                            turn = 2
                    elif use == "max potion" and maxp > 0:
                        maxp = maxp - 1
                        health = base
                        if skip != 3:
                            skip = skip + 1
                        else:
                            pass
                        print name + " used Max Potion"
                        print "Health fully restored"
                        raw_input()
                        turn = 2
                    elif use == "flash bomb" and flash > 0:
                        skip = 1
                        turn = 2
                        flash = flash - 1
                        print "Poof!"
                        print enemy + "'s turn was skipped"
                    elif use == "back":
                        pass
                    else:
                        pass
                elif do == "magic":
                    cast = raw_input("| " + spell1 + " | " + spell2 + " |: ")
                    cast = cast.lower()
                    if cast == "fire" and mp >= 30 and fire == "equipped":
                        print "Fire!"
                        raw_input()
                        print enemy + "'s health was cut in half"
                        print "Skip your next turn"
                        troll = troll/2
                        mp = mp - 30
                        lol = 1
                        turn = 2
                        raw_input()
                    elif cast == "ice" and mp >= 50 and ice == "equipped":
                        eattack = eattack/2
                        mp = mp - 50
                        lol = 1
                        turn = 2
                        print enemy + "'s attack was cut in half"
                        print "Skip your next turn"
                        raw_input()
                    elif cast == "poison" and mp >= 75 and poison == "equipped":
                        mp = mp - 75
                        estatus = "poisoned"
                        lol = 1
                        turn = 2
                        print enemy + " was poisoned"
                        print "Skip your next turn"
                        raw_input()
                    elif cast == "sharpen" and mp >= 50 and sharpen == "equipped":
                        mp = mp - 50
                        tempa = 20
                        lol = 1
                        turn = 2
                        print "Attack increased"
                        print "Skip your next turn"
                        raw_input()
                    elif cast == "harden" and mp >= 50 and harden == "equipped":
                        mp = mp - 50
                        tempd = 10
                        lol = 1
                        turn = 2
                        eattack = eattack - tempd
                        print "Defense increased"
                        print "Skip your next turn"
                        raw_input()
                    elif cast == "poison" and mp < 75:
                        print "Not enough MP"
                    else:
                        pass
                if skip != 3:
                    turn = 1
                else:
                    pass
    #Enemy's turn-------------------------------------------------------
            elif turn == 2 and troll > 0 and skip == 3:
                if estatus == "poisoned":
                    copy10 = str(int(round(troll - troll * 0.9)))
                    troll = troll * 0.9
                    troll = int(troll)
                    print enemy + " was hurt by poison"
                    raw_input()
                    print copy10 + " damage"
                    
                else:
                    pass
                if lol ==  1:
                    lol2 = lol2 + 1
                else:
                    pass
                if lol2 == 2:
                    lol = 0
                    lol2 = 0
                copy2 = str(troll)
                copy5 = str(eattack)
                copy6 = str(eattack/2)
                print enemy + " 's Turn"
                print "HP " + copy2
                raw_input()
                if troll <= Attack + sword and tpotion == 1:
                    print enemy + " used potion"
                    raw_input()
                    print enemy + " recovered " + copy8 + " HP"
                    raw_input()
                    tpotion = tpotion - 1
                    troll = troll + potionv
                    print troll
                    turn = 1
                    if lol == 1:
                        turn = 2
                    else:
                        pass
                else:
                    print enemy + " attacks!"
                    print copy5 + " Damage to " + name
                    health = health - eattack
                    raw_input()
                    turn = 1
                    if lol == 1:
                        turn = 2
                    else:
                        pass
#End        

    if troll <= 0:
        print enemy + " Defeated"
        print "Exp + 45"
        print "Money + 45"
        raw_input()
        money = money + 45
        eattack = eattack + tempd + armour
        Exp = Exp + 45
        turn = 1
        outside = 1
        health = 80 + bonus
        mp = 40 + bonus2
        if Exp >= Total:
            Attack = Attack + 5
            armour = armour + 3
            bonus =  bonus + 15
            health = 100 + bonus
            Total = Total  + 20
            Level = Level + 1
            bonus2 = bonus2 + 15
            eattack = eattack + eattack * .5
            eattack = int(round(eattack))
            Exp = 0
            tpotion = tpotion + 15
            potionv = potionv + 15
            print "Level Up!"
            raw_input()
            print "Attack +5"
            print "HP +5"
            print "MP +10"
            raw_input()
        else:
            pass
    elif health <= 0 and gal == 1:
        while 1:
            print "Game Over"
    else:
        print "You lost"
#Enemies----------------------------------------------------------------
    if Level == 4:
        enemy = "Dragon"
    elif Level == 10:
        enemy = "Warlord"
    elif Level == 15:
        enemy = "Demi-God"
    elif Level == 20:
            enemy = "Dungeon Master"
    else:
        pass
#Escape               
    if gal == 1:
        enemy = "Warrior"
        print "Phew, that was close"
        raw_input()
        print "You exit the dark room and find yourself in a basement of a store"
        print "Welcome to the Overworld"
        gal = 2
    else:
        pass

    #Store-------------------------------------------------------------

    while outside == 1:
        life = raw_input("| Store | Arena | Stats |: ")
        life = life.lower()
        if life == "arena":
            outside = 0
            turn = 1
        elif life == "stats":
            copybleh = "$" + str(money)
            copyy = str(armour)
            print "Level"
            print Level
            print ""
            print "Money"
            print copybleh
            print ""
            print "Attack"
            print Attack + sword
            print ""
            print "Defense"
            print armour
            print ""
            print "Health"
            print health
            print ""
            print "Exp to Next Level"
            print Total - Exp
            print ""
            print "Magic"
            print mp + bonus2
            print ""
            print "Spells"
            print "| " + spell1 + " | " + spell2 + " |"
            print ""
            print "Inventory"
            print "| Potion " * potion + "| Max Potion " * maxp + "| Flash Bomb " * flash + "|"
            raw_input()
            
        elif life == "store":
            buy = 1
            while buy == 1:
                store = raw_input("| Items | Spells | Leave |: ")
                store = store.lower()
                if store == "items":
                    la = 1
                    while la == 1:
                        bitem = raw_input("| Potion-$30 | Max Potion-$200 | Sword Upgrade-$150 | Armour Upgrade-$200 | Flash Bomb-$100 | Back |: ")
                        bitem = bitem.lower()
                        if bitem == "potion" and money >= 30:
                            money = money - 30
                            potion = potion + 1
                            bought = 2
                            print "Thanks!"
                            raw_input()
                        elif bitem == "sword upgrade" and money >= 150:
                            money =  money - 150
                            sword = sword + 10
                            bought = 2
                            print "Thanks!"
                            raw_input()
                        if bitem == "flash bomb" and money >= 100:
                            flash = flash + 1
                            money = money - 100
                            bought = 2
                            print "Thanks!"
                            raw_input()
                        elif bitem == "armour upgrade" and money >= 200:
                            money = money - 200
                            armour = armour + 5
                            bought = 2
                            print "Thanks!"
                            raw_input()
                        elif bitem == "max potion" and money >= 200:
                            maxp = maxp + 1
                            money = money - 200
                            bought = 2
                            print "Thanks!"
                            raw_input()
                        elif bitem == "back":
                            la = 2
                        elif bitem == "sword upgrade" and money < 150 or bitem == "potion" and money < 30 or "armour upgrade" and money < 200 or bitem == "max potion" and money < 200 or bitem == "flash bomb" and money < 100:
                            if bought == 1:
                                print "Hey!  You don't have enough money!"
                                raw_input()
                            else:
                                pass
                        else:
                            pass
                elif store == "spells":
                    lal = 1
                    while lal == 1:
                            bspell = raw_input("| Fire-$125-30MP | Ice-$150-50MP | Poison-$200-75MP | Sharpen-$100-50MP | Harden-$100-50MP | Back |: ")
                            bspell = bspell.lower()
                            if bspell == "back":
                                lal = 2
                            elif bspell == "fire" and money >= 125:
                                choice = raw_input("| Slot One | Slot Two | Cancel |: ")
                                choice = choice.lower()
                                buying = 1
                                money = money - 125
                                while buying == 1:
                                    if choice == "slot one" and spell1 != "Fire" or spell2 != "Fire":
                                        spell1 = "Fire"
                                        buying = 2
                                        la = 2
                                        fire = "equipped"
                                        print "Thanks!"
                                        raw_input()
                                    elif choice == "slot two" and spell1 != "Fire" or spell2 != "Fire":
                                        spell2 = "Fire"
                                        buying = 2
                                        la = 2
                                        fire = "equipped"
                                        print "Thanks!"
                                        raw_input()
                                    elif choice == "cancel":
                                        buying = 2
                                        la = 2
                                    else:
                                        pass
                            elif bspell == "ice" and money >= 150:
                                choice = raw_input("| Slot One | Slot Two | Cancel |: ")
                                choice = choice.lower()
                                buying = 1
                                money = money - 150
                                while buying == 1:
                                    if choice == "slot one" and spell1 != "Ice" or spell2 != "Ice":
                                        spell1 = "Ice"
                                        buying = 2
                                        la = 2
                                        ice = "equipped"
                                        print "Thanks!"
                                        raw_input()
                                    elif choice == "slot two" and spell1 != "Ice" or spell2 != "Ice":
                                        spell2 = "Ice"
                                        buying = 2
                                        la = 2
                                        ice = "equipped"
                                        print "Thanks!"
                                        raw_input()
                                    elif choice == "cancel":
                                        buying = 2
                                    else:
                                        pass
                            elif bspell == "poison" and money >= 150:
                                choice = raw_input("| Slot One | Slot Two | Cancel |: ")
                                choice = choice.lower()
                                buying = 1
                                money = money - 150
                                while buying == 1:
                                    if choice == "slot one" and spell1 != "Poison" or spell2 != "Poison":
                                        spell1 = "Poison"
                                        buying = 2
                                        la = 2
                                        poison = "equipped"
                                        print "Thanks!"
                                        raw_input()
                                    elif choice == "slot two" and spell1 != "Poison" or spell2 != "Poison":
                                        spell2 = "Poison"
                                        buying = 2
                                        la = 2
                                        poison = "equipped"
                                        print "Thanks!"
                                        raw_input()
                                    elif choice == "cancel":
                                        buying = 2
                                    else:
                                        pass
                            elif bspell == "sharpen" and money >= 150:
                                choice = raw_input("| Slot One | Slot Two | Cancel |: ")
                                choice = choice.lower()
                                buying = 1
                                money = money - 150
                                while buying == 1:
                                    if choice == "slot one" and spell1 != "Sharpen" or spell2 != "Sharpen":
                                        spell1 = "Sharpen"
                                        buying = 2
                                        la = 2
                                        sharpen = "equipped"
                                        print "Thanks!"
                                        raw_input()
                                    elif choice == "slot two" and spell1 != "Sharpen" or spell2 != "Sharpen":
                                        spell2 = "Sharpen"
                                        buying = 2
                                        la = 2
                                        sharpen = "equipped"
                                        print "Thanks!"
                                        raw_input()
                                    elif choice == "cancel":
                                        buying = 2
                                    else:
                                        pass
                            elif bspell == "harden" and money >= 150:
                                choice = raw_input("| Slot One | Slot Two | Cancel |: ")
                                choice = choice.lower()
                                buying = 1
                                money = money - 150
                                while buying == 1:
                                    if choice == "slot one" and spell1 != "Harden" or spell2 != "Harden":
                                        spell1 = "Harden"
                                        buying = 2
                                        la = 2
                                        harden = "equipped"
                                        print "Thanks!"
                                        raw_input()
                                    elif choice == "slot two" and spell1 != "Harden" or spell2 != "Harden":
                                        spell2 = "Harden"
                                        buying = 2
                                        la = 2
                                        harden = "equipped"
                                        print "Thanks!"
                                        raw_input()
                                    elif choice == "cancel":
                                        buying = 2
                                    else:
                                        pass
                            elif bspell == "fire" and money < 125 or bspell == "ice" and money < 150 or bspell == "poison" and money < 200 or bspell == "harden" and money < 100 or bspell == "sharpen" and money < 100:
                                print "Hey!  You don't have enough money!"
                            else:
                                pass
                elif store == "leave":
                    buy = 2
                    if spell1 != "Fire" and spell2 != "Fire":
                        fire = "unequipped"
                    elif spell1 != "Ice" and spell2 != "Ice":
                        ice = "unequipped"
                    elif spell1 != "Poison" and spell2 != "Poison":
                        poison = "unequipped"
                    elif spell1 != "Sharpen" and spell2 != "Sharpen":
                        sharpen = "unequipped"
                    elif spell1 != "Harden" and spell2 != "Harden":
                        harden = "unequipped"
                else:
                    pass
            