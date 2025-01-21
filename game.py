import os, random

log = []

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
    def __init__(self,name,qnt = 0,val = 1):
        self.name = name
        self.qnt = qnt
        self.val = val
    
    def changeqnt(self,x):
        if self.qnt >= x:
            self.qnt+=x
            return 1
        else:
            return 0

class passItem(item):
    def __init__(self,name, perday, qnt=0, val=1):
        super().__init__(name, qnt, val)
        self.perday = perday

class activeItem(item):
    def __init__(self,name , eff = 'none', qnt=0, val=1):
        super().__init__(name, qnt, val)
        self.eff = eff

    def useItem(self):
        log.append(f'{self.name}_used')
# endregion

# region pirate
pirate_names = [
        "Piratas do Caribe",
    "Bucaneiros",
    "Corsários",
    "Filhos de Poseidon",
    "Mãos de Ferro",
    "Caveiras Negras",
    "Papagaios Falantes",
    "Marujos Fantasmas",
    "Assombradores dos Sete Mares",
    "Reis do Mar"]
class pirate:
    def __init__(self,
                name = random.choice(pirate_names),
                hp = True,
                adj = 'null',
                status = 'normal',
                eff_cap = 'null',
                occupied = False
                ) -> None:
        self.name = name
        self.hp = hp
        self.adj = adj
        self.status = status
        self.eff_cap = eff_cap
        self.occupied = occupied
# endregion

# region island
islandnames = ['guaxupé','muzambinho',
    "Ilha da Caveira",
    "Ilha Perdida",
    "Ilha do Tesouro",
    "Ilha Tortuga",
    "Ilha dos Esqueletos",
    "Ilha Misteriosa",
    "Ilha do Diabo",
    "Ilha das Sombras",
    "Ilha das Sereias",
    "Ilha dos Canibais"]
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
            self.death = 5
            self.caract = random.choice(['beatch','forest','merchant','village'])
            
            if random.randint(1,5) == 1:
                self._eff = random.choice(islandeffects[1])
            else:
                self._eff = 'normal'

        elif dif == 'medium':
            self._dif = dif
            self.loot = 50
            self.death = 10
            self.caract = random.choice(['beatch','forest','merchant','village'])

            if random.randint(1,4) == 1:
                self._eff = random.choice(islandeffects[2])
            else:
                self._eff = 'normal'

        elif dif == 'hard':
            self._dif = dif
            self.loot = 100
            self.death = 20
            self.caract = random.choice(['beatch','forest','merchant','village'])
            
            if random.randint(1,3) == 1:
                self._eff = random.choice(islandeffects[3])
            else:
                self._eff = 'normal'
    
    def raid(self, pirate):
       sucssrate = random.randint(1,100)
       if sucssrate > self.death:
                   #loot
           if pirate:
                pirate.occupied = True
                if pirate.eff == 'none':
                        pirate.eff = self._eff
       else:
           pirate.hp = False
           

    def explore(self, pirate):
        if pirate:
            self.explore = True
            pirate.occupied = True

        
              
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

paraguaio = [
    "Arr! Um tesouro!",
    "Yo ho ho, e uma garrafa de rum!",
    "Cuidado com os canhões!",
    "Terra à vista!",
    "Pega a prancha, vamos surfar!",
    "Argh! Um navio inimigo!",
    "Eu quero um biscoito!",
    "Vamos afundar esse navio!",
    "Tesouro, tesouro!",
    "O capitão está furioso!"
]

inventory_pss = [
    passItem('food',1,5,5),
    passItem('water',1,5,1),
    passItem('wood',1,5,10),
    passItem('cannonball',0,3,50)]
inventory_act = [
    activeItem('medcine', 'cure', 1 ,50),
    activeItem('booze', 'strength', 1 ,30),
    activeItem('fishbait', '+food', 3 ,10)
]

sea = [
    island('easy'),
    island('easy'),
    island('easy'),
    outpost()
]

pirates = [
    pirate()
]
unoccupied_pirates = [

]
for pirata in pirates:
    if pirata.occupied == "False" and pirate.hp:
        unoccupied_pirates.append(pirata)





# region menu
def resouresMenu(inventory_pss,inventory_act):
    while True:
        os.system('cls')

        print(f'|- nome | qnt | val uni')

        for i in range(0,len(inventory_pss)):
            print(f'|- {inventory_pss[i].name}| {inventory_pss[i].qnt} | {inventory_pss[i].val}')

        for i in range(0,len(inventory_act)):
            print(f'|- {inventory_act[i].name}| {inventory_act[i].qnt} | {inventory_act[i].val}')
        
        print('---------------------')
        print('ações:\n1 -> usar recurso\n2 -> cancelar')

        try:
            r = int(input('>>>'))
            if r < 3 and r > 0:
                break
        except:
            input('input invalido, aperte enter para tentar novamente...')
        
    match r:
        case 2:
            return 0
        case 1:
            while True:
                for i in range(0,inventory_act):
                    print(f'|[{i}]| {inventory_act[i].name}| {inventory_act[i].qnt} | {inventory_act[i].val}')
            
                try:
                    r = int(input('>>>'))
                    if r < len(inventory_act) and r > 0:
                        break
                except:
                    input('input invalido, aperte enter para tentar novamente...')
            if inventory_act[r].qnt > 1:
                inventory_act[r].useItem()
            else:
                input('não há recursos suficientes, pressione enter para continuar...')
            return 0

def seaMenu(sea):
    for i in range(len(sea)):
        if sea[i].explored:
            print(f'[{i}]|{sea[i].name} | dif:{sea[i].dif} | %succ: {sea[i].succ}')
        else:
            print(f'[{i}]|{sea[i].name}')
        
        try:
            r = int(input('>>>'))
            if r < len(sea) and r > 0:
                    break
        except:
            input('input invalido, aperte enter para tentar novamente...')

        print(f'{sea[r].name}')
        os.system('cls')
        print('1 -- Atacar // 2 -- Explorar // 3 -- Cancelar')
        try:
            s = int(input('>>>'))
            if s < 4 and s > 0:
                break
        except:
            input('input invalido, aperte enter para tentar novamente...')
        match s:
            case 1:
                for i in range(unoccupied_pirates):
                    print(f'{i} ||{unoccupied_pirates[i].name}')
                    print('selecione um grupo pirata')
                try:
                    p = int(input('>>>'))
                    if p < len(unoccupied_pirates) and p > 0:
                            break
                except:
                        input('input invalido, aperte enter para tentar novamente...')
                
                sea[r].raid(unoccupied_pirates[p])
            case 2:
                for i in range(unoccupied_pirates):
                    print(f'{i} ||{unoccupied_pirates[i].name}')
                    print('selecione um grupo pirata')
                    try:
                        p = int(input('>>>'))
                        if p < len(unoccupied_pirates) and p > 0:
                                break
                    except:
                            input('input invalido, aperte enter para tentar novamente...')
                sea[r].explore(unoccupied_pirates[p])
            case 3:
                return 0
        



def menu(d,boat):
    while True:
        os.system('cls')
        print(f"-------[{d}]--------")
        print(f'papagaio diz:{random.choice(paraguaio)}')
        boat.showStatus()
        print('---------------------')
        print('ações:\n1 -> ver recursos\n2 -> ver mapa\n 3 -> ver piratas\n 4 -> passar o dia')

        try:
            r = int(input('>>>'))
            if r < 5 and r > 0:
                break
        except:
            input('input invalido, aperte enter para tentar novamente...')
        
    match r:
        case 1:
            os.system('cls')
            seaMenu(sea)
# endregion
