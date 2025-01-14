import random
# region boat
class boat:
    def __init__(self,nome):
        self.nome = nome
        self.hp = 100
        self.eff = 'normal'
        self.gold = 100
        self.rep = 50

    def showStatus(self):
        return f'\n|[Status de {self.nome}]:\n| - HP:[{self.hp}/100]\n| - eff: {self.eff}\n| - ouro: {self.gold}\n| - reputação:{self.rep}\n'

    def addEffect(self,):
        pass
# endregion

# region item
class item:
    def __init__(self,qnt = 0,val = 1):
        self._qnt = qnt
        self.val = val
    
    def changeqnt(self,x):
        if self._qnt >= x:
            self._qnt+=x
            return 1
        else:
            return 0

class passItem(item):
    def __init__(self, perday, qnt=0, val=1):
        super().__init__(qnt, val)
        self.perday = perday

class activeItem(item):
    def __init__(self, eff = 'none', qnt=0, val=1):
        super().__init__(qnt, val)
        self.eff = eff
# endregion

# region pirate
class pirate:
    def __init__(self,
                name = 'pirate_group',
                hp = 100,
                adj = 'null',
                status = 'normal',
                eff_cap = 'null',
                ) -> None:
        self.name = name
        self.hp = hp
        self.adj = adj
        self.status = status
        self.eff_cap = eff_cap
# endregion

# region island
islandnames = ['guaxupé','muzambinho']
islandeffects = [
    ['tired','hungry','weak',],
    ['tired','weak','hungry','hurt','poisoned','bleeding'],
    ['tired','weak','hungry','hurt','poisoned','bleeding','ckripled','burnt','mad','traidor']
]
class island:
    def __init__(self,
                dif = 'medium',
                explored = False
                ):
        
        self.name = random.choice(islandnames)
        self.explored = explored


        if dif == 'easy':
            self._dif = dif
            self.loot = 10
            self.death = 0.05
            self.caract = random.choice(['beatch','forest','merchant','village'])
            
            if random.randint(1,5) == 1:
                self._eff = random.choice(islandeffects[1])
            else:
                self._eff = 'normal'

        elif dif == 'medium':
            self._dif = dif
            self.loot = 50
            self.death = 0.10
            self.caract = random.choice(['beatch','forest','merchant','village'])

            if random.randint(1,4) == 1:
                self._eff = random.choice(islandeffects[2])
            else:
                self._eff = 'normal'

        elif dif == 'hard':
            self._dif = dif
            self.loot = 100
            self.death = 0.20
            self.caract = random.choice(['beatch','forest','merchant','village'])
            
            if random.randint(1,3) == 1:
                self._eff = random.choice(islandeffects[3])
            else:
                self._eff = 'normal'
              
class outpost(island):
    def __init__(self, explored=True, lv = 1):
        super().__init__(explored)
        self.lv = lv

        # TODO : success rate in outposts
        match lv:
            case 1:
                self.name = 'crakudas'
                self._dif = 'very hard'
                self.loot = 200
                self.death = 0.35
                self.caract = 'rocky'
                self._eff = 'hurt'
                
            case 2:
                self.name = 'kudomagu'
                self._dif = 'very hard'
                self.loot = 220
                self.death = 0.45
                self.caract = 'jungle'
                self._eff = 'poisoned'
            
            case 3:
                self.name = 'kúdaokada'
                self._dif = 'very hard'
                self.loot = 220
                self.death = 0.45
                self.caract = 'lava'
                self._eff = 'burnt'

            case 4:
                self.name = 'Áuladujansley'
                self._dif = 'very hard'
                self.loot = 220
                self.death = 0.45
                self.caract = 'cult'
                self._eff = 'mad'
            
            case 5:
                self.name = 'Capital'
                self._dif = 'very hard'
                self.loot = 999
                self.death = 0.
                self.caract = 'cult'
                self._eff = 'mad'
            

# endregion