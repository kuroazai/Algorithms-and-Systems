# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 17:55:16 2019

@author: KuroAzai
"""
class Units:
    
    def __init__(self,Name, HP, Atk, Arm,Spd, location, Faction):
        self.Name = Name 
        self.HP = HP
        self.Atk = Atk
        self.Arm = Arm
        self.Spd = Spd
        self.location = location
        self.Faction = Faction


class Locations:
    
    def __init__(self,Name, Attackers, Defenders, Owner):
        self.Name = Name 
        self.Attackers = Attackers
        self.Defenders = Defenders
        self.Owner = Owner

class Factions:
    
    def __init__(self,Name, Units, Territories):
        self.Name = Name 
        self.Units = Units
        self.Territories = Territories

def NewGame():
    #Factions
    Demacia = Factions("Demacia", Units = [] , Territories = [])
    Piltover = Factions("Piltover", Units = [] , Territories = [])

    #Demacian Locations
    GreatCityDemacia = Locations("Great City of Demacia", None, None, Demacia.Name)
    Glaserport = Locations("Glaserport", None, None, Demacia.Name)
    Rygann = Locations("Rygann's Reach", None, None, Demacia.Name)
    Valar = Locations("Valar's Hollow", None, None, Demacia.Name)
    Fossbarrow = Locations("Fossbarrow", None, None, Demacia.Name)   
    
    #Demacian Units 
    Garen = Units("Garen", 1500, 100 , 34, 25, GreatCityDemacia.Name, Demacia)
    Lux = Units("Lux", 750, 100 , 70, 50,GreatCityDemacia.Name , Demacia)
    Jarvan = Units("Jarvan", 1000, 100 , 50, 50 , GreatCityDemacia.Name,Demacia)
    Shyvanna = Units("Shyvanna", 1000, 100 , 34, 25 , GreatCityDemacia.Name,Demacia)
    
    #Demacia Unit allocation 
    Demacia.Units.append(Garen)
    Demacia.Units.append(Lux)
    Demacia.Units.append(Jarvan)
    Demacia.Units.append(Shyvanna)
    '''
    for x in Demacia.Units:
        print(x.Name)
    '''
    #Demacia Locations Allocation 
    Demacia.Territories.append(Glaserport)
    Demacia.Territories.append(Rygann)
    Demacia.Territories.append(Valar)
    Demacia.Territories.append(Fossbarrow)
    '''
    for x in Demacia.Territories:
        print(x.Name)
    ''' 
    DeploymentPhase(Demacia)

def DeploymentPhase(Demacia):
    deployment = 1
    while deployment == 1:        
        print("\n Deployment Phase !")
        print("\n 1. Move Units , 2. View Units , 3. End Deployment ")
        UndeployedTroops = Demacia.Units
        answer = int(input())
        while answer == 1:
            print("\n Here are your current troops!")
            counter = 1
            for x in UndeployedTroops:
                print(str(counter) + ". " + x.Name)
                counter = counter + 1
            print("\n Choose a unit you wish deploy or type ext to exit deployment ")
            choice = int(input()) - 1
            if choice <= len(UndeployedTroops):
                ext = 0 
                while ext == 0:            
                    print("\n 1. Deploy, 2. Stats, 3. Exit")
                    answer2 = int(input())
                    
                    if answer2 == 1: 
                        print("\n here's a list of Areas you can deploy")
                        counter = 0
                        
                        for x in Demacia.Territories:
                            if x.Owner == UndeployedTroops[choice].Faction.Name:
                                print(str(counter) + ". " + x.Name)
                                counter = counter + 1
                                
                        print("\n Choose where " + UndeployedTroops[choice].Name + " should be deployed")
                        choice2 = int(input())
                        
                        if choice2 <= len(Demacia.Territories):
                            print("\n Are you sure you wish to deploy " + UndeployedTroops[choice].Name + " to " + Demacia.Territories[choice2].Name )
                            UndeployedTroops[choice].location =  Demacia.Territories[choice2].Name
                            choice3 = input()
                            
                            if choice3 == "yes":
                                print("\n " + UndeployedTroops[choice].Name + " has successfully been deployed to " + Demacia.Territories[choice2].Name )                          
                                #UndeployedTroops.remove(UndeployedTroops[choice])
                                ext = 1
                    
                    if answer2 == 2:
                        print("\n Name : " + UndeployedTroops[choice].Name + "\n Health : " + str(UndeployedTroops[choice].HP) + "\n Attack : " + str(UndeployedTroops[choice].Atk) + "\n Armor : " + str(UndeployedTroops[choice].Arm) + "\n Speed : " + str(UndeployedTroops[choice].Spd) )
                        print("\n Press enter to continue")
                        input()
                    
                    if answer2 == 3:
                        ext = 1
                        
            if choice != 1 or choice != 2:
                answer = 0
                
        while answer == 2:
            print("\n Here are your current troops!")
            counter = 1
            for x in Demacia.Units:
                print(str(counter) + ". " + x.Name)
                counter = counter + 1
            print("\n Choose a unit you wish to view")
            choice = int(input()) - 1
            if choice <= len(Demacia.Units) - 1 :
                ext = 0 
                print("\n Name : " + Demacia.Units[choice].Name + "\n Health : " + str( Demacia.Units[choice].HP) + "\n Attack : " + str(Demacia.Units[choice].Atk) + "\n Armor : " + str( Demacia.Units[choice].Arm) + "\n Speed : " + str( Demacia.Units[choice].Spd) + "\n location : " + str( Demacia.Units[choice].location))
                print("\n Press enter to continue")
                input()
            else:
                answer = 0
            
        if answer == 3:
            deployment = 0
            
            
            
def defend(defender, location):
    print(defender.Name + " is defending " + location.Name)
    
def Attack(Attacker, location):
    print(Attack.Name + " is attacking " + location.Name)    
    
    
NewGame()