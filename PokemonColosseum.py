# Cameron Davis
# Dr.Liu
# 1/27/2023
# Intro to AI

#import statements for other python modules
import random #import for random number generation
from pokemon import newPokemon #import for pokemon object
from que import Queue #import for que
from Color import colors #import for color
from mechanics import Moves #import for moves


def addpokemon(array: newPokemon,que):
    index = random.randint(0,(len(array) - 1) )
    randomPokemon = newPokemon(array[index].name, array[index].type, array[index].health,array[index].attack, array[index].defense, array[index].height, array[index].weight, array[index].moves)
    array.pop(index)
    que.append(randomPokemon)
#function is used to get type of pokemon and match a color with that
def getType(pokemon:newPokemon):
    color = ""
    match pokemon.type:
        case "Electric":
             color = colors.fontcolor.yellow
             return color
        case "Fire":
            color = colors.fontcolor.red
            return color
        case "Water":
            color = colors.fontcolor.blue
            return color
        case "Grass":
            color = colors.fontcolor.green
            return color
        case "Normal":
            color = colors.fontcolor.lightgrey
            return color

#function to calculate damage using the
def calculateDamage(move:Moves,pokemonA:newPokemon,pokemonB:newPokemon):
    power = move.power
    attackPokemon = pokemonA.attack
    defensePokemon = pokemonB.defense
    stab = 1.5 if move.type == pokemonA.type else 1


pokemonArray = []
movesArray = []
playerQue = []
rocketQue = []
# this is where I read in the file
with open('pokemon-data.csv', 'r') as file:
    fileLine = file.readline()
    while fileLine:
        fileLine = file.readline()
        fileLine = fileLine.replace('[', '').replace(']', '').replace('"', '')
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
                     \/    \/      \/            \/ 
             .__  .__                                            
  ____  ____ |  | |  |   ____  ______ ______ ____  __ __  _____  
_/ ___\/  _ \|  | |  |  /  _ \/  ___//  ___// __ \|  |  \/     \ 
\  \__(  <_> )  |_|  |_(  <_> )___ \ \___ \\  ___/|  |  /  Y Y  \
 \___  >____/|____/____/\____/____  >____  >\___  >____/|__|_|  /
     \/                           \/     \/     \/            \/
                                
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

colRocket1 = getType(rocketQue[0])
colRocket2 = getType(rocketQue[1])
colRocket3 = getType(rocketQue[2])

#print team rockets intro
print("Team Rocket enters with ",colRocket1,rocketQue[0].name,colors.reset,colRocket2,rocketQue[1].name,colors.reset,colRocket3,rocketQue[2].name,colors.reset)

#code for adding the pokemon to the player que
while countPlay != 0:
    addpokemon(pokemonArray,playerQue)
    countPlay -= 1
colPlayer1 = getType(playerQue[0])
colPlayer2 = getType(playerQue[1])
colPlayer3 = getType(playerQue[2])
print("Team ",  playerName ," enters with ",colPlayer1,playerQue[0].name,colors.reset,colPlayer2,playerQue[1].name,colors.reset,colPlayer3,playerQue[2].name,colors.reset)

coinToss = random.randint(1,2)






