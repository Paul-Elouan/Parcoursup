class Player:
    def __init__(self, Class, Health=1, Level=0, Xp=0):
        self.classs = Class
        self.health = Health
        self.level = Level
        self.xp = Xp
        self.xpNeeded = 50
        self.damage = 1

    def leveling(self):
        while True:
            if self.xp == xpNeeded:
                self.level = self.lvel + 1
                
                if self.level == 1:
                    xpNeeded= xpNeeded + 75 #125 xp requiered to lvl up
                    self.damage = self.damage + 1
                    self.health = self.health + 1
                
                elif self.level ==2:
                    xpNeeded = xpNeeded + 100 #225 xp requiered to lvl up
                
                elif self.level == 3:
                    xpNeeded = xpNeeded + 175 #400 xp requiered to lvl up
                    self.damage = self.damage + 1
                
                elif self.level == 4:
                    xpNeeded = xpNeeded + 300 #700 xp requiered to lvl up
                
                elif self.level == 5:
                    self.damage = self.damage + 2
                    self.health = self.health + 1



PotionList = ("Elixir of Rose Petals","Draught of Vigor","Elixir of the Bear","Flask of Souls","Elixir of the End") #Heal potion name, Armour potion name, Strength potion name, Ghost potion name & Win conditon name
WeaponList = ( # class/basic/upgraded/artefact/ice/poison/ghost/end game
    ("Wands" , "Prophecy", "Starlight", "Moonshadow", "Cryptic", "Venom Talisman" , "Starfall, Bauble of the Banished", "Corrupted Wand", "Moonshard")
    ("Axes" , "Prideful War Axe", "Purifier", "Knight's Fall", "Eclipse", "Sharpened Bone Maul" , "Malice, Greataxe of the Fallen", "Glory of the End", "Eternal Rest")
    ("Swords", "Trainee's Iron Swiftblade", "Broken Promise", "Heartless Sword", "Frozen Doomblade", "Venom, Reach of Subtlet", "Doom Glass Blade", "Silence, Claymore of the End", "Worldbreaker")
    ("Daggers", "" , "", "", "", "" , "", "", "")
    )


HealPotion, ArmourPotion, StrengthPotion, GhostPotion = 0, 0, 0, 0
#When pick up item == True
def backpack(self):
    if self in PotionList:
        if self == "Potion of Souls":
            if HealPotion <= 5:
                HealPotion += 1
            else:
                self.backpackfull()
                print("Limit reached!")
            
        elif self == "Draught of Vigor":
            if ArmourPotion <= 3:
                ArmourPotion += 1
            
        elif self == "Elixir of the Bear":
            if StrengthPotion <= 3:
                StrengthPotion += 1
            
        elif self == "Flask of Souls":
            if GhostPotion <= 2:
                GhostPotion += 1

        elif self == "Elexir of the End":
            end()
    
    elif self in WeaponList:
        if player.classs == "Mage":
            pass
        elif player.classs == "Berserker":
            pass
        elif player.classs == "Knight":
            pass
        elif player.classs == "Archer":
            pass


#Mage = Female; Berserker = Norse Male; Knight = Male Elf; Archer = Female
ClassNameList = {"Mage": "Elyn", "Berserker": "Uyvok", "Knight": "Rhys Daeven", "Archer": "Ashlynn"}

def end():
    print("gg") #show end credits