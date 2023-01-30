from Color import colors #import for color
class Moves:

    def __init__(self, name, type,category, contest, PP, power,accuracy):
        self.name = name
        self.type = type
        self.category = category
        self.contest = contest
        self.PP = PP
        self.power = power
        self.accuracy = accuracy


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
            case _:
                 color = colors.fontcolor.lightgrey
                 return co
