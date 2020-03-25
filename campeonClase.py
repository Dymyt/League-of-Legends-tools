#Ponemos todito igual a none, por si no le asignamos nada
#HpRegen y SpRegen es cada 5 segundos. Attackpeed por level es un % que de multimiplica al attack speed actual
class campeon:
    def __init__(self, nombre = None, imagen = None, hp = None, sp = None, movespeed = None, rmagic = None, armor = None, attackrange = None,
                 hpregen = None, spregen = None, attack = None, attackspeed = None, powerspike= None, consejo= None):
        self.nombre = nombre
        self.imagen = imagen
        self.hp = hp
        self.sp = sp
        self.movespeed = movespeed
        self.rmagic = rmagic
        self.armor = armor
        self.attackrange = attackrange
        self.hpregen = hpregen
        self.spregen = spregen
        self.attack = attack
        self.attackspeed =attackspeed
        self.powerspike = powerspike
        self.consejo = consejo

    def infoCampeon(self):
        return self.nombre + " HP: " + str(self.hp) + " SP: " + str(self.sp)