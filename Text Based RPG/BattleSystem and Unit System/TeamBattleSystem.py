# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 14:53:11 2019

@author: KuroAzai
"""


def Battle(Player,Enemy):
    import random
    import time
    #Combine them 
    Fighters = Player + Enemy
    
    #Sort array to fastest unit to act first.
    Fighters.sort(key=lambda x: x.Agi, reverse=True)
    Player.sort(key=lambda x: x.Agi, reverse=True)
    Enemy.sort(key=lambda x: x.Agi, reverse=True)
    
    #while members are still alive keep fighting!    
    while len(Player) > 0 and len(Enemy) > 0:
        #Count remaining members
        PSize = len(Player) - 1
        ESize = len(Enemy) - 1  
        #for each character member check if they are faster 
        for x in Fighters:
            if x.HP < 1:
                continue
            #attack!
            if x in Player:
                target = random.randint(0,ESize)
                print(x.Name + " has attacked " + Enemy[target].Name + " and dealt! :" + str(x.Str / 2))
                Enemy[target].HP = Enemy[target].HP - x.Str / 2

                if Enemy[target].HP > 0:
                    pass
                else:
                    print(x.Name + " has slain " + Enemy[target].Name)
                    del Enemy[target]
                    ESize = len(Enemy) - 1  

            else:
                target = random.randint(0,PSize)
                print(x.Name + " has attacked " + Player[target].Name + " and dealt! :" + str(x.Str / 2))
                Player[target].HP = Player[target].HP - x.Str / 2

                if Player[target].HP > 0:
                    pass
                else:
                    print(x.Name + " has slain " + Player[target].Name)
                    del Player[target]
                    PSize = len(Player) - 1

            time.sleep(1)
    if len(Player) == 0 :
        print("GET REKT!!!")
    else:
        print("Clearly hacking but I'll let it pass")   