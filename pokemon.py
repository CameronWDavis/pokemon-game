from Color import colors #import for color

class newPokemon:
    def __init__(self,name,type,health,attack,defense,height,weight,moves):
        self.name = name
        self.type = type
        self.health = health
        self.attack = attack
        self.defense = defense
        self.weight = weight
        self.height = height
        self.moves = moves

    def getType(self):
        color = ""
        match self.type:
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

