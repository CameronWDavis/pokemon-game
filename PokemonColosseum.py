# Cameron Davis
# Dr.Liu
# 1/27/2023
# Intro to AI

#import statements for other python modules
import random #import for random number generation
from pokemon import newPokemon #import for pokemon object
from Color import colors #import for color
from mechanics import Moves #import for moves



#this is the moveset for team rocket
def rocketMove(pokemonRocket: newPokemon, moveArray, pokemonPlayer:newPokemon):
    # algorithm for move data finds the moves in the pokemon and finds the actual move data from that
    rocketMoves = [1,2,3,4,5]
    choice = random.choice(rocketMoves)

    index = 0
    for x in pokemonRocket.moves:
        for i in moveArray:
            if x.strip() == i.name:
                rocketMoves[index] = i
                index += 1
    match choice:
        case 1:
            dmg = calculateDamage(rocketMoves[0], pokemonRocket, pokemonPlayer)
            print("Team rockets ", pokemonRocket.getType(), pokemonRocket.name, colors.reset, " used ", rocketMoves[0].getType(), rocketMoves[0].name, colors.reset," on ", pokemonPlayer.getType(), pokemonPlayer.name, colors.reset)
            print("Damage to ", pokemonPlayer.getType(), pokemonPlayer.name, colors.reset, " is ", dmg)
            pokemonPlayer.health = int(pokemonPlayer.health) - dmg
            rocketMoves.pop(0)
        case 2:
            dmg = calculateDamage(rocketMoves[1], pokemonRocket, pokemonPlayer)
            print("Team rockets ",pokemonRocket.getType(), pokemonRocket.name, colors.reset, " used ", rocketMoves[1].getType(),rocketMoves[1].name, colors.reset, " on ", pokemonPlayer.getType(), pokemonPlayer.name, colors.reset)
            print("Damage to ", pokemonPlayer.getType(), pokemonPlayer.name, colors.reset, " is ", dmg)
            pokemonPlayer.health = int(pokemonPlayer.health) - dmg
            rocketMoves.pop(1)
        case 3:
            dmg = calculateDamage(rocketMoves[2], pokemonRocket, pokemonPlayer)
            print("Team rockets ",pokemonRocket.getType(), pokemonRocket.name, colors.reset, " used ", rocketMoves[2].getType(),rocketMoves[2].name, colors.reset, " on ", pokemonPlayer.getType(), pokemonPlayer.name, colors.reset)
            print("Damage to ", pokemonPlayer.getType(), pokemonPlayer.name, colors.reset, " is ", dmg)
            pokemonPlayer.health = int(pokemonPlayer.health) - dmg
            rocketMoves.pop(2)
        case 4:
            dmg = calculateDamage(rocketMoves[3], pokemonRocket, pokemonPlayer)
            print("Team rockets ",pokemonRocket.getType(), pokemonRocket.name, colors.reset, " used ", rocketMoves[3].getType(),
                  rocketMoves[3].name, colors.reset, " on ", pokemonPlayer.getType(), pokemonPlayer.name, colors.reset)
            print("Damage to ", pokemonPlayer.getType(), pokemonPlayer.name, colors.reset, " is ", dmg)
            pokemonPlayer.health = int(pokemonPlayer.health) - dmg
            rocketMoves.pop(3)
        case 5:
            dmg = calculateDamage(rocketMoves[4], pokemonRocket, pokemonPlayer)
            print("Team rockets ",pokemonRocket.getType(), pokemonRocket.name, colors.reset, " used ", rocketMoves[4].getType(),
                  rocketMoves[4].name, colors.reset, " on ", pokemonPlayer.getType(), pokemonPlayer.name, colors.reset)
            print("Damage to ", pokemonPlayer.getType(), pokemonPlayer.name, colors.reset, " is ", dmg)
            pokemonPlayer.health = int(pokemonPlayer.health) - dmg
            rocketMoves.pop(4)
    rocketData = {
        "pokemonPlayer": pokemonPlayer,
        "pokemonRocket":pokemonRocket
    }
    return rocketData


def addpokemon(array: newPokemon,que):
    index = random.randint(0,(len(array) - 1) )
    randomPokemon = newPokemon(array[index].name, array[index].type, array[index].health,array[index].attack, array[index].defense, array[index].height, array[index].weight, array[index].moves)
    array.pop(index)
    que.append(randomPokemon)


#function to calculate damage using the
def calculateDamage(move:Moves,pokemonA:newPokemon,pokemonB:newPokemon):
    power = int(move.power)
    attackPokemon = int(pokemonA.attack)
    defensePokemon = int(pokemonB.defense)
    stab = 1.5 if move.type == pokemonA.type else 1
    TE = typeMatchup(move, pokemonB)
    randomValue = random.uniform(0.5,1)
    finalValue = (power * (attackPokemon/defensePokemon)) * (stab * TE) * randomValue
    finalValue = round(finalValue)
    return finalValue

def typeMatchup(move:Moves, pokemonB:newPokemon):
    dmg = 1
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
    elif move.type == "Grass" and pokemonB.type == "Water":
        dmg = 2
    else:
        dmg = 1

    return dmg

#module for players moves
def playerTurn(pokemonA: newPokemon,pokemonB: newPokemon,movesArray: Moves):
    #sets a array of size 4 for adding move data
   playerOptions = [0,1,2,3,4]
   index = 0
    #algorithm for move data finds the moves in the pokemon and finds the actual move data from that
   for x in pokemonA.moves:
       for i in movesArray:
           if x.strip() == i.name:
               playerOptions[index] = i
               index += 1


   #setting the color of the moves and displaying for the user
   color0 = playerOptions[0].getType()
   color1 = playerOptions[1].getType()
   color2 = playerOptions[2].getType()
   color3 = playerOptions[3].getType()
   color4 = playerOptions[4].getType()
   print("How will ",pokemonA.getType(),pokemonA.name,colors.reset," attack ",pokemonB.getType(),pokemonB.name,colors.reset)
   print("1) ",color0,playerOptions[0].name,colors.reset)
   print("2) ",color1,playerOptions[1].name,colors.reset)
   print("3) ",color2,playerOptions[2].name,colors.reset)
   print("4) ",color3,playerOptions[3].name,colors.reset)
   print("5) ",color4,playerOptions[4].name,colors.reset)
   choice = input("Move choice? -> ")
   choice = choice

    #switch statement for choice based on what user selects as the move
   match choice:
         case "1":
           dmg = calculateDamage(playerOptions[0],pokemonA,pokemonB)
           print(pokemonA.getType(),pokemonA.name,colors.reset," used ",color0,playerOptions[0].name,colors.reset," on ",pokemonB.getType(),pokemonB.name,colors.reset)
           print("Damage to ",pokemonB.getType(),pokemonB.name,colors.reset," is ",dmg)
           pokemonB.health = int(pokemonB.health) - dmg
           #options.pop(0)
         case "2":
           dmg = calculateDamage(playerOptions[1], pokemonA, pokemonB)
           print(pokemonA.getType(),pokemonA.name,colors.reset," used ", color1, playerOptions[1].name, colors.reset, " on ", pokemonB.getType(), pokemonB.name, colors.reset)
           print("Damage to ", pokemonB.getType(), pokemonB.name, colors.reset, " is ", dmg)
           pokemonB.health = int(pokemonB.health) - dmg
           #options.pop(1)
         case "3":
           dmg = calculateDamage(playerOptions[2], pokemonA, pokemonB)
           print(pokemonA.getType(),pokemonA.name,colors.reset," used ", color2, playerOptions[2].name, colors.reset, " on ", pokemonB.getType(),pokemonB.name, colors.reset)
           print("Damage to ", pokemonB.getType(), pokemonB.name, colors.reset, " is ", dmg)
           pokemonB.health = int(pokemonB.health) - dmg
           #options.pop(2)
         case "4":
           dmg = calculateDamage(playerOptions[3], pokemonA, pokemonB)
           print(pokemonA.getType(),pokemonA.name,colors.reset," used ", color3, playerOptions[3].name, colors.reset, " on ", pokemonB.getType(),pokemonB.name, colors.reset)
           print("Damage to ", pokemonB.getType(), pokemonB.name, colors.reset, " is ", dmg)
           pokemonB.health = int(pokemonB.health) - dmg
           #options.pop(3)
         case "5":
           dmg = calculateDamage(playerOptions[4], pokemonA, pokemonB)
           print(pokemonA.getType(),pokemonA.name,colors.reset, " used ", color4, playerOptions[4].name, colors.reset, " on ", pokemonB.getType(),pokemonB.name, colors.reset)
           print("Damage to ", pokemonB.getType(), pokemonB.name, colors.reset, " is ", dmg)
           pokemonB.health = int(pokemonB.health) - dmg
           #options.pop(4)
         case _:
           print("Invalid please enter a proper number! From 1 - 5")
           playerTurn(pokemonA,pokemonB,movesArray)
   playerData = {
 "pokemonA":pokemonA,
 "pokemonB":pokemonB
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
    while fileLine:
        fileLine = file.readline()
        fileLine = fileLine.replace('[', '').replace(']', '').replace('"', '').replace("'","")
        pokemonData = fileLine.split(",")
        if len(pokemonData) > 1:
            pokemonName = pokemonData[0]
            pokemonType = pokemonData[1]
            pokemonHealth = pokemonData[2]
            pokemonAttack = pokemonData[3]
            pokemonDefense = pokemonData[4]
            pokemonHeight = pokemonData[5]
            pokemonWeight = pokemonData[6]
            pokemonMove1 = pokemonData[7]
            if len(pokemonData) == 8:
                userPokemon = newPokemon(pokemonName, pokemonType, pokemonHealth, pokemonAttack, pokemonDefense,
                                         pokemonHeight, pokemonWeight, pokemonMove1)
                pokemonArray.append(userPokemon)
            elif len(pokemonData) > 8:
                pokemonMove2 = pokemonData[8]
                pokemonMove3 = pokemonData[9]
                pokemonMove4 = pokemonData[10]
                pokemonMove5 = pokemonData[11]
                userPokemon = newPokemon(pokemonName, pokemonType, pokemonHealth, pokemonAttack, pokemonDefense,
                                         pokemonHeight, pokemonWeight,
                                         [pokemonMove1, pokemonMove2, pokemonMove3, pokemonMove4, pokemonMove5])
                pokemonArray.append(userPokemon)

with open('moves-data.csv', 'r') as file:
    fileLine = file.readline()
    while fileLine:
        fileLine = file.readline()
        pokemonData = fileLine.split(",")
        if len(pokemonData) > 1:
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
colPlayer1 = playerQue[0].getType()
colPlayer2 = playerQue[1].getType()
colPlayer3 = playerQue[2].getType()
print("Team ",  playerName ," enters with ",colPlayer1,playerQue[0].name,colors.reset,colPlayer2,playerQue[1].name,colors.reset,colPlayer3,playerQue[2].name,colors.reset)
#these arrays are for verifying moves
options = [1,2,3,4,5]
choiceArray = [0,1,2,3,4]
#flipping the coin heads or tails but with 1 and 2
coinToss = random.randint(1,2)


print("flipping the coin and the answer is ....")
gameLoop = True


#declaring arrays for players taking turns
playerTurns = []
rocketTurns = []

if coinToss == 1:
    print(colors.fontcolor.purple,playerName,colors.reset," has won the coin toss and will go first")
    print("Let the battle begin!")
    playerData = playerTurn(playerQue[0], rocketQue[0], movesArray)
    rocketQue[0].health = playerData["pokemonB"].health
    playerTurns.append(1)

else:
    print(colors.fontcolor.red,"Team Rocket has won the coin toss and will go first!",colors.reset)
    print("Let the Battle Begin")
    rocketData = rocketMove(rocketQue[0], movesArray, playerQue[0])
    playerQue[0].health = rocketData["pokemonPlayer"].health
    rocketTurns.append(1)

#starting the game loop
while(gameLoop):



    #checking team rocket que
    if int(rocketQue[0].health) <= 0:
        print("Now ",rocketQue[0].getType(),rocketQue[0].name,colors.reset," faints into its pokeball")
        rocketQue.pop(0)
        if len(rocketQue) != 0:
            print("Team Rocket sends out  ", rocketQue[0].getType(), rocketQue[0].name, colors.reset, " to battle you next!")


    #checking player health que
    if int(playerQue[0].health) <= 0:
        print("Now ",playerQue[0].getType(),playerQue[0].name,colors.reset," faints into its pokeball")
        playerQue.pop(0)
        if len(playerQue) != 0:
          print("Now ",playerQue[0].getType(),playerQue[0].name,colors.reset," your up to battle next!")


    #checking who should take the current move
    if len(playerTurns) > len(rocketTurns):
        if bool(rocketQue) == False:
            print(colors.fontcolor.yellow, "Team Rocket has been defeated")
            print(playerName, " beat the colosseum!!!!!")
            gameLoop = False
        else:
            print(colors.fontcolor.red,"Team Rockets turn",colors.reset)
            rocketData = rocketMove(rocketQue[0], movesArray, playerQue[0])
            playerQue[0].health = rocketData["pokemonPlayer"].health
            rocketTurns.append(1)
            if len(rocketTurns) == len(playerTurns):
                rocketTurns.append(1)
    elif len(rocketTurns) > len(playerTurns):
        # checking to see if player que is empty
        if bool(playerQue) == False:
            print(colors.fontcolor.red, "Team Rocket has won")
            print(playerName, " you loose")
            gameLoop = False
        else:
            print(colors.fontcolor.purple,playerName,colors.reset, "your up!")
            playerData = playerTurn(playerQue[0], rocketQue[0], movesArray)
            rocketQue[0].health = playerData["pokemonB"].health
            playerTurns.append(1)
            if len(rocketTurns) == len(playerTurns):
                playerTurns.append(1)


