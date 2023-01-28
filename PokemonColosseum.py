#Cameron Davis
#Dr.Liu
#1/27/2023
#Intro to AI

from pokemon import newPokemon

pokemonArray = []
#this is where I read in the file
with open('pokemon-data.csv', 'r') as file:
    fileLine = file.readline()
    while fileLine:
        fileLine = file.readline()
        fileLine = fileLine.replace('[','').replace(']','').replace('"','')
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
             userPokemon = newPokemon(pokemonName,pokemonType,pokemonHealth,pokemonAttack,pokemonDefense,pokemonHeight,pokemonWeight,pokemonMove1)
             print(userPokemon.name)
            elif len(pokemonData) > 8:
                pokemonMove2 = pokemonData[8]
                pokemonMove3 = pokemonData[9]
                pokemonMove4 = pokemonData[10]
                pokemonMove5 = pokemonData[11]
                userPokemon = newPokemon(pokemonName,pokemonType,pokemonHealth,pokemonAttack,pokemonDefense,pokemonHeight,pokemonWeight,[pokemonMove1,pokemonMove2,pokemonMove3,pokemonMove4,pokemonMove5])
                print(userPokemon.name)




