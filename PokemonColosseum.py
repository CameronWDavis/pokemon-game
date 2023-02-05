# Cameron Davis
# Dr.Liu
# 1/27/2023
# Intro to AI

#import statements for other python modules
import random #import for random number generation
from pokemon import Pokemon #import for pokemon object
from Color import colors #import for color
from mechanics import Moves #import for moves



#this is the moveset for team rocket
def rocketMove(pokemonRocket: Pokemon, moveArray, pokemonPlayer:Pokemon,rocketOptions):
    #choice array is the move selected from our array randonly
    choice = random.choice(rocketOptions)

    #array to hold all moves
    rocketMoves = [1,2,3,4,5]
    #case for Magikarp since it has a single move
    if pokemonRocket.name == "Magikarp":
        #for loop for setting the value
      for i in moveArray:
          #damage and calculations for magikarp
        if pokemonRocket.moves.strip() == i.name:
            rocketMoves[0] = i
            stab = 1.5 if rocketMoves[0].type == pokemonRocket.type else 1
            typeEff = typeMatchup(rocketMoves[0], pokemonPlayer)  # type matchup function
            dmg = calculateDamage(int(rocketMoves[0].power), int(pokemonRocket.attack), int(pokemonPlayer.defense), stab, typeEff)
            print("Team rockets ", pokemonRocket.getType(), pokemonRocket.name, colors.reset, " used ",
            rocketMoves[0].getType(), rocketMoves[0].name, colors.reset, " on ", pokemonPlayer.getType(),pokemonPlayer.name, colors.reset)
            print("Damage to ", pokemonPlayer.getType(), pokemonPlayer.name, colors.reset, " is ", dmg)
            pokemonPlayer.health = int(pokemonPlayer.health) - dmg
            rocketData = {
                "pokemonPlayer": pokemonPlayer,
                "pokemonRocket": pokemonRocket,
            }
            return rocketData
    #set the index value equal to 0
    index = 0
    # algorithm for move data finds the moves in the pokemon and finds the actual move data from that
    for x in pokemonRocket.moves:
        for i in moveArray:
            #strip teh whitespace from the moves
            if x.strip() == i.name:
                rocketMoves[index] = i
                index += 1


    #this is a switch statement for the random option that is selected for team rockets move
    match choice:
        case 1:
            stab = 1.5 if rocketMoves[0].type == pokemonRocket.type else 1
            typeEff = typeMatchup(rocketMoves[0], pokemonPlayer)  # type matchup function
            dmg = calculateDamage(int(rocketMoves[0].power),int(pokemonRocket.attack),int(pokemonPlayer.defense),stab,typeEff)
            print("Team rockets ", pokemonRocket.getType(), pokemonRocket.name, colors.reset, " used ", rocketMoves[0].getType(), rocketMoves[0].name, colors.reset," on ", pokemonPlayer.getType(), pokemonPlayer.name, colors.reset)
            print("Damage to ", pokemonPlayer.getType(), pokemonPlayer.name, colors.reset, " is ", dmg)
            pokemonPlayer.health = int(pokemonPlayer.health) - dmg
            rocketOptions.remove(choice)
        case 2:
            stab = 1.5 if rocketMoves[1].type == pokemonRocket.type else 1
            typeEff = typeMatchup(rocketMoves[1], pokemonPlayer)  # type matchup function
            dmg = calculateDamage(int(rocketMoves[1].power), int(pokemonRocket.attack), int(pokemonPlayer.defense), stab, typeEff)
            print("Team rockets ",pokemonRocket.getType(), pokemonRocket.name, colors.reset, " used ", rocketMoves[1].getType(),rocketMoves[1].name, colors.reset, " on ", pokemonPlayer.getType(), pokemonPlayer.name, colors.reset)
            print("Damage to ", pokemonPlayer.getType(), pokemonPlayer.name, colors.reset, " is ", dmg)
            pokemonPlayer.health = int(pokemonPlayer.health) - dmg
            rocketOptions.remove(choice)
        case 3:
            stab = 1.5 if rocketMoves[2].type == pokemonRocket.type else 1
            typeEff = typeMatchup(rocketMoves[2], pokemonPlayer)  # type matchup function
            dmg = calculateDamage(int(rocketMoves[2].power), int(pokemonRocket.attack), int(pokemonPlayer.defense), stab, typeEff)
            print("Team rockets ",pokemonRocket.getType(), pokemonRocket.name, colors.reset, " used ", rocketMoves[2].getType(),rocketMoves[2].name, colors.reset, " on ", pokemonPlayer.getType(), pokemonPlayer.name, colors.reset)
            print("Damage to ", pokemonPlayer.getType(), pokemonPlayer.name, colors.reset, " is ", dmg)
            pokemonPlayer.health = int(pokemonPlayer.health) - dmg
            rocketOptions.remove(choice)
        case 4:
            stab = 1.5 if rocketMoves[3].type == pokemonRocket.type else 1
            typeEff = typeMatchup(rocketMoves[3], pokemonPlayer)  # type matchup function
            dmg = calculateDamage(int(rocketMoves[3].power), int(pokemonRocket.attack), int(pokemonPlayer.defense), stab, typeEff)
            print("Team rockets ",pokemonRocket.getType(), pokemonRocket.name, colors.reset, " used ", rocketMoves[3].getType(),
                  rocketMoves[3].name, colors.reset, " on ", pokemonPlayer.getType(), pokemonPlayer.name, colors.reset)
            print("Damage to ", pokemonPlayer.getType(), pokemonPlayer.name, colors.reset, " is ", dmg)
            pokemonPlayer.health = int(pokemonPlayer.health) - dmg
            rocketOptions.remove(choice)
        case 5:
            stab = 1.5 if rocketMoves[4].type == pokemonRocket.type else 1
            typeEff = typeMatchup(rocketMoves[4], pokemonPlayer)  # type matchup function
            dmg = calculateDamage(int(rocketMoves[4].power), int(pokemonRocket.attack), int(pokemonPlayer.defense), stab, typeEff)
            print("Team rockets ",pokemonRocket.getType(), pokemonRocket.name, colors.reset, " used ", rocketMoves[4].getType(),
                  rocketMoves[4].name, colors.reset, " on ", pokemonPlayer.getType(), pokemonPlayer.name, colors.reset)
            print("Damage to ", pokemonPlayer.getType(), pokemonPlayer.name, colors.reset, " is ", dmg)
            pokemonPlayer.health = int(pokemonPlayer.health) - dmg
            rocketOptions.remove(choice)
    #dictionary that is returned
    rocketData = {
        "pokemonPlayer": pokemonPlayer,
        "pokemonRocket":pokemonRocket,
        'rocketOptions':rocketOptions
    }
    return rocketData

#function to add pokemon to a que
def addpokemon(array: Pokemon,que):
    #we get a random index since we need to take a pokemonm from the pokemon array
    index = random.randint(0,(len(array) - 1) )
    #create new pokemon
    randomPokemon = Pokemon(array[index].name, array[index].type, array[index].health,array[index].attack, array[index].defense, array[index].height, array[index].weight, array[index].moves)
    array.pop(index)
    #add to the list
    que.append(randomPokemon)



#function to calculate damage using the
def calculateDamage(power,attackPokemon,defensePokemon,stab,typeEff):
    randomValue = random.uniform(0.5,1) #random value with range 0.5 to 1
    finalValue = (power * (attackPokemon/defensePokemon)) * (stab * typeEff) * randomValue #function for final game value
    finalValue = round(finalValue) #making sure value is whole number
    return finalValue #return final value

#function to calcuate the type matchup of different pokemon
def typeMatchup(move:Moves, pokemonB:Pokemon):
    dmg = 1 # set damage equal to one for the rest of them just follow the chart for types
    if (move.type == "Fire" and pokemonB.type == "Fire") or (move.type == "Fire" and pokemonB.type == "Water"):
        dmg = 0.5
    elif move.type == "Fire" and pokemonB.type == "Grass":
        dmg = 2
    elif move.type == "Water" and pokemonB.type == "Fire":
        dmg = 2
    elif (move.type == "Water" and pokemonB.type == "Water") or (move.type == "Water" and pokemonB.type == "Grass"):
        dmg = 0.5
    elif move.type == "Electric" and pokemonB.type == "Water":
        dmg = 2
    elif (move.type == "Electric" and pokemonB.type == "Electric") or (move.type == "Electric" and pokemonB.type == "Grass"):
        dmg = 0.5
    elif(move.type == "Grass" and pokemonB.type == "Grass") or (move.type == "Grass" and pokemonB.type == "Fire"):
        dmg = 0.5
    elif (move.type == "Grass" and pokemonB.type == "Water"):
        dmg = 2
    else:
        dmg = 1

    return dmg



#module for players moves
def playerTurn(pokemonA: Pokemon,pokemonB: Pokemon,movesArray: Moves,playerAllowed):
    #sets a array of size 4 for adding move data
   playerOptions = [Moves(0,0,0,0,0,0,0)] * 5

    #code for dealing with Magikarp
   if pokemonA.name == "Magikarp":
     for  i in movesArray:
        if pokemonA.moves[0] == i.name:
         playerOptions[0] == i
         print("How will ",colors.fontcolor.blue,"Magkikarp attack ", pokemonB.getType(),pokemonB.name,colors.reset)
         choice = input("1) Tackle")
         while choice != "1":
             print("How will ", colors.fontcolor.blue, "Magkikarp attack ", pokemonB.getType(), pokemonB.name,
                   colors.reset)
             choice = input("1) Tackle")
         dmg = calculateDamage(playerOptions[0], pokemonA, pokemonB)
         print(pokemonA.getType(), pokemonA.name, colors.reset, " used ", playerOptions[0].getType(), playerOptions[0].name, colors.reset,
               " on ", pokemonB.getType(), pokemonB.name, colors.reset)
         print("Damage to ", pokemonB.getType(), pokemonB.name, colors.reset, " is ", dmg)
         pokemonB.health = int(pokemonB.health) - dmg
         playerData = {
             "pokemonA": pokemonA,
             "pokemonB": pokemonB
         }
         return playerData




   index = 0
    #algorithm for move data finds the moves in the pokemon and finds the actual move data from that
   for x in pokemonA.moves:
       for i in movesArray:
           if x.strip() == i.name:
               playerOptions[index] = i
               index += 1

   testValue = 0

   #array for displaying things being not available
   notAllowed = ["Not Available!","Not Available!","Not Available!","Not Available!","Not Available!"]
   #if statement to see if things are in list
   if "1" in playerAllowed:
       notAllowed[0] = " "
   if "2" in playerAllowed:
       notAllowed[1] = " "
   if "3" in playerAllowed:
       notAllowed[2] = " "
   if "4" in playerAllowed:
       notAllowed[3] = " "
   if "5" in playerAllowed:
       notAllowed[4] = " "


   #while loop for player choices this prints a menu and makes sure player makes a valid choice
   while testValue == 0:
       print("How will ", pokemonA.getType(), pokemonA.name, colors.reset, " attack ", pokemonB.getType(),
             pokemonB.name, colors.reset)
       print("1) ", playerOptions[0].getType(), playerOptions[0].name, colors.reset,colors.fontcolor.pink,notAllowed[0],colors.reset)
       print("2) ", playerOptions[1].getType(), playerOptions[1].name, colors.reset,colors.reset,colors.fontcolor.pink,notAllowed[1],colors.reset)
       print("3) ", playerOptions[2].getType(), playerOptions[2].name, colors.reset,colors.reset,colors.fontcolor.pink,notAllowed[2],colors.reset)
       print("4) ", playerOptions[3].getType(), playerOptions[3].name, colors.reset,colors.reset,colors.fontcolor.pink,notAllowed[3],colors.reset)
       print("5) ", playerOptions[4].getType(), playerOptions[4].name, colors.reset,colors.reset,colors.fontcolor.pink,notAllowed[4],colors.reset)
       choice = input("Move choice? -> ")

       for c in playerAllowed:
           if choice == c:
               testValue = choice

       if testValue == 0:
           print("Cant use the same, until all other moves have been used")



    #switch statement for choice based on what user selects as the move
   match choice:
       #each statement prints
         case "1":
           stab = 1.5 if playerOptions[0].type == pokemonA.type else 1
           typeEff = typeMatchup(playerOptions[0], pokemonB)  # type matchup function
           dmg = calculateDamage(int(playerOptions[0].power), int(pokemonA.attack), int(pokemonB.defense), stab, typeEff)
           print(pokemonA.getType(),pokemonA.name,colors.reset," used ",playerOptions[0].getType(),playerOptions[0].name,colors.reset," on ",pokemonB.getType(),pokemonB.name,colors.reset)
           print("Damage to ",pokemonB.getType(),pokemonB.name,colors.reset," is ",dmg)
           pokemonB.health = int(pokemonB.health) - dmg
           playerAllowed.remove(choice)
         case "2":
           stab = 1.5 if playerOptions[1].type == pokemonA.type else 1
           typeEff = typeMatchup(playerOptions[1], pokemonB)  # type matchup function
           dmg = calculateDamage(int(playerOptions[1].power), int(pokemonA.attack), int(pokemonB.defense), stab, typeEff)
           print(pokemonA.getType(),pokemonA.name,colors.reset," used ", playerOptions[1].getType(), playerOptions[1].name, colors.reset, " on ", pokemonB.getType(), pokemonB.name, colors.reset)
           print("Damage to ", pokemonB.getType(), pokemonB.name, colors.reset, " is ", dmg)
           pokemonB.health = int(pokemonB.health) - dmg
           playerAllowed.remove(choice)
         case "3":
           stab = 1.5 if playerOptions[2].type == pokemonA.type else 1
           typeEff = typeMatchup(playerOptions[2], pokemonB)  # type matchup function
           dmg = calculateDamage(int(playerOptions[2].power), int(pokemonA.attack), int(pokemonB.defense), stab, typeEff)
           print(pokemonA.getType(),pokemonA.name,colors.reset," used ", playerOptions[2].getType(), playerOptions[2].name, colors.reset, " on ", pokemonB.getType(),pokemonB.name, colors.reset)
           print("Damage to ", pokemonB.getType(), pokemonB.name, colors.reset, " is ", dmg)
           pokemonB.health = int(pokemonB.health) - dmg
           playerAllowed.remove(choice)
         case "4":
           stab = 1.5 if playerOptions[3].type == pokemonA.type else 1
           typeEff = typeMatchup(playerOptions[3], pokemonB)  # type matchup function
           dmg = calculateDamage(int(playerOptions[3].power), int(pokemonA.attack), int(pokemonB.defense), stab, typeEff)
           print(pokemonA.getType(),pokemonA.name,colors.reset," used ", playerOptions[3].getType(), playerOptions[3].name, colors.reset, " on ", pokemonB.getType(),pokemonB.name, colors.reset)
           print("Damage to ", pokemonB.getType(), pokemonB.name, colors.reset, " is ", dmg)
           pokemonB.health = int(pokemonB.health) - dmg
           playerAllowed.remove(choice)
         case "5":
           stab = 1.5 if playerOptions[4].type == pokemonA.type else 1
           typeEff = typeMatchup(playerOptions[4], pokemonB)  # type matchup function
           dmg = calculateDamage(int(playerOptions[4].power), int(pokemonA.attack), int(pokemonB.defense), stab, typeEff)
           print(pokemonA.getType(),pokemonA.name,colors.reset, " used ", playerOptions[4].getType(), playerOptions[4].name, colors.reset, " on ", pokemonB.getType(),pokemonB.name, colors.reset)
           print("Damage to ", pokemonB.getType(), pokemonB.name, colors.reset, " is ", dmg)
           pokemonB.health = int(pokemonB.health) - dmg
           playerAllowed.remove(choice)
         case _:
           print("Invalid please enter a proper number! From 1 - 5")
           playerTurn(pokemonA,pokemonB,movesArray,playerAllowed)
   playerData = { #return data about the move with Pokemon A,  B , and the allowed moves
 "pokemonA":pokemonA, #players pokemon
 "pokemonB":pokemonB, #attackers pokemon
 "playerAllowed":playerAllowed #allowed moves array
}
   return playerData



# This is a refrence for how the move array worksprint(playerQue[0].moves[0])

pokemonArray = []
movesArray = []
playerQue = []
rocketQue = []
# this is where I read in the file
with open('pokemon-data.csv', 'r') as file:
    fileLine = file.readline()
    #read the file until the end of the file
    while fileLine:
        fileLine = file.readline()
        fileLine = fileLine.replace('[', '').replace(']', '').replace('"', '').replace("'","")
        pokemonData = fileLine.split(",")
        #if the pokemon length is greater than one
        if len(pokemonData) > 1:
            pokemonName = pokemonData[0]
            pokemonType = pokemonData[1]
            pokemonHealth = pokemonData[2]
            pokemonAttack = pokemonData[3]
            pokemonDefense = pokemonData[4]
            pokemonHeight = pokemonData[5]
            pokemonWeight = pokemonData[6]
            pokemonMove1 = pokemonData[7]
            #if magikarp do this
            if len(pokemonData) == 8:
                userPokemon = Pokemon(pokemonName, pokemonType, pokemonHealth, pokemonAttack, pokemonDefense,
                                         pokemonHeight, pokemonWeight, pokemonMove1)
                pokemonArray.append(userPokemon)
            #if not magikarp do this
            elif len(pokemonData) > 8:
                pokemonMove2 = pokemonData[8]
                pokemonMove3 = pokemonData[9]
                pokemonMove4 = pokemonData[10]
                pokemonMove5 = pokemonData[11]
                userPokemon = Pokemon(pokemonName, pokemonType, pokemonHealth, pokemonAttack, pokemonDefense,
                                         pokemonHeight, pokemonWeight,
                                         [pokemonMove1, pokemonMove2, pokemonMove3, pokemonMove4, pokemonMove5])
                pokemonArray.append(userPokemon)

#file processing for the moves
with open('moves-data.csv', 'r') as file:
    fileLine = file.readline()
    while fileLine:  #until the file is empty keep reading lines
        fileLine = file.readline()
        pokemonData = fileLine.split(",")
        if len(pokemonData) > 1: #checking for errors
            moveName = pokemonData[0]
            moveType = pokemonData[1]
            moveCatagory = pokemonData[2]
            moveContest = pokemonData[3]
            movePP = pokemonData[4]
            movePower = pokemonData[5]
            moveAccuracy = pokemonData[6]
            newMove = Moves(moveName, moveType, moveCatagory, moveContest, movePP, movePower, moveAccuracy)
            movesArray.append(newMove)




#start welcoming the players to the game and running the game
print(colors.fontcolor.yellow,r"""
_________       __                                 
\______   \____ |  | __ ____   _____   ____   ____  
 |     ___/  _ \|  |/ // __ \ /     \ /  _ \ /    \ 
 |    |  (  <_> )    <\  ___/|  Y Y  (  <_> )   |  \
 |____|   \____/|__|_ \\___  >__|_|  /\____/|___|  /
              ___    \/    \/      \/            \/ 
  ____       |  |   ____  ______ ______ ____  __ __  _____  
_/ ___\/  _ \|  |  /  _ \/  ___//  ___// __ \|  |  \/     \ 
\  \__(  <_> )  |_(  <_> )___ \ \___ \\  ___/|  |  /  Y Y  \
 \___  >____/|____/\____/____  >____  >\___  >____/|__|_|  /
     \/                      \/     \/     \/            \/ 
                                
""",colors.reset)
#welcoming section for the project
print("Developed by",colors.fontcolor.purple,"Cameron Davis",colors.reset)
print("Professor",colors.fontcolor.purple,"Dr.Liu Xudong",colors.reset)
playerName = input("Enter your player Name: ")
countPlay = 3
aiPlay = 3
#code for adding the pokemon to the team rocket que
while aiPlay != 0:
    addpokemon(pokemonArray,rocketQue)
    aiPlay -= 1

colRocket1 = rocketQue[0].getType()
colRocket2 = rocketQue[1].getType()
colRocket3 = rocketQue[2].getType()

#print team rockets intro
print("Team Rocket enters with ",colRocket1,rocketQue[0].name,colors.reset,colRocket2,rocketQue[1].name,colors.reset,colRocket3,rocketQue[2].name,colors.reset)

#code for adding the pokemon to the player que
while countPlay != 0:
    addpokemon(pokemonArray,playerQue)
    countPlay -= 1

#setting colors for each item in que
colPlayer1 = playerQue[0].getType()
colPlayer2 = playerQue[1].getType()
colPlayer3 = playerQue[2].getType()
print("Team ",  playerName ," enters with ",colPlayer1,playerQue[0].name,colors.reset,colPlayer2,playerQue[1].name,colors.reset,colPlayer3,playerQue[2].name,colors.reset)


#flipping the coin heads or tails but with 1 and 2
coinToss = random.randint(1,2)


print("flipping the coin and the answer is ....")

#setting loop to true
gameLoop = True


#declaring arrays for players taking turns
playerTurns = []
rocketTurns = []

#declaring arrays for validating moves
rocketOptions = [1,2,3,4,5]
playerOptions = ["1","2","3","4","5"]


#coin toss for random choices
if coinToss == 1:
    print(colors.fontcolor.purple,playerName,colors.reset," has won the coin toss and will go first")
    print("Let the battle begin!")
    playerData = playerTurn(playerQue[0], rocketQue[0], movesArray,playerOptions)
    rocketQue[0].health = playerData["pokemonB"].health
    rocketQue[0].health = 0 if rocketQue[0].health < 0 else rocketQue[0].health
    print(colors.fontcolor.red,"Team Rocket ",colors.reset,rocketQue[0].getType(), rocketQue[0].name, colors.reset, " is at ", rocketQue[0].health)
    playerTurns.append(1)  #we need to append to the turns to see who went last

#else we start with team rocket
else:
    print(colors.fontcolor.red,"Team Rocket has won the coin toss and will go first!",colors.reset)
    print("Let the Battle Begin!")
    rocketData = rocketMove(rocketQue[0], movesArray, playerQue[0],rocketOptions)
    playerQue[0].health = rocketData["pokemonPlayer"].health
    playerQue[0].health = 0 if playerQue[0].health < 0 else playerQue[0].health
    print(colors.fontcolor.purple,playerName,"'s ",colors.reset,playerQue[0].getType(), playerQue[0].name, colors.reset, " is at ", playerQue[0].health)
    rocketTurns.append(1) #we need to append to the turns to see who went last

#starting the game loop
while(gameLoop):



    #checking team rocket que
    if int(rocketQue[0].health) <= 0:
        print("Now ",colors.fontcolor.red,"Team Rocket",colors.reset,rocketQue[0].getType(),rocketQue[0].name,colors.reset," faints into its pokeball")
        rocketQue.pop(0)
        rocketOptions = [1,2,3,4,5]
        if len(rocketTurns) > 1:   #resetting the moves
            del rocketData
        if len(rocketQue) != 0:
            print("Team Rocket sends out  ", rocketQue[0].getType(), rocketQue[0].name, colors.reset, " to battle you next!")


    #checking player health que
    if int(playerQue[0].health) <= 0:
        print(colors.fontcolor.purple,playerName,"'s ",colors.reset,playerQue[0].getType(),playerQue[0].name,colors.reset," faints into its pokeball")
        playerQue.pop(0)
        playerOptions = ["1","2","3","4","5"]
        if len(playerTurns) > 1:  #resetting the moves
            del playerData
        if len(playerQue) != 0:
          print(playerQue[0].getType(),playerQue[0].name,colors.reset," is up next for ",colors.fontcolor.purple,playerName,colors.reset," in this Pokemon battle!")


    #checking who should take the current move
    if len(playerTurns) > len(rocketTurns):
        if bool(rocketQue) == False:
            print(colors.fontcolor.yellow, "Team Rocket has been defeated")
            print(playerName, " beat the colosseum!!!!!")
            gameLoop = False
        else:
            print(colors.fontcolor.red,"Team Rockets turn",colors.reset)
            rocketData = rocketMove(rocketQue[0], movesArray, playerQue[0],rocketOptions)
            playerQue[0].health = rocketData["pokemonPlayer"].health
            playerQue[0].health = 0 if playerQue[0].health < 0 else playerQue[0].health
            print(colors.fontcolor.purple,playerName,"'s ",colors.reset,playerQue[0].getType(), playerQue[0].name, colors.reset, " is at ", playerQue[0].health)
            rocketTurns.append(1)
            # to stop a infinite loop if the len of the tokens equal append to say rocket went most recent
            if len(rocketTurns) == len(playerTurns):
                rocketTurns.append(1)
    elif len(rocketTurns) > len(playerTurns):
        # checking to see if player que is empty
        if bool(playerQue) == False:
            print(colors.fontcolor.red, "Team Rocket has won")
            print(playerName, " you loose")
            gameLoop = False
        else:
            #if  the array is not empty we are going to allow the play er to make a move
            print(colors.fontcolor.purple,playerName,colors.reset, "your up!")
            playerData = playerTurn(playerQue[0], rocketQue[0], movesArray,playerOptions)
            rocketQue[0].health = playerData["pokemonB"].health
            rocketQue[0].health = 0 if rocketQue[0].health < 0 else rocketQue[0].health
            print(colors.fontcolor.red,"Team Rocket ",colors.reset,rocketQue[0].getType(),rocketQue[0].name,colors.reset," is at ",rocketQue[0].health)
            playerTurns.append(1)
            #to stop a infinite loop if the len of the tokens equal append to say player went most recent
            if len(rocketTurns) == len(playerTurns):
                playerTurns.append(1)

