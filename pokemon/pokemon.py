import random
import time

computer = ("Charmander","Bulbasur","Squirtle")
comp = random.choice(computer)

bulbasur  = ("Vine Whip" ,"Tackle","Sludge Bomb","Solar Beam")
attackb = random.choice(bulbasur)

squirtle = ("Water Gun","Rapid Spin","Water Plus","Hydro Pump")
attacks = random.choice(squirtle)

charmander = ("Scratch","Dragon Breadth","DraganClaw","Fire")
attackc = random.choice(charmander)


def charvsbal():
    health = 100
    comphealth = 100
    print("Charmander Health: 100%")
    print("{:>50}".format("----->Lets Fight<-----"))
    while True:
        print('Charmander Attack -> 1. Fire,2. DragonClaw,3. Scratch,4. Dragon Breadth')
        user = int(input("Please Choose The Attack: "))
        print("Computer Turn")
        print(f"Computer attack: {attackb}")
        if user == 1 and attackb == "Vine Whip":
            print("Charmander attack Bulbasur by fire attack")
            comphealth -= 15
            print(f"Bulbasur health {comphealth}")
            print("...")
            time.sleep(1)
            print("Bulbasur attack Charmander by V         ine Whip attack")
            health -= 10
            print(f"Charmander health {health}")
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 1 and attackb == "Tackle":
            print("Charmander attack Bulbasur by fire attack")
            comphealth -= 15
            print(f"Bulbasur health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Bulbasur attack Charmander by Tackle attack")
            health -= 8
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                pokemon()
                input("Please type any key to play again")
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 1 and attackb == "Sludge Bomb":
            print("Charmander attack Bulbasur by fire attack")
            comphealth -= 15
            print(f"Bulbasur health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Bulbasur attack Charmander by Sludge Bomb attack")
            health -= 20
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()
    
        elif user == 1 and attackb == "Solar Beam":
            print("Charmander attack Bulbasur by fire attack")
            comphealth -= 15
            print(f"Bulbasur health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Bulbasur attack Charmander by Solar Beam attack")
            health -= 25
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")                
                pokemon()


        elif user == 2 and attackb == "Vine Whip":
            print("Charmander attack Bulbasur by DragonClaw attack")
            comphealth -= 20
            print(f"Bulbasur health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Bulbasur attack Charmander by Vibe Whip attack")
            health -= 10
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                pokemon()
                input("Please type any key to play again")
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 2 and attackb == "Tackle":
            print("Charmander attack Bulbasur by DragonClaw attack")
            comphealth -= 20
            print(f"Bulbasur health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Bulbasur attack Charmander by Tackle attack")
            health -= 8
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                pokemon()
                input("Please type any key to play again")
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 2 and attackb == "Sludge Bomb":
            print("Charmander attack Bulbasur by DragonClaw  attack")
            comphealth -= 20
            print(f"Bulbasur health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Bulbasur attack Charmander by Sludge Bomb attack")
            health -= 20
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()
    
        elif user == 2 and attackb == "Solar Beam":
            print("Charmander attack Bulbasur by DragonClaw  attack")
            comphealth -= 20
            print(f"Bulbasur health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Bulbasur attack Charmander by Solar Beam attack")
            health -= 25
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")                
                pokemon()     


        elif user == 3 and attackb == "Vine Whip":
            print("Charmander attack Bulbasur by  Scratch attack")
            comphealth -= 8
            print(f"Bulbasur health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Bulbasur attack Charmander by Vibe Whip attack")
            health -= 10
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                pokemon()
                input("Please type any key to play again")
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 3 and attackb == "Tackle":
            print("Charmander attack Bulbasur by  Scratch attack")
            comphealth -= 8
            print(f"Bulbasur health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Bulbasur attack Charmander by Tackle attack")
            health -= 8
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                pokemon()
                input("Please type any key to play again")
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 3 and attackb == "Sludge Bomb":
            print("Charmander attack Bulbasur by Scratch attack")
            comphealth -= 8
            print(f"Bulbasur health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Bulbasur attack Charmander by Sludge Bomb attack")
            health -= 20
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()
    
        elif user == 3 and attackb == "Solar Beam":
            print("Charmander attack Bulbasur by Scratch attack")
            comphealth -= 8
            print(f"Bulbasur health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Bulbasur attack Charmander by Solar Beam attack")
            health -= 25
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")                
                pokemon()     


        elif user == 4 and attackb == "Vine Whip":
            print("Charmander attack Bulbasur by  Dragon Breadth attack")
            comphealth -= 30
            print(f"Bulbasur health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Bulbasur attack Charmander by Vibe Whip attack")
            health -= 10
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                pokemon()
                input("Please type any key to play again")
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 4 and attackb == "Tackle":
            print("Charmander attack Bulbasur by  Dragon Breadth  attack")
            comphealth -= 30          
            print(f"Bulbasur health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Bulbasur attack Charmander by Tackle attack")
            health -= 8
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                pokemon()
                input("Please type any key to play again")
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 4 and attackb == "Sludge Bomb":
            print("Charmander attack Bulbasur by Dragon Breadth attack")
            comphealth -= 30
            print(f"Bulbasur health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Bulbasur attack Charmander by Sludge Bomb attack")
            health -= 20
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()
    
        elif user == 4 and attackb == "Solar Beam":
            print("Charmander attack Bulbasur by  Dragon Breadth  attack")
            comphealth -= 30
            print(f"Bulbasur health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Bulbasur attack Charmander by Solar Beam attack")
            health -= 25
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")                
                pokemon()     

def charvssqu():
    health = 100
    comphealth = 100
    print("Charmander Health: 100%")
    print("{:>50}".format("----->Lets Fight<-----"))
    while True:
        print('Charmander Attack -> 1. Fire,2. DragonClaw,3. Scratch,4. Dragon Breadth')
        user = int(input("Please Choose The Attack: "))

        print("Computer Turn")
        print(f"Computer attack: {attacks}")
        if user == 1 and attacks == "Water Gun":
            print("Charmander attack Squirtle by fire attack")
            comphealth -= 12
            print(f"Squirtle  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Squirtle  attack Charmander by Water Gun attack")
            health -= 15
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 1 and attacks == "Rapid Spin":
            print("Charmander attack Squirtle by fire attack")
            comphealth -= 12
            print(f"Squirtle  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Squirtle  attack Charmander by Rapid Spin attack")
            health -= 10
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                pokemon()
                input("Please type any key to play again")
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 1 and attacks == "Water Plus":
            print("Charmander attack Squirtle by fire attack")
            comphealth -= 12
            print(f"Squirtle  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Squirtle  attack Charmander by Water Plus attack")
            health -= 25
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()
    
        elif user == 1 and attacks == "Hydro Pump":
            print("Charmander attack Squirtle by fire attack")
            comphealth -= 12
            print(f"Squirtle  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Squirtle  attack Charmander by Hydro Pump attack")
            health -= 30
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")                
                pokemon()


        elif user == 2 and attacks == "Water Gun":
            print("Charmander attack Squirtle by  DragonClaw attack")
            comphealth -= 14
            print(f"Squirtle  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Squirtle  attack Charmander by Water Gun attack")
            health -= 15
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 2 and attacks == "Rapid Spin":
            print("Charmander attack Squirtle by  DragonClaw attack")
            comphealth -= 14
            print(f"Squirtle  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Squirtle  attack Charmander by Rapid Spin attack")
            health -= 10
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                pokemon()
                input("Please type any key to play again")
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 2 and attacks == "Water Plus":
            print("Charmander attack Squirtle by  DragonClaw attack")
            comphealth -= 14
            print(f"Squirtle  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Squirtle  attack Charmander by Water Plus attack")
            health -= 25
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()
    
        elif user == 2 and attacks == "Hydro Pump":
            print("Charmander attack Squirtle by  DragonClaw attack")
            comphealth -= 14
            print(f"Squirtle  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Squirtle  attack Charmander by Hydro Pump attack")
            health -= 30
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")                
                pokemon()


        elif user == 3 and attacks == "Water Gun":
            print("Charmander attack Squirtle by Scratch attack")
            comphealth -= 10 
            print(f"Squirtle  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Squirtle  attack Charmander by Water Gun attack")
            health -= 15
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 3 and attacks == "Rapid Spin":
            print("Charmander attack Squirtle by  Scratch attack")
            comphealth -= 10
            print(f"Squirtle  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Squirtle  attack Charmander by Rapid Spin attack")
            health -= 10
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                pokemon()
                input("Please type any key to play again")
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 3 and attacks == "Water Plus":
            print("Charmander attack Squirtle by Scratch attack")
            comphealth -= 10
            print(f"Squirtle  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Squirtle  attack Charmander by Water Plus attack")
            health -= 25
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()
    
        elif user == 3 and attacks == "Hydro Pump":
            print("Charmander attack Squirtle by Scratch attack")
            comphealth -= 10
            print(f"Squirtle  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Squirtle  attack Charmander by Hydro Pump attack")
            health -= 30
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")                
                pokemon()


        elif user == 4 and attacks == "Water Gun":
            print("Charmander attack Squirtle by Dragon Breadth attack")
            comphealth -= 25
            print(f"Squirtle  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Squirtle  attack Charmander by Water Gun attack")
            health -= 15
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 4 and attacks == "Rapid Spin":
            print("Charmander attack Squirtle by Dragon Breadth attack")
            comphealth -= 25
            print(f"Squirtle  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Squirtle  attack Charmander by Rapid Spin attack")
            health -= 10
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                pokemon()
                input("Please type any key to play again")
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 4 and attacks == "Water Plus":
            print("Charmander attack Squirtle by Dragon Breadth attack")
            comphealth -= 25
            print(f"Squirtle  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Squirtle  attack Charmander by Water Plus attack")
            health -= 25
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()
    
        elif user == 4 and attacks == "Hydro Pump":
            print("Charmander attack Squirtle by Dragon Breadth attack")
            comphealth -= 25
            print(f"Squirtle  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Squirtle  attack Charmander by Hydro Pump attack")
            health -= 30
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")                
                pokemon()

def charvschar():
    health = 100
    comphealth = 100
    print("Charmander Health: 100%")
    print("{:>50}".format("----->Lets Fight<-----"))
    while True:
        print('Charmander Attack -> 1. Fire,2. DragonClaw,3. Scratch,4. Dragon Breadth')
        user = int(input("Please Choose The Attack: "))

        print("Computer Turn...")
        print(f"Computer attack: {attackc}")
        
        if user == 1 and attacks == "Fire":
            print("Charmander attack Charmander by fire attack")
            comphealth -= 13
            print(f"Charmander  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Charmander  attack Charmander by fire attack")
            health -= 13
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 1 and attacks == "DragonClaw":
            print("Charmander attack Charmander by fire attack")
            comphealth -= 13
            print(f"Charmander health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Charmander  attack Charmander by DragonClaw attack")
            health -= 20
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                pokemon()
                input("Please type any key to play again")
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 1 and attacks == "Scratch":
            print("Charmander attack Charmander by fire attack")
            comphealth -= 13
            print(f"Charmander  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Charmander  attack Charmander by Scratch attack")
            health -= 10
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()
    
        elif user == 1 and attacks == "Dragon Breadth":
            print("Charmander attack Squirtle by fire attack")
            comphealth -= 12
            print(f"Charmander  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Charmander  attack Charmander by Dragon Breadth attack")
            health -= 30
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")                
                pokemon()


        elif user == 2 and attacks == "Fire":
            print("Charmander attack Charmander by  DragonClaw attack")
            comphealth -= 20
            print(f"Charmander  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Charmander  attack Charmander by Fire attack")
            health -= 13
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 2 and attacks == "DragonClaw":
            print("Charmander attack Charmander by DragonClaw attack")
            comphealth -= 20
            print(f"Charmander  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Charmander  attack Charmander by DragonClaw attack")
            health -= 20
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                pokemon()
                input("Please type any key to play again")
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 2 and attacks == "Scratch":
            print("Charmander attack Charmander by DragonClaw attack")
            comphealth -= 20
            print(f"Charmander health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Charmander  attack Charmander by Scratch attack")
            health -= 10
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()
    
        elif user == 2 and attacks == "Dragon Breadth":
            print("Charmander attack dragonclaw by fire attack")
            comphealth -= 20
            print(f"Charmander  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Charmander  attack Charmander by Dragon Breadth attack")
            health -= 30
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")                
                pokemon()


        elif user == 3 and attacks == "Fire":
            print("Charmander attack Charmander by  Scratch attack")
            comphealth -= 10
            print(f"Charmander  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Charmander  attack Charmander by Fire attack")
            health -= 13
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 3 and attacks == "DragonClaw":
            print("Charmander attack Charmander by Scratch attack")
            comphealth -= 10
            print(f"Charmander  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Charmander  attack Charmander by DragonClaw attack")
            health -= 20
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                pokemon()
                input("Please type any key to play again")
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 3 and attacks == "Scratch":
            print("Charmander attack Charmander by Scratch attack")
            comphealth -= 10
            print(f"Charmander health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Charmander  attack Charmander by Scratch attack")
            health -= 10
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()
    
        elif user == 3 and attacks == "Dragon Breadth":
            print("Charmander attack  by Scratch attack")
            comphealth -= 10
            print(f"Charmander  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Charmander attack Charmander by Dragon Breadth attack")
            health -= 30
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")                
                pokemon()


        elif user == 4 and attacks == "Fire":
            print("Charmander attack Charmander by  Dragon Breadth attack")
            comphealth -= 30
            print(f"Charmander  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Charmander  attack Charmander by Fire attack")
            health -= 13
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 4 and attacks == "DragonClaw":
            print("Charmander attack Charmander by Dragon Breadth attack")
            comphealth -= 30
            print(f"Charmander  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Charmander  attack Charmander by DragonClaw attack")
            health -= 20
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                pokemon()
                input("Please type any key to play again")
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 4 and attacks == "Scratch":
            print("Charmander attack Charmander by Dragon breadth attack")
            comphealth -= 30
            print(f"Charmander health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Charmander  attack Charmander by Scratch attack")
            health -= 10
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()
    
        elif user == 4 and attacks == "Dragon Breadth":
            print("Charmander attack  by Dragon Breadth attack")
            comphealth -= 30
            print(f"Charmander  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Charmander  attack Charmander by Dragon Breadth attack")
            health -= 30
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")                
                pokemon()

def sqvsbul():
    health = 100
    comphealth = 100
    print("Squirtle Health: 100%")
    print("{:>50}".format("----->Lets Fight<-----"))
    while True:
        print('Squirtle Attack ->"1. Water Gun","2. Rapid Spin","3. Water Plus","4. Hydro Pump"')
        user = int(input("Please Choose The Attack: "))
        print("Computer Turn")
        print(f"Computer attack: {attackb}")
        if user == 1 and attackb == "Vine Whip":
            print("Squirtle attack Bulbasur by Water Gun attack")
            comphealth -= 10
            print(f"Bulbasur health {comphealth}")
            print("...")
            time.sleep(1)
            print("Bulbasur attack Squirtle by Vin         e Whip attack")
            health -= 13
            print(f"Squirtle health {health}")
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 1 and attackb == "Tackle":
            print("Squirtle attack Bulbasur by Water Gun attack")
            comphealth -= 10
            print(f"Bulbasur health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Bulbasur attack Squirtle by Tackle attack")
            health -= 10
            print(f"Squirtle health {health}")
            if health <= 0:
                print("You lose the Match")
                pokemon()
                input("Please type any key to play again")
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 1 and attackb == "Sludge Bomb":
            print("Squirtle attack Bulbasur by Water Gun attack")
            comphealth -= 10
            print(f"Bulbasur health {comphealth}")
            print("...")
            time.sleep(1)
            print("Bulbasur attack Squirtle by Slu         dge Bomb attack")
            health -= 24
            print(f"Squirtle health {health}")
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()
    
        elif user == 1 and attackb == "Solar Beam":
            print("Squirtle attack Bulbasur by Water Gun attack")
            comphealth -= 10
            print(f"Bulbasur health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Bulbasur attack Squirtle by Solar Beam attack")
            health -= 30
            print(f"Squirtle health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")                
                pokemon()


        elif user == 2 and attackb == "Vine Whip":
            print("Squirtle attack Bulbasur by Rapid Spin attack")
            comphealth -= 14
            print(f"Bulbasur health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Bulbasur attack Squirtle by Vibe Whip attack")
            health -= 13
            print(f"Squirtle health {health}")
    
            if health <= 0:
                print("You lose the Match")
                pokemon()
                input("Please type any key to play again")
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 2 and attackb == "Tackle":
            print("Squirtle attack Bulbasur by Rapid Spin attack")
            comphealth -= 14
            print(f"Bulbasur health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Bulbasur attack Squirtle by Tackle attack")
            health -= 10
            print(f"Squirtle health {health}")
    
            if health <= 0:
                print("You lose the Match")
                pokemon()
                input("Please type any key to play again")
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 2 and attackb == "Sludge Bomb":
            print("Squirtle attack Bulbasur by Rapid Spin  attack")
            comphealth -= 14
            print(f"Bulbasur health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Bulbasur attack Squirtle by Sludge Bomb attack")
            health -= 24
            print(f"Squirtle health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()
    
        elif user == 2 and attackb == "Solar Beam":
            print("Squirtle attack Bulbasur by Rapid Spin  attack")
            comphealth -= 14
            print(f"Bulbasur health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Bulbasur attack Squirtle by Solar Beam attack")
            health -= 30
            print(f"Squirtle health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")                
                pokemon()     


        elif user == 3 and attackb == "Vine Whip":
            print("Squirtle attack Bulbasur by  Water Plus attack")
            comphealth -= 20
            print(f"Bulbasur health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Bulbasur attack Squirtle by Vine Whip attack")
            health -= 13
            print(f"Squirtle health {health}")
    
            if health <= 0:
                print("You lose the Match")
                pokemon()
                input("Please type any key to play again")
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 3 and attackb == "Tackle":
            print("Squirtle attack Bulbasur by  Water Plus attack")
            comphealth -= 20
            print(f"Bulbasur health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Bulbasur attack Squirtle by Tackle attack")
            health -= 10
            print(f"Squirtle health {health}")
    
            if health <= 0:
                print("You lose the Match")
                pokemon()
                input("Please type any key to play again")
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 3 and attackb == "Sludge Bomb":
            print("Squirtle attack Bulbasur by Water Plus attack")
            comphealth -= 20
            print(f"Bulbasur health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Bulbasur attack Squirtle by Sludge Bomb attack")
            health -= 24
            print(f"Squirtle health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()
    
        elif user == 3 and attackb == "Solar Beam":
            print("Squirtle attack Bulbasur by Water Plus attack")
            comphealth -= 20
            print(f"Bulbasur health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Bulbasur attack Squirtle by Solar Beam attack")
            health -= 30
            print(f"Squirtle health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")                
                pokemon()     


        elif user == 4 and attackb == "Vine Whip":
            print("Squirtle attack Bulbasur by  Hydro Pump attack")
            comphealth -= 25
            print(f"Bulbasur health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Bulbasur attack Squirtle by Vibe Whip attack")
            health -= 13
            print(f"Squirtle health {health}")
    
            if health <= 0:
                print("You lose the Match")
                pokemon()
                input("Please type any key to play again")
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 4 and attackb == "Tackle":
            print("Squirtle attack Bulbasur by Hydro Pump  attack")
            comphealth -= 25        
            print(f"Bulbasur health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Bulbasur attack Squirtle by Tackle attack")
            health -= 10
            print(f"Squirtle health {health}")
    
            if health <= 0:
                print("You lose the Match")
                pokemon()
                input("Please type any key to play again")
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 4 and attackb == "Sludge Bomb":
            print("Squirtle attack Bulbasur by Hydro Pump attack")
            comphealth -= 25
            print(f"Bulbasur health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Bulbasur attack Squirtle by Sludge Bomb attack")
            health -= 24
            print(f"Squirtle health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()
    
        elif user == 4 and attackb == "Solar Beam":
            print("Squirtle attack Bulbasur by  Hydro Pump  attack")
            comphealth -= 25
            print(f"Bulbasur health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Bulbasur attack Squirtle by Solar Beam attack")
            health -= 30
            print(f"Squirtle health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")                
                pokemon()     

def sqvssq():
    health = 100
    comphealth = 100
    print("Squirtle Health: 100%")
    print("{:>50}".format("----->Lets Fight<-----"))
    while True:
        print('Squirtle Attack ->"1. Water Gun","2. Rapid Spin","3. Water Plus","4. Hydro Pump"')
        user = int(input("Please Choose The Attack: "))
        print("Computer Turn")
        print(f"Computer attack: {attacks}")
        if user == 1 and attacks == "Water Gun":
            print("Squirtle attack Squirtle by Water Gun")
            comphealth -= 10
            print(f"Squirtle  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Squirtle  attack Squirtle by Water Gun attack")
            health -= 10
            print(f"Squirtle health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 1 and attacks == "Rapid Spin":
            print("Squirtle attack Squirtle by Water Gun attack")
            comphealth -= 10
            print(f"Squirtle  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Squirtle  attack Squirtle by Rapid Spin attack")
            health -= 15
            print(f"Squirtle health {health}")
    
            if health <= 0:
                print("You lose the Match")
                pokemon()
                input("Please type any key to play again")
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 1 and attacks == "Water Plus":
            print("Squirtle attack Squirtle by Water Gun attack")
            comphealth -= 10
            print(f"Squirtle  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Squirtle  attack Squirtle by Water Plus attack")
            health -= 18
            print(f"Squirtle health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()
    
        elif user == 1 and attacks == "Hydro Pump":
            print("Squirtle attack Squirtle by Water Gun attack")
            comphealth -= 10
            print(f"Squirtle  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Squirtle  attack Squirtle by Hydro Pump attack")
            health -= 24
            print(f"Squirtle health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")                
                pokemon()


        elif user == 2 and attacks == "Water Gun":
            print("Squirtle attack Squirtle by  Rapid Spin attack")
            comphealth -= 15
            print(f"Squirtle  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Squirtle  attack Squirtle by Water Gun attack")
            health -= 10
            print(f"Squirtle health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 2 and attacks == "Rapid Spin":
            print("Squirtle attack Squirtle by Rapid Spin attack")
            comphealth -= 15
            print(f"Squirtle  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Squirtle  attack Squirtle by Rapid Spin attack")
            health -= 15
            print(f"Squirtle health {health}")
    
            if health <= 0:
                print("You lose the Match")
                pokemon()
                input("Please type any key to play again")
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 2 and attacks == "Water Plus":
            print("Squirtle attack Squirtle by Rapid Spin attack")
            comphealth -= 15
            print(f"Squirtle  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Squirtle  attack Squirtle by Water Plus attack")
            health -= 18
            print(f"Squirtle health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()
    
        elif user == 2 and attacks == "Hydro Pump":
            print("Charmander attack Squirtle by Rapid Spin attack")
            comphealth -= 15
            print(f"Squirtle  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Squirtle  attack Charmander by Hydro Pump attack")
            health -= 24
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")                
                pokemon()


        elif user == 3 and attacks == "Water Gun":
            print("Squirtle attack Squirtle by Water Plus attack")
            comphealth -= 18
            print(f"Squirtle  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Squirtle  attack Squirtle by Water Gun attack")
            health -= 10
            print(f"Squirtle health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 3 and attacks == "Rapid Spin":
            print("Squirtle attack Squirtle by Water Plus attack")
            comphealth -= 18
            print(f"Squirtle  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Squirtle  attack Squirtle by Rapid Spin attack")
            health -= 15
            print(f"Squirtle health {health}")
    
            if health <= 0:
                print("You lose the Match")
                pokemon()
                input("Please type any key to play again")
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 3 and attacks == "Water Plus":
            print("Squirtle attack Squirtle by Water Plus attack")
            comphealth -= 18
            print(f"Squirtle  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Squirtle  attack Squirtle by Water Plus attack")
            health -= 18
            print(f"Squirtle health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()
    
        elif user == 3 and attacks == "Hydro Pump":
            print("Charmander attack Squirtle by Water PLus attack")
            comphealth -= 18
            print(f"Squirtle  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Squirtle  attack Charmander by Hydro Pump attack")
            health -= 24
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")                
                pokemon()


        elif user == 4 and attacks == "Water Gun":
            print("Squirtle attack Squirtle by Hydro Pump attack")
            comphealth -= 24
            print(f"Squirtle  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Squirtle  attack Squirtle by Water Gun attack")
            health -= 10
            print(f"Squirtle health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 4 and attacks == "Rapid Spin":
            print("Squirtle attack Squirtle by Hydro Pump attack")
            comphealth -= 24
            print(f"Squirtle  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Squirtle  attack Squirtle by Rapid Spin attack")
            health -= 15
            print(f"Squirtle health {health}")
    
            if health <= 0:
                print("You lose the Match")
                pokemon()
                input("Please type any key to play again")
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 4 and attacks == "Water Plus":
            print("Squirtle attack Squirtle by Hydro Pump attack")
            comphealth -= 24
            print(f"Squirtle  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Squirtle  attack Squirtle by Water Plus attack")
            health -= 18
            print(f"Squirtle health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()
    
        elif user == 4 and attacks == "Hydro Pump":
            print("Charmander attack Squirtle by Hydro Pump attack")
            comphealth -= 24
            print(f"Squirtle  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Squirtle  attack Charmander by Hydro Pump attack")
            health -= 24
            print(f"Charmander health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")                
                pokemon()

def sqvsch():
    health = 100
    comphealth = 100
    print("Squirtle Health: 100%")
    print("{:>50}".format("----->Lets Fight<-----"))
    while True:
        print('Squirtle Attack ->"1. Water Gun","2. Rapid Spin","3. Water Plus","4. Hydro Pump"')
        user = int(input("Please Choose The Attack: "))
        print("Computer Turn")
        print(f"Computer attack: {attacks}")
        if user == 1 and attacks == "Scratch":
            print("Squirtle attack Charmander by Water Gun")
            comphealth -= 15
            print(f"Charmander  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Charmander attack Squirtle by Scratch attack")
            health -= 10
            print(f"Squirtle health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 1 and attacks == "Dragon Breadth":
            print("Squirtle attack Charmander by Water Gun attack")
            comphealth -= 15
            print(f"Charmander health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Charmander attack Squirtle by DragonBreadth attack")
            health -= 24
            print(f"Squirtle health {health}")
    
            if health <= 0:
                print("You lose the Match")
                pokemon()
                input("Please type any key to play again")
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 1 and attacks == "DragonClaw":
            print("Squirtle attack Charamander by Water Gun attack")
            comphealth -= 15
            print(f"Charamander  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Charamander  attack Squirtle by DragonClaw attack")
            health -= 17
            print(f"Squirtle health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()
    
        elif user == 1 and attacks == "Fire":
            print("Squirtle attack Charmander by Water Gun attack")
            comphealth -= 15
            print(f"Charmander  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Charmander  attack Squirtle by Fire attack")
            health -= 12
            print(f"Squirtle health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")                
                pokemon()

        elif user == 2 and attacks == "Scratch":
            print("Squirtle attack Charmander by Rapid Spin")
            comphealth -= 12
            print(f"Charmander  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Charmander attack Squirtle by Scratch attack")
            health -= 10
            print(f"Squirtle health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 2 and attacks == "Dragon Breadth":
            print("Squirtle attack Charmander by Rapid Spin attack")
            comphealth -= 12
            print(f"Charmander health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Charmander attack Squirtle by DragonBreadth attack")
            health -= 24
            print(f"Squirtle health {health}")
    
            if health <= 0:
                print("You lose the Match")
                pokemon()
                input("Please type any key to play again")
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 2 and attacks == "DragonClaw":
            print("Squirtle attack Charamander by Rapid Spin attack")
            comphealth -= 12
            print(f"Charamander  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Charamander  attack Squirtle by DragonClaw attack")
            health -= 17
            print(f"Squirtle health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()
    
        elif user == 2 and attacks == "Fire":
            print("Squirtle attack Charmander by Rapid Spin attack")
            comphealth -= 12
            print(f"Charmander  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Charmander  attack Squirtle by Fire attack")
            health -= 12
            print(f"Squirtle health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")                
                pokemon()


        elif user == 3 and attacks == "Scratch":
            print("Squirtle attack Charmander by Water Plus attack")
            comphealth -= 20
            print(f"Charmander  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Charmander attack Squirtle by Scratch attack")
            health -= 10
            print(f"Squirtle health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 3 and attacks == "Dragon Breadth":
            print("Squirtle attack Charmander by Water Plus attack")
            comphealth -= 20
            print(f"Charmander health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Charmander attack Squirtle by DragonBreadth attack")
            health -= 24
            print(f"Squirtle health {health}")
    
            if health <= 0:
                print("You lose the Match")
                pokemon()
                input("Please type any key to play again")
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 3 and attacks == "DragonClaw":
            print("Squirtle attack Charamander by Water Plus attack")
            comphealth -= 20
            print(f"Charamander  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Charamander  attack Squirtle by DragonClaw attack")
            health -= 17
            print(f"Squirtle health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()
    
        elif user == 3 and attacks == "Fire":
            print("Squirtle attack Charmander by Water Plus attack")
            comphealth -= 20
            print(f"Charmander  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Charmander  attack Squirtle by Fire attack")
            health -= 12
            print(f"Squirtle health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")                
                pokemon()


        elif user == 4 and attacks == "Scratch":
            print("Squirtle attack Charmander by Hydro Pump Spin")
            comphealth -= 30
            print(f"Charmander  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Charmander attack Squirtle by Scratch attack")
            health -= 10
            print(f"Squirtle health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 4 and attacks == "Dragon Breadth":
            print("Squirtle attack Charmander by Hydro Pump  attack")
            comphealth -= 30
            print(f"Charmander health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Charmander attack Squirtle by DragonBreadth attack")
            health -= 24
            print(f"Squirtle health {health}")
    
            if health <= 0:
                print("You lose the Match")
                pokemon()
                input("Please type any key to play again")
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 4 and attacks == "DragonClaw":
            print("Squirtle attack Charamander by Hydro Pump attack")
            comphealth -= 30
            print(f"Charamander  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Charamander  attack Squirtle by DragonClaw attack")
            health -= 17
            print(f"Squirtle health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()
    
        elif user == 4 and attacks == "Fire":
            print("Squirtle attack Charmander by Hydro Pump attack")
            comphealth -= 30
            print(f"Charmander  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Charmander  attack Squirtle by Fire attack")
            health -= 12
            print(f"Squirtle health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")                
                pokemon()


    
def bulvsbul():
    health = 100
    comphealth = 100
    print("Bulbasur Health: 100%")
    print("{:>50}".format("----->Lets Fight<-----"))
    while True:
        print('Bulbasur Attack -> 1. Vine Whip ,2. Tackle,3. Sludge Bomb, 4. Solar Beam')
        user = int(input("Please Choose The Attack: "))
        print("Computer Turn")
        print(f"Computer attack: {attackb}")
        if user == 1 and attackb == "Vine Whip":
            print("Bulbasur attack Bulbasur by Vine Whip attack")
            comphealth -= 13
            print(f"Bulbasur health {comphealth}")
            print("...")
            time.sleep(1)
            print("Bulbasur attack Bulbasur by Vin         e Whip attack")
            health -= 13
            print(f"Bulbasur health {health}")
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 1 and attackb == "Tackle":
            print("BulBasur attack Bulbasur by Vine Whip attack")
            comphealth -= 13
            print(f"Bulbasur health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Bulbasur attack BulBasur by Tackle attack")
            health -= 10
            print(f"BulBasur health {health}")
    
            if health <= 0:
                print("You lose the Match")
                pokemon()
                input("Please type any key to play again")
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 1 and attackb == "Sludge Bomb":
            print("Bulbasur attack Bulbasur Vine Whip attack")
            comphealth -= 13
            print(f"Bulbasur health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Bulbasur attack Bulbasur by Sludge Bomb attack")
            health -= 18
            print(f"Bulbasur health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()
    
        elif user == 1 and attackb == "Solar Beam":
            print("Bulbasur attack Bulbasur by Vine Whip attack")
            comphealth -= 13
            print(f"Bulbasur health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Bulbasur attack Bulbasur by Solar Beam attack")
            health -= 25
            print(f"Bulbasur health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")                
                pokemon()


        elif user == 2 and attackb == "Vine Whip":
            print("Bulbasur attack Bulbasur by Tackle attack")
            comphealth -= 10
            print(f"Bulbasur health {comphealth}")
            print("...")
            time.sleep(1)
            print("Bulbasur attack Bulbasur by Vin         e Whip attack")
            health -= 13
            print(f"Bulbasur health {health}")
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 2 and attackb == "Tackle":
            print("BulBasur attack Bulbasur by Tackle attack")
            comphealth -= 10
            print(f"Bulbasur health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Bulbasur attack BulBasur by Tackle attack")
            health -= 10
            print(f"BulBasur health {health}")
    
            if health <= 0:
                print("You lose the Match")
                pokemon()
                input("Please type any key to play again")
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 2 and attackb == "Sludge Bomb":
            print("Bulbasur attack Bulbasur Tackle attack")
            comphealth -= 10
            print(f"Bulbasur health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Bulbasur attack Bulbasur by Sludge Bomb attack")
            health -= 18
            print(f"Bulbasur health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()
    
        elif user == 2 and attackb == "Solar Beam":
            print("Bulbasur attack Bulbasur by Tackle attack")
            comphealth -= 10
            print(f"Bulbasur health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Bulbasur attack Bulbasur by Solar Beam attack")
            health -= 25
            print(f"Bulbasur health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")                
                pokemon()


        elif user == 3 and attackb == "Vine Whip":
            print("Bulbasur attack Bulbasur by Sludge Bomb attack")
            comphealth -= 18
            print(f"Bulbasur health {comphealth}")
            print("...")
            time.sleep(1)
            print("Bulbasur attack Bulbasur by Vin         e Whip attack")
            health -= 13
            print(f"Bulbasur health {health}")
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 3 and attackb == "Tackle":
            print("BulBasur attack Bulbasur by Sludge Bomb attack")
            comphealth -= 18
            print(f"Bulbasur health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Bulbasur attack BulBasur by Tackle attack")
            health -= 10
            print(f"BulBasur health {health}")
    
            if health <= 0:
                print("You lose the Match")
                pokemon()
                input("Please type any key to play again")
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 3 and attackb == "Sludge Bomb":
            print("Bulbasur attack Bulbasur Sludge Bomb attack")
            comphealth -= 18
            print(f"Bulbasur health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Bulbasur attack Bulbasur by Sludge Bomb attack")
            health -= 18
            print(f"Bulbasur health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()
    
        elif user == 3 and attackb == "Solar Beam":
            print("Bulbasur attack Bulbasur by Sludge Bomb attack")
            comphealth -= 18
            print(f"Bulbasur health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Bulbasur attack Bulbasur by Solar Beam attack")
            health -= 25
            print(f"Bulbasur health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")                
                pokemon()


        elif user == 4 and attackb == "Vine Whip":
            print("Bulbasur attack Bulbasur by Solar Beam attack")
            comphealth -= 25
            print(f"Bulbasur health {comphealth}")
            print("...")
            time.sleep(1)
            print("Bulbasur attack Bulbasur by Vin         e Whip attack")
            health -= 13
            print(f"Bulbasur health {health}")
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 4 and attackb == "Tackle":
            print("BulBasur attack Bulbasur by Solar Beam attack")
            comphealth -= 25
            print(f"Bulbasur health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Bulbasur attack BulBasur by Tackle attack")
            health -= 10
            print(f"BulBasur health {health}")
    
            if health <= 0:
                print("You lose the Match")
                pokemon()
                input("Please type any key to play again")
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 4 and attackb == "Sludge Bomb":
            print("Bulbasur attack Bulbasur Solar Beam attack")
            comphealth -= 25
            print(f"Bulbasur health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Bulbasur attack Bulbasur by Sludge Bomb attack")
            health -= 18
            print(f"Bulbasur health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()
    
        elif user == 4 and attackb == "Solar Beam":
            print("Bulbasur attack Bulbasur by Solar Beam attack")
            comphealth -= 25
            print(f"Bulbasur health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Bulbasur attack Bulbasur by Solar Beam attack")
            health -= 25
            print(f"Bulbasur health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")                
                pokemon()


def bulvsch():
    health = 100
    comphealth = 100
    print("Bulbasur Health: 100%")
    print("{:>50}".format("----->Lets Fight<-----"))
    while True:
        print('Bulbasur Attack -> 1. Vine Whip ,2. Tackle,3. Sludge Bomb, 4. Solar Beam')
        user = int(input("Please Choose The Attack: "))
        print("Computer Turn")
        print(f"Computer attack: {attacks}")
        if user == 1 and attacks == "Scratch":
            print("Bulbasur attack Charmander by Vine Whip attack")
            comphealth -= 13
            print(f"Charmander  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Charmander attack Bulbasur by Scratch attack")
            health -= 10
            print(f"Bulbasur health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 1 and attacks == "Dragon Breadth":
            print("Bulbasur attack Charmander by Vine whip attack")
            comphealth -= 13
            print(f"Charmander health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Charmander attack Bulbasur by DragonBreadth attack")
            health -= 30
            print(f"Bulbasur health {health}")
    
            if health <= 0:
                print("You lose the Match")
                pokemon()
                input("Please type any key to play again")
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 1 and attacks == "DragonClaw":
            print("Bulbasur attack Charmander by Vine whip attack")
            comphealth -= 13
            print(f"Charmander health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Charmander attack Bulbasur by DragonClaw attack")
            health -= 20
            print(f"Bulbasur health {health}")
    
            if health <= 0:
                print("You lose the Match")
                pokemon()
                input("Please type any key to play again")
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()
    
        elif user == 1 and attacks == "Fire":
            print("Bulbasur attack Charmander by Vine whip attack")
            comphealth -= 13
            print(f"Charmander health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Charmander attack Bulbasur by fire attack")
            health -= 15
            print(f"Bulbasur health {health}")
    
            if health <= 0:
                print("You lose the Match")
                pokemon()
                input("Please type any key to play again")
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()
        

        elif user == 2 and attacks == "Scratch":
            print("Bulbasur attack Charmander by Tackle attack")
            comphealth -= 10
            print(f"Charmander  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Charmander attack Bulbasur by Scratch attack")
            health -= 10
            print(f"Bulbasur health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 2 and attacks == "Dragon Breadth":
            print("Bulbasur attack Charmander by Tackle attack")
            comphealth -= 10
            print(f"Charmander health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Charmander attack Bulbasur by DragonBreadth attack")
            health -= 30
            print(f"Bulbasur health {health}")
    
            if health <= 0:
                print("You lose the Match")
                pokemon()
                input("Please type any key to play again")
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 2 and attacks == "DragonClaw":
            print("Bulbasur attack Charmander by Tackle attack")
            comphealth -= 10
            print(f"Charmander health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Charmander attack Bulbasur by DragonClaw attack")
            health -= 20
            print(f"Bulbasur health {health}")
    
            if health <= 0:
                print("You lose the Match")
                pokemon()
                input("Please type any key to play again")
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()
    
        elif user == 2 and attacks == "Fire":
            print("Bulbasur attack Charmander by Tackle attack")
            comphealth -= 10
            print(f"Charmander health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Charmander attack Bulbasur by fire attack")
            health -= 15
            print(f"Bulbasur health {health}")
    
            if health <= 0:
                print("You lose the Match")
                pokemon()
                input("Please type any key to play again")
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()
        

        elif user == 3 and attacks == "Scratch":
            print("Bulbasur attack Charmander by Sludge Bomb attack")
            comphealth -= 18
            print(f"Charmander  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Charmander attack Bulbasur by Scratch attack")
            health -= 10
            print(f"Bulbasur health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 3 and attacks == "Dragon Breadth":
            print("Bulbasur attack Charmander by Sludge Bomb attack")
            comphealth -= 10
            print(f"Charmander health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Charmander attack Bulbasur by DragonBreadth attack")
            health -= 30
            print(f"Bulbasur health {health}")
    
            if health <= 0:
                print("You lose the Match")
                pokemon()
                input("Please type any key to play again")
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 3 and attacks == "DragonClaw":
            print("Bulbasur attack Charmander by Sludge Bomb attack")
            comphealth -= 10
            print(f"Charmander health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Charmander attack Bulbasur by DragonClaw attack")
            health -= 20
            print(f"Bulbasur health {health}")
    
            if health <= 0:
                print("You lose the Match")
                pokemon()
                input("Please type any key to play again")
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()
    
        elif user == 3 and attacks == "Fire":
            print("Bulbasur attack Charmander by Sludge Bomb attack")
            comphealth -= 10
            print(f"Charmander health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Charmander attack Bulbasur by fire attack")
            health -= 15
            print(f"Bulbasur health {health}")
    
            if health <= 0:
                print("You lose the Match")
                pokemon()
                input("Please type any key to play again")
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()
        

        elif user == 4 and attacks == "Scratch":
            print("Bulbasur attack Charmander by Solar Beam attack")
            comphealth -= 23
            print(f"Charmander  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Charmander attack Bulbasur by Scratch attack")
            health -= 10
            print(f"Bulbasur health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 4 and attacks == "Dragon Breadth":
            print("Bulbasur attack Charmander by Solar Beam attack")
            comphealth -= 23
            print(f"Charmander health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Charmander attack Bulbasur by DragonBreadth attack")
            health -= 30
            print(f"Bulbasur health {health}")
    
            if health <= 0:
                print("You lose the Match")
                pokemon()
                input("Please type any key to play again")
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 4 and attacks == "DragonClaw":
            print("Bulbasur attack Charmander by Solar Beam attack")
            comphealth -= 23
            print(f"Charmander health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Charmander attack Bulbasur by DragonClaw attack")
            health -= 20
            print(f"Bulbasur health {health}")
    
            if health <= 0:
                print("You lose the Match")
                pokemon()
                input("Please type any key to play again")
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()
    
        elif user == 4 and attacks == "Fire":
            print("Bulbasur attack Charmander by Solar Beam attack")
            comphealth -= 23
            print(f"Charmander health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Charmander attack Bulbasur by fire attack")
            health -= 15
            print(f"Bulbasur health {health}")
    
            if health <= 0:
                print("You lose the Match")
                pokemon()
                input("Please type any key to play again")
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()
        

def bulvssq():
    health = 100
    comphealth = 100
    print("Bulbasur Health: 100%")
    print("{:>50}".format("----->Lets Fight<-----"))
    while True:
        print('Bulbasur Attack -> 1. Vine Whip ,2. Tackle,3. Sludge Bomb, 4. Solar Beam')
        user = int(input("Please Choose The Attack: "))
        print("Computer Turn")
        print(f"Computer attack: {attacks}")
        if user == 1 and attacks == "Water Gun":
            print("Bulbasur attack Squirtle by Vine Whip attack")
            comphealth -= 15
            print(f"Squirtle  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Squirtle  attack Bulbasur by Water Gun attack")
            health -= 10
            print(f"Bulbasur health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 1 and attacks == "Rapid Spin":
            print("Bulbasur attack Squirtle by Vine Whip attack")
            comphealth -= 15
            print(f"Squirtle  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Squirtle  attack Bulbasur by Rapid Spin attack")
            health -= 12
            print(f"Bulbasur health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 1 and attacks == "Water Plus":
            print("Bulbasur attack Squirtle by Vine Whip attack")
            comphealth -= 15
            print(f"Squirtle  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Squirtle  attack Bulbasur by Water Plus attack")
            health -= 17
            print(f"Bulbasur health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 1 and attacks == "Hydro Pump":
            print("Bulbasur attack Squirtle by Vine Whip attack")
            comphealth -= 15
            print(f"Squirtle  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Squirtle  attack Bulbasur by Hydro Pump attack")
            health -= 22
            print(f"Bulbasur health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()


        elif user == 2 and attacks == "Water Gun":
            print("Bulbasur attack Squirtle by Tackle attack")
            comphealth -= 12
            print(f"Squirtle  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Squirtle  attack Bulbasur by Water Gun attack")
            health -= 10
            print(f"Bulbasur health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 2 and attacks == "Rapid Spin":
            print("Bulbasur attack Squirtle by Tackle attack")
            comphealth -= 12
            print(f"Squirtle  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Squirtle  attack Bulbasur by Rapid Spin attack")
            health -= 12
            print(f"Bulbasur health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 2 and attacks == "Water Plus":
            print("Bulbasur attack Squirtle by Tackle attack")
            comphealth -= 12
            print(f"Squirtle  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Squirtle  attack Bulbasur by Water Plus attack")
            health -= 17
            print(f"Bulbasur health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 2 and attacks == "Hydro Pump":
            print("Bulbasur attack Squirtle by Tackle attack")
            comphealth -= 12
            print(f"Squirtle  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Squirtle  attack Bulbasur by Hydro Pump attack")
            health -= 22
            print(f"Bulbasur health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()


        elif user == 3 and attacks == "Water Gun":
            print("Bulbasur attack Squirtle by Sludge Bomb attack")
            comphealth -= 20
            print(f"Squirtle  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Squirtle  attack Bulbasur by Water Gun attack")
            health -= 10
            print(f"Bulbasur health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 3 and attacks == "Rapid Spin":
            print("Bulbasur attack Squirtle by Sludge Bomb attack")
            comphealth -= 20
            print(f"Squirtle  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Squirtle  attack Bulbasur by Rapid Spin attack")
            health -= 12
            print(f"Bulbasur health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 3 and attacks == "Water Plus":
            print("Bulbasur attack Squirtle by Sludge Bomb attack")
            comphealth -= 20
            print(f"Squirtle  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Squirtle  attack Bulbasur by Water Plus attack")
            health -= 17
            print(f"Bulbasur health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 3 and attacks == "Hydro Pump":
            print("Bulbasur attack Squirtle by Sludge Bomb attack")
            comphealth -= 20
            print(f"Squirtle  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Squirtle  attack Bulbasur by Hydro Pump attack")
            health -= 22
            print(f"Bulbasur health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()


        elif user == 4 and attacks == "Water Gun":
            print("Bulbasur attack Squirtle by Solar Beam attack")
            comphealth -= 30
            print(f"Squirtle  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Squirtle  attack Bulbasur by Water Gun attack")
            health -= 10
            print(f"Bulbasur health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 4 and attacks == "Rapid Spin":
            print("Bulbasur attack Squirtle by Solar Beam attack")
            comphealth -= 30
            print(f"Squirtle  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Squirtle  attack Bulbasur by Rapid Spin attack")
            health -= 12
            print(f"Bulbasur health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 4 and attacks == "Water Plus":
            print("Bulbasur attack Squirtle by Solar Beam attack")
            comphealth -= 30
            print(f"Squirtle  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Squirtle  attack Bulbasur by Water Plus attack")
            health -= 17
            print(f"Bulbasur health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()

        elif user == 4 and attacks == "Hydro Pump":
            print("Bulbasur attack Squirtle by Solar Beam attack")
            comphealth -= 30
            print(f"Squirtle  health {comphealth}")
            print("...")
            time.sleep(1)
            
            print("Squirtle  attack Bulbasur by Hydro Pump attack")
            health -= 22
            print(f"Bulbasur health {health}")
    
            if health <= 0:
                print("You lose the Match")
                input("Please type any key to play again")
                pokemon()
            elif comphealth <= 0:
                print("You win the Match")
                input("Please type any key to play again")
                pokemon()



def pokemon():
    print("1. Charmander")
    print("2. Squirtle") 
    print("3. Bulbasaur")       
    print("{:>50}".format("----->Choice Pokemon<-----"))
    user = int(input("Enter the number: "))
    if user == 1:
        print("You choice Charmander")
        print(f'Computer choice: {comp}')
        fight = input("Please type any key to fight: ")
        if user == 1 and comp == "Bulbasur":
            charvsbal()
        elif user == 1 and comp == "Squirtle":
            charvssqu()
        elif user == 1 and comp == "Charmander":
            charvschar()
    elif user == 2 :
        print("You choice Squirtle")
        print(f'Computer choice: {comp}')
        fight = input("Please type any key to fight: ")
        if user == 2 and comp == "Bulbasur":
            sqvsbul()
        elif user == 2 and comp == "Squirtle":
            sqvssq()
        elif user == 2 and comp == "Charmander":
            sqvsch()
    elif user == 3 :
        print("You choice Bulbasur")
        print(f'Computer choice: {comp}')
        fight = input("Please type any key to fight: ")
        if user == 3 and comp == "Bulbasur":
            bulvsbul()
        elif user == 3 and comp == "Squirtle":
            bulvssq()
        elif user == 3 and comp == "Charmander":
            bulvsch()
        

pokemon()