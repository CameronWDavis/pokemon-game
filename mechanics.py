from Color import colors #import for color
#author Cameron Davis
#this is a class to generate a move object
class Moves:
#this is a constructor for the move
#move object
    def __init__(self, name, type,category, contest, PP, power,accuracy):
        self.name = name
        self.type = type
        self.category = category
        self.contest = contest
        self.PP = PP
        self.power = power
        self.accuracy = accuracy

 #this gets the type of a move to send back the color
    def getType(self):
        color = ""
        match self.type:
            case "Electric":
                color = colors.fontcolor.yellow #color asci codes
                return color
            case "Fire":
                color = colors.fontcolor.red
                return color
            case "Water": #this  is color for the pokemon types
                color = colors.fontcolor.blue
                return color
            case "Grass":
                color = colors.fontcolor.green
                return color
            case "Normal":
                color = colors.fontcolor.lightgrey
                return color
            case _:
                 color = colors.fontcolor.lightgrey
                 return color
