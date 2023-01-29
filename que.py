from pokemon import newPokemon
class Queue:
    def __int__(self):
        self.elements = []


    def addQue(self,item:newPokemon):
        self.elements.insert(0,item)

    def removeQue(self):
        if not self.isEmpty():
            return self.elements.pop(0)


    def isEmpty(self):
        if len(self) == 0:
            return  True