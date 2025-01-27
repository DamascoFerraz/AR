import os, random

# region boat
class Boat:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.eff = 'normal'
        self.gold = 100
        self.rep = 50

    def show_status(self):
        return f'\n|[Status de {self.name}]:\n| - HP:[{self.hp}/100]\n| - eff: {self.eff}\n| - ouro: {self.gold}\n| - reputação:{self.rep}\n'

# endregion boat

# region item
class Item:
    def __init__(self, name, qnt=0, val=1):
        self.name = name
        self.qnt = qnt
        self.val = val
    
    def change_qnt(self, x):
        if self.qnt >= x:
            self.qnt += x
            return 1
        else:
            return 0
# region >>Item_use
class PassItem(Item):
    def __init__(self, name, qnt=0, val=1):
        super().__init__(name, qnt, val)

class ActiveItem(Item):
    def __init__(self, name, eff='none', qnt=0, val=1):
        super().__init__(name, qnt, val)
        self.eff = eff
# endregion >>Item_use
# endregion item

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
    "Reis do Mar"
]

class Pirate:
    def __init__(self, name=random.choice(pirate_names), hp=100, adj='null', status='normal', occupied=False):
        self.name = name
        self.hp = hp
        self.adj = adj
        self.status = status
        self.occupied = occupied
# endregion pirate

# region island
island_names = [
    'guaxupé', 'muzambinho', "Ilha da Caveira", "Ilha Perdida", "Ilha do Tesouro", "Ilha Tortuga",
    "Ilha dos Esqueletos", "Ilha Misteriosa", "Ilha do Diabo", "Ilha das Sombras", "Ilha das Sereias", "Ilha dos Canibais"
]
island_effects = [
    ['tired', 'hungry', 'weak'],
    ['tired', 'weak', 'hungry', 'hurt', 'poisoned', 'bleeding'],
    ['tired', 'weak', 'hungry', 'hurt', 'poisoned', 'bleeding', 'crippled', 'burnt', 'mad', 'traitor']
]

class Island:
    def __init__(self, dif='medium', explored=False):
        self.name = random.choice(island_names)
        self.explored = explored
        self.raided = False

        if dif == 'easy':
            self._dif = dif
            self.loot = random.randint(10, 50)
            self.death = random.randint(1, 5)
            self.caract = random.choice(['beach', 'forest', 'merchant', 'village'])
            self._eff = random.choice(island_effects[1]) if random.randint(1, 5) == 1 else 'normal'

        elif dif == 'medium':
            self._dif = dif
            self.loot = random.randint(50, 100)
            self.death = random.randint(5, 10)
            self.caract = random.choice(['beach', 'forest', 'merchant', 'village'])
            self._eff = random.choice(island_effects[2]) if random.randint(1, 4) == 1 else 'normal'

        elif dif == 'hard':
            self._dif = dif
            self.loot = random.randint(100, 200)
            self.death = random.randint(10, 20)
            self.caract = random.choice(['beach', 'forest', 'merchant', 'village'])
            self._eff = random.choice(island_effects[2]) if random.randint(1, 3) == 1 else 'normal'

    def explore(self, pirate):
        if pirate:
            self.explored = True
# region >>Outpost
class Outpost(Island):
    def __init__(self, lv=1, raided=False):
        super().__init__('very hard', explored=True)
        self.lv = lv
        self.raided = raided

        match lv:
            case 1:
                self.name = 'crakudas'
                self._dif = 'very hard'
                self.loot = 200
                self.death = 35
                self.caract = 'rocky'
                self._eff = 'hurt'
                
            case 2:
                self.name = 'kudomagu'
                self._dif = 'very hard'
                self.loot = 220
                self.death = 45
                self.caract = 'jungle'
                self._eff = 'poisoned'
            
            case 3:
                self.name = 'kúdaokada'
                self._dif = 'very hard'
                self.loot = 220
                self.death = 45
                self.caract = 'lava'
                self._eff = 'burnt'

            case 4:
                self.name = 'Áuladujansley'
                self._dif = 'very hard'
                self.loot = 220
                self.death = 45
                self.caract = 'cult'
                self._eff = 'mad'
            
            case 5:
                self.name = 'Capital'
                self._dif = 'very hard'
                self.loot = 999
                self.death = 90
                self.caract = 'cult'
                self._eff = 'mad'
# endregion >>Outpost
# endregion island

#region use_vars

actions_messages = []
pirates = [Pirate()]
anti_attack = 0
lvl = 1

inventory_passive = [
    PassItem('food', 5, 5),
    PassItem('water', 5, 1),
    PassItem('wood', 3, 10),
    PassItem('cannonball', 5, 50)
]
inventory_active = [
    ActiveItem('strength_potion', 'strength_potion', 0, 100),
    ActiveItem('armor', 'armor', 0, 200),
    ActiveItem('weaponry', 'weaponry', 0, 300)
]
sea = [
    Island('easy'),
    Island('easy'),
    Island('easy'),
    Outpost(lvl)
]

# region >>miscelaneous vars

parrot_phrases = [
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

# endregion >>miscelaneous vars
# endregion use_vars

# region actions
effects_percentage = {
    'tired': 0.8,
    'hungry': 0.8,
    'weak': 0.7,
    'hurt': 0.5,
    'poisoned': 0.5,
    'bleeding': 0.5,
    'crippled': 0.1,
    'burnt': 0.5,
    'mad': 0.2,
    'traitor': 0.0
}
itens_percentage = {
    'strength_potion': 2,
    'armor': 1.3,
    'weaponry': 1.5,
}
    
def calculate_success_rate(pirate, island):
    base_rate = 100 - island.death
    health_modifier = pirate.hp / 100
    effect_modifier = 1.0  # Default modifier for 'normal' effect
    if pirate.status != 'normal':
        effect_modifier = effects_percentage[pirate.status]
    
    item_modifier = 1.0
    for item in inventory_active:
        if item.eff != 'none':
            item_modifier *= itens_percentage[item.eff]

    success_rate = base_rate * health_modifier * effect_modifier * item_modifier
    return success_rate

def raid(pirate, island, boat):
    success_rate = calculate_success_rate(pirate, island)
    success_roll = random.randint(1, 100)
    if success_roll <= success_rate:
        if pirate.status == 'none':
            pirate.status = island._eff
        boat.gold += island.loot  # Add loot to the boat's gold
        if isinstance(island, Outpost): # ARRUMAR ISSO AQUI
            island.raided = True
            
        else:
            sea.remove(island)
        actions_messages.append(f'{pirate.name} invadiu {island.name} com sucesso!')
    else:
        pirate.hp -= 50  # Pirate dies if the raid fails
        pirate.status = island._eff
        actions_messages.append(f'{pirate.name} machucou-se tentando invadir {island.name}!')

item_per_random = {
    1: 'food',
    2: 'water',
    3: 'wood',
    4: 'cannonball'
}
def collect_resource(pirate):
    random = random.randint(1, 4)
    for item in inventory_passive:
        if item.name == item_per_random[random]:
            item.qnt += random.randint(1, 3)
    actions_messages.append(f'{pirate.name} coletou {item_per_random[random]}')
    pirate.occupied = False


def fish(pirate):
    random = random.randint(1, 5)
    for item in inventory_passive:
        if item.name == 'food':
            item.qnt += random
    actions_messages.append(f'{pirate.name} pescou {random} peixes')
    pirate.occupied = False

def watch(pirate):
    actions_messages.append(f'{pirate.name} vigiou o barco')
    anti_attack = random.randint(5,15)
    pirate.occupied = False

# region >>actions_add
daily_actions = []

def add_action(action):
    daily_actions.append(action)

def execute_actions():
    for action in daily_actions:
        action()
    daily_actions.clear()

def add_raid_action(pirate, island, boat):
    def action():
        raid(pirate, island, boat)
    add_action(action)

def add_explore_action(pirate, island):
    def action():
        island.explore(pirate)
    add_action(action)

def add_collect_resource_action(pirate):
    def action():
        collect_resource(pirate)
    add_action(action)

def add_fish_action(pirate):
    def action():
        fish(pirate)
    add_action(action)

def add_watch_action(pirate):
    def action():
        watch(pirate)
    add_action(action)

# endregion >>actions_add
# endregion actions

# region functionalities
def pass_day(boat,d, lvl):
    global pirates, unoccupied_pirates
    attack_chance = random.randint(1, 100)

    inventory_passive[0].qnt -= len(pirates)  # Consume food
    inventory_passive[1].qnt -= len(pirates)  # Consume water
    inventory_passive[3].qnt -= len(pirates)  # Consume cannonballs
    
    if inventory_passive[0].qnt < 0:
        boat.hp -= random.randint(10, 20)
        boat.rep -= random.randint(5, 20)
        for pirate in pirates:
            pirate.hp -= random.randint(10, 30)
            pirate.status = 'hungry'
            if random.randint(1, 5) == 1:
                pirate.status = 'mad'
            if random.randint(1, 10) == 1:
                pirate.status = 'traitor'
        actions_messages.append("Fome a bordo!")
    if inventory_passive[1].qnt < 0:
        boat.hp -= random.randint(10, 20)
        boat.rep -= random.randint(5, 20)
        for pirate in pirates:
            pirate.hp -= random.randint(10, 30)
            if random.randint(1, 5) == 1:
                pirate.status = 'mad'
            if random.randint(1, 10) == 1:
                pirate.status = 'traitor'
        actions_messages.append("Sede a bordo!")
    

    if attack_chance >= 50 + anti_attack + (inventory_passive[3].qnt)*10:  # 50% chance of pirate attack
        actions_messages.append("Ataque de piratas!")
        boat.hp -= random.randint(10, 50)
        boat.rep -= random.randint(5, 20)
        boat.gold -= random.randint(10, 50)
        for pirate in pirates:
            pirate.hp -= random.randint(10, 50)
    else:
        actions_messages.append("Dia tranquilo...")
    
    execute_actions()
    # Update unoccupied pirates list
    unoccupied_pirates = [pirate for pirate in pirates if not pirate.occupied and pirate.hp]
    # making all pirates unoccupied
    for pirate in pirates:
        pirate.occupied = False

    # Check if the outpost was explored
    dif_per_lvl = {
        1: 'easy',
        2: 'medium',
        3: 'hard',
    }
    if sea[len(sea)-1].explored:
        sea.clear()
        match lvl:
            case 1:
                sea.append(Island(dif_per_lvl[random.randint(1,2)]))
                sea.append(Island(dif_per_lvl[random.randint(1,2)]))
                sea.append(Island(dif_per_lvl[random.randint(1,2)]))
            case 2:
                sea.append(Island('medium'))
                sea.append(Island('medium'))
                sea.append(Island('medium'))
            case 3:
                sea.append(Island(dif_per_lvl[random.randint(2,3)]))
                sea.append(Island(dif_per_lvl[random.randint(2,3)]))
                sea.append(Island(dif_per_lvl[random.randint(2,3)]))
            case 4:
                sea.append(Island('hard'))
                sea.append(Island('hard'))
                sea.append(Island('hard'))
        sea.append(Outpost(lvl))
        lvl += 1
    if lvl == 5:
        os.system('cls')
        print(f'Você venceu o jogo! em {d} dias')
        input('Aperte enter para sair...')

    return
# endregion functionalities

# region menu
def resources_menu(inventory_passive, inventory_active):
    while True:
        os.system('cls')
        print(f'|- nome | qnt | val uni')

        for item in inventory_passive:
            print(f'|- {item.name}| {item.qnt} | {item.val}')

        for item in inventory_active:
            print(f'|- {item.name}| {item.qnt} | {item.val}')
        
        print('---------------------')
        print('ações:\n1 -> usar recurso\n2 -> cancelar')

        try:
            r = int(input('>>>'))
            if 0 < r < 3:
                break
        except:
            input('input invalido, aperte enter para tentar novamente...')
        
    match r:
        case 2:
            return 0
        case 1:
            while True:
                for i, item in enumerate(inventory_active):
                    print(f'|[{i}]| {item.name}| {item.qnt} | {item.val}')
            
                try:
                    r = int(input('>>>'))
                    if 0 <= r < len(inventory_active):
                        break
                except:
                    input('input invalido, aperte enter para tentar novamente...')
            if inventory_active[r].qnt > 0:
                inventory_active[r].use_item()
            else:
                input('não há recursos suficientes, pressione enter para continuar...')
            return 0

def sea_menu(sea, boat):
    while True:
        os.system('cls')

        for i, island in enumerate(sea):
            if island.explored == True:
                print(f'[{i}]|{island.name} | dif:{island._dif} | %succ: {100 - island.death}')
            else:
                print(f'[{i}]|{island.name} | dif:{island._dif} | %succ: ???')
        
        try:
            r = int(input('>>>'))
            if 0 <= r < len(sea):
                break
        except:
            input('input invalido, aperte enter para tentar novamente...')

    os.system('cls')
    print(f'{sea[r].name}')
    print('1 -- Atacar // 2 -- Explorar // 3 -- Cancelar')
    try:
        s = int(input('>>>'))
        if 0 < s < 4:
            unoccupied_pirates = [pirate for pirate in pirates if not pirate.occupied and pirate.hp]
            match s:
                case 1:
                    for i, pirate in enumerate(unoccupied_pirates):
                        print(f'{i} ||{pirate.name}')
                    print('selecione um grupo pirata')
                    try:
                        p = int(input('>>>'))
                        if 0 <= p < len(unoccupied_pirates):
                            add_raid_action(unoccupied_pirates[p], sea[r], boat)
                            unoccupied_pirates[p].occupied = True
                            
                    except:
                        input('input invalido, aperte enter para tentar novamente...')
                case 2:
                    for i, pirate in enumerate(unoccupied_pirates):
                        print(f'{i} ||{pirate.name}')
                    print('selecione um grupo pirata')
                    try:
                        p = int(input('>>>'))
                        if 0 <= p < len(unoccupied_pirates):
                            add_explore_action(unoccupied_pirates[p], sea[r])
                            unoccupied_pirates[p].occupied = True
                            
                    except:
                        input('input invalido, aperte enter para tentar novamente...')
                case 3:
                    return 0
    except:
        input('input invalido, aperte enter para tentar novamente...')

def assign_task(pirate):
    while True:
        os.system('cls')
        print(f'Selecionado: {pirate.name}')
        print('Tarefas disponíveis:')
        print('1 -> Coletar recurso')
        print('2 -> Pescar')
        print('3 -> Vigiar')
        print('4 -> Cancelar')

        try:
            t = int(input('>>>'))
            if 0 < t < 5:
                break
        except:
            input('input invalido, aperte enter para tentar novamente...')
        
    match t:
        case 1:
            add_collect_resource_action(pirate)
        case 2:
            add_fish_action(pirate)
        case 3:
            add_watch_action(pirate)
        case 4:
            return 0



def pirates_menu(pirates):
    while True:
        os.system('cls')
        print(f'|- nome | hp | status | ocupado')

        for i, pirate in enumerate(pirates):
            print(f'|- {pirate.name} | {pirate.hp} | {pirate.status} | {pirate.occupied}')
        
        print('---------------------')
        print('ações:\n1 -> selecionar pirata\n2 -> cancelar')

        try:
            r = int(input('>>>'))
            if 0 < r < 3:
                break
        except:
            input('input invalido, aperte enter para tentar novamente...')
        
    match r:
        case 2:
            return 0
        case 1:
            while True:
                for i, pirate in enumerate(pirates):
                    print(f'|[{i}]| {pirate.name}| {pirate.hp} | {pirate.status} | {pirate.occupied}')
            
                try:
                    r = int(input('>>>'))
                    if 0 <= r < len(pirates):
                        break
                except:
                    input('input invalido, aperte enter para tentar novamente...')
            selected_pirate = pirates[r]
            assign_task(selected_pirate)
            return 0

def shop_menu(inventory_passive, inventory_active, pirates):
    while True:
        os.system('cls')
        print('Loja:')
        print('1 -> Comprar itens passivos')
        print('2 -> Comprar itens ativos')
        print('3 -> Comprar piratas')
        print('4 -> Cancelar')

        try:
            r = int(input('>>>'))
            if 0 < r < 5:
                break
        except:
            input('input invalido, aperte enter para tentar novamente...')
        
    match r:
        case 1:
            # Comprar itens passivos
            pass
        case 2:
            # Comprar itens ativos
            pass
        case 3:
            # Comprar piratas
            pass
        case 4:
            return 0

def menu(d, boat,lvl):
    if boat.hp <= 0:
        os.system('cls')
        print('Seu barco afundou, você perdeu!')
        input('Aperte enter para sair...')
        exit()
    while True:
        os.system('cls')
        attack_chance = 50  # 50% chance of pirate attack
        print(f"-------[dia:{d}]--------")
        print(f'papagaio diz:{random.choice(parrot_phrases)}')
        print(f'--------[lvl:{lvl}]---------')
        for message in actions_messages:
            print(f">{message}")
        actions_messages.clear()
        print('---------------------')
        print(boat.show_status())
        print(f'Chance de ataque pirata: {attack_chance - anti_attack - (inventory_passive[3].qnt)*10}%')
        print('---------------------')
        print('ações:\n1 -> ver recursos\n2 -> ver mapa\n3 -> ver piratas\n4 -> passar o dia\n5 -> visitar loja')

        try:
            r = int(input('>>>'))
            if 0 < r < 6:
                break
        except:
            input('input invalido, aperte enter para tentar novamente...')
        
    match r:
        case 1:
            os.system('cls')
            resources_menu(inventory_passive, inventory_active)
            return d
        case 2:
            os.system('cls')
            sea_menu(sea, boat)
            return d
        case 3:
            os.system('cls')
            pirates_menu(pirates)
            return d
        case 4:
            
            pass_day(boat,d,lvl)
            d+=1
            return d
        case 5:
            os.system('cls')
            shop_menu(inventory_passive, inventory_active, pirates)
            return d

def main():
    d = 1
    os.system('cls')
    boat_name = input("Digite o nome do seu barco: ")
    my_boat = Boat(boat_name)
    while True:
        d = menu(d, my_boat,lvl)

if __name__ == "__main__":
    main()
# endregion menu
