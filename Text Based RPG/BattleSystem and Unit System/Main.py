# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 14:39:58 2019

@author: KuroAzai
"""


import TeamBattleSystem
class Units:
  def __init__(self,Name, HP ,Str , Agi, level):
    self.Name = Name 
    self.HP = HP 
    self.Str = Str 
    self.Agi = Agi 
    

def UnitCreator():
    #Creating the units 
    Ichigo = Units("Ichigo Kurosaki",1000,125, 150, 1)
    Renji = Units("Renji Abarai", 1500, 150, 75, 1)
    Rukia = Units("Rukia Kuchiki", 1000, 100, 100, 1)
    Hitsugaya = Units("Hitsugaya Toshiro", 2500, 150, 75, 1)
    Byakuya = Units("Byakuya Kuchiki", 2500, 200, 175 ,1 )
    
    #enemies
    hollowT1 = Units("hollow ",25, 25, 25, 1)
    hollowT2 = Units("hollow ",25, 25, 25, 1)
    MenosGrande = Units("Menos Grande ",950, 150, 25, 1)
    Ulqioura = Units("Ulqioura ",3500, 1000, 500, 1)
    Grimmjow = Units("Grimmjow ",2500, 250, 225, 1)
    
    Party = []
    EnemyParty = []
    
    #Player team
    Party.append(Ichigo)
    Party.append(Renji)
    Party.append(Rukia)
    Party.append(Hitsugaya)
    Party.append(Byakuya)
    
    #Enemy team 
    EnemyParty.append(hollowT1)
    EnemyParty.append(hollowT2)
    EnemyParty.append(MenosGrande)
    EnemyParty.append(Ulqioura)
    EnemyParty.append(Grimmjow)
    #Send created/selected units to the battle manager
    BattleManager(Party,EnemyParty)
    
def BattleManager(Party,EnemyParty):
    #Special rules 
    
    #Passing information to our battlesystem on our contestants.Battlesystem(Player,Enemy) first variable being player and second being enemy etc..
    TeamBattleSystem.Battle(Party,EnemyParty)
if __name__ == '__main__':
    UnitCreator()
     
