import random

witches = {25:15,34:1,47:19,65:52,77:57,91:61,99:69}
potions = { "h":[8, 31, 49, 75, 83, 95], "p":[12, 38, 55], "t":[23, 40, 86], "x":[21, 27, 39, 62]}
help = [8, 12, 21, 23, 27, 31, 35, 39, 40, 49, 55, 62, 75, 83, 86, 95]

def roll_dice():
    return random.randint(1,6)

class player:
    def __init__(self):
        pass
        self.position = 0
        self.spells = [0,0,0] #health,power,teleport
        self.hp = 10
    #persoforms heal
    def heal(self):
        if self.spells[0] == 0:
            print("Ooops! You don't have a heal spell dummy!")
        else:
            if self.hp == 10:
                print("health is at max")
            elif self.hp == 9:
                self.hp += 1
                self.spells[0] -= 1
                print("it feels so good to be back")
            else:
                self.hp += 2
                self.spells[0] -= 1
                print("it feels so good to be back")
    #poerforms teleportation
    def teleport(self):
        if self.spells[2] == 0:
            print("Does this place seem familiar?! Cause you need a spell to teleport.")
        else:
            if (self.position + 3) >= 100:
                print("Can't teleport")
            else :
                self.position = self.position + 3
                self.spells[2] -= 1
                print(f" I think I'm liking this \n Position: {self.position}")
    #moves the players position
    def move(self,dice):
        if (self.position + dice) > 100:
            print("UUUGGGRRRR!!! can't moveeee!!")
        else:
            self.position += dice
            print(f"Position: {self.position}")
    
    def play(self):
        option = str.lower(input("Choose an action 'Roll the dice'(R) / 'Heal'(H) / 'Teleport'(T) :"))
        if option == "h" or option == "t":
            if option == "h":
                self.heal()
            if option == "t":
                self.teleport()
        dice = roll_dice()
        print(f"Dice gave you {dice}")
        self.move(dice)
        #checks for witches
        if self.position in witches :
            print("OH NO, A WITCH?!")
            if self.spells[1] > 0:
                self.position += 1
                self.spells[1] -= 1
                print("I lost some HP but atleast I didn't go down")
            else:
                self.position = witches[self.position]
                print("AArrrggg SHIT!! Here we go again!!")
            self.hp -= 2
        #checks for potions or poison
        if self.position in help:
            if self.position in potions["h"]:
                self.spells[0] += 1
                print("Hey I got a HEAL spell")
            if self.position in potions["p"]:
                self.spells[1] += 1
                print("Hey I got a POWER spell")
            if self.position in potions["t"]:
                self.spells[2] += 1
                print("Hey I got a TELEPORTATION spell")
            if self.position in potions["x"]:
                self.hp -= 1
                print("Hmmmmm... That tastes weird and I don't feel so good.")
        

p1 = player() #player 1
p2 = player() #player 2

tutorial = str.lower(input("Hey there did you lost your way? (Skip(S)/Yes(Y)/No(N)):"))
if tutorial == 'skip'or's'or'S':
    print(f"Stop Ingnoring Me!!!!😡 \nAnyways... \n")
else:
    print(f"Oh, you guys sure need some help 😉\n")
print(f"Unfortunately There is only one way out... \nyou guys need to go through this forest. The forest expands from 1 to 100. You need to roll the dice and can only move the number of spaces shown on the dice.\nBut beware it's not just a walk from start to end. There is a WITCH lurking around in the forest. She's a nasty one.\nShe appears out of nowhere and descends you from the current position. Not only that you also lose your health after her attack. \nBut don't worry but I've your back. I've put some potions in the forest.....\nHmmmm....  Actually I've lost them 😅 , but you can use them. \nThere are 3 potions HEAL, POWER, TELEPORTATION.\nThe heal potion give you a spell to regenerate your health. That means +2 health and you can't go beyond max. \nPower potion give you the ability to not descend and goto one place further than witch but you will still lose you health. This spell activates automatically when you encounter the witch. \nThe teleportation potion gives you the spell to move 3 spaces from the current space. \nOH! Also I forgot there is also some poison. They decrease your health by one means -1 health. You could avoid it but they all look the same 😅.\n You can only use the spells before rolling the dice and only once. If you use the spell then the dice will roll automatically. \nAlso only player can get out of the forest? The looser will die. \nOkay then! bye have a great time.")



while (p1.position != 100) or (p2.position !=100):
    #player 1 turn
    print(f" \n *************************************  PLAYER 1  *************************************\nplayer 1:\n H  P  T    Health: {p1.hp} \n{p1.spells}   position: {p1.position}\n ")
    p1.play()
    if (p1.hp <= 0):
            print(f"player 1 is dead😵\nplayer 2 wins!!")
            break
    if (p1.position == 100):
            
            print("player 1 wins!!")
            break
    print(f"player 1:\n H  P  T   Health: {p1.hp} \n{p1.spells}   position: {p1.position}\n ")
    
    #player 2 turn
    print(f"\n ****************************************  PLAYER 2  *********************************\nplayer 2:\n H  P  T    Health: {p2.hp} \n{p2.spells}   position: {p2.position}\n  ")
    p2.play()
    if (p2.hp <= 0):
            print(f"player 2 is dead😵\nplayer 1 wins!!")
            break
    if (p2.position == 100):
            print("player 2 wins!!")
            break
    print(f"player 2:\n H  P  T    Health: {p2.hp} \n{p2.spells}   position: {p2.position}\n")

print("GAME OVER")