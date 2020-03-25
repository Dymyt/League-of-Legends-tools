#Este programa extrae de la carpeta de la base de datos en json (javascript), datos de los personajes.

#Hace falta llamar a la clase para crear objetos y llamar a funciones
#Glob sirve para leer todos los archivos de un directorio y devolver una lista
import glob
from Intgrafica import campeonClase as c

#Devuelve lista de todos los documentos dentro de la carpeta, cambiar a donde este la carpeta
listaDocumentos = glob.glob(r'D:\Archivos lol 10.6.1\10.6.1\data\es_ES\champion\*.json')

#*********CONSEGUIR NOMBRES*************
nombrePersonajes = []
for directorio in listaDocumentos:
    #el enconding para que pueda leer caracteres especiales
    f = open(directorio, encoding="utf8")
    #Hay que leer la línea para convertirlo en un string
    campeonString = f.readline()
    #Localizar donde está el name. Sumarle 7 para llegar a primera letra de nombre de campeon.
    #Split por " para coger el primer objeto, que es el nombre justo cuando llegue a ".
    indexName = campeonString.find("name")
    nombrePersonajes.append(campeonString[indexName+7:].split('"')[0])
    f.close()

#*********CREAR LISTA DE OBJETOS CAMPEON**************
#Creamos lista de objetos CAMPEON, e iniciamos cada uno con el nombre del personaje en cuestión
listaCampeonesObjeto = [c.campeon(nombre=n) for n in nombrePersonajes]


#*******AÑADIR ATRIBUTOs IMAGEN, HP, SP, MOVESPEED, ARMOR...**************
#La ruta donde deben estar las imagenes para que luego tkinter acceda
rutaImagenes = r'C:\LolTool\championImages'
listaRutaImagenes = []
listaHP = []
listaHPPerLevel = []
listaSP = []
listaSPPerLevel= []
listaMoveSpeed = []
listaArmor = []
listaArmorperLevel = []
listaMagicResist = []
listaMagicResistPerLevel = []
listaAttackRange = []
listaHPRegen = []
listaHPRegenPerLevel = []
listaSPRegen = []
listaSPRegenPerLevel = []
listaAttack = []
listaAttackPerLevel = []
listaAttackSpeed = []
listaAttackSpeedPerLevel = []
for directorio in listaDocumentos:
    f = open(directorio, encoding="utf8")
    campeonString = f.readline()
    indexImgFull = campeonString.find("full")
    imagenAnadir = rutaImagenes
    imagenAnadir = imagenAnadir + "\\" + str(campeonString[indexImgFull+7:].split('"')[0])
    listaRutaImagenes.append(imagenAnadir)

    #Cortar el string en stats
    #Hp inicio
    indexStats = campeonString.find("stats")
    campeonString = campeonString[indexStats:]
    indexHP = campeonString.find("hp")
    listaHP.append(campeonString[indexHP+4:].split(",")[0])
    #Hp por level
    indexHPPerLevel = campeonString.find("hpperlevel")
    listaHPPerLevel.append(campeonString[indexHPPerLevel+12:].split(",")[0])
    #Sp Inicio
    indexSP = campeonString.find("mp")
    listaSP.append(campeonString[indexSP+4:].split(",")[0])
    #Sp por Level
    indexSPPerLevel = campeonString.find("mpperlevel")
    listaSPPerLevel.append(campeonString[indexSPPerLevel+12:].split(",")[0])
    #Move Speed
    indexMoveSpeed = campeonString.find("movespeed")
    listaMoveSpeed.append(campeonString[indexMoveSpeed+11:].split(",")[0])
    #Armor
    indexArmor = campeonString.find("armor")
    listaArmor.append(campeonString[indexArmor+7:].split(",")[0])
    #Armor por Level
    indexArmorperLevel = campeonString.find("armorperlevel")
    listaArmorperLevel.append(campeonString[indexArmorperLevel+15:].split(",")[0])
    #Magic Resist
    indexMagicResist = campeonString.find("spellblock")
    listaMagicResist.append(campeonString[indexMagicResist+12:].split(",")[0])
    #Magic Resist por Level
    indexMagicResistPerLevel = campeonString.find("spellblockperlevel")
    listaMagicResistPerLevel.append(campeonString[indexMagicResistPerLevel+20:].split(",")[0])
    #Attack Range
    indexAttackRange = campeonString.find("attackrange")
    listaAttackRange.append(campeonString[indexAttackRange+13:].split(",")[0])
    #HP Regen
    indexHPRegen = campeonString.find("hpregen")
    listaHPRegen.append(campeonString[indexHPRegen+9:].split(",")[0])
    #HP Regen per Level
    indexHPRegenPerLevel = campeonString.find("hpregenperlevel")
    listaHPRegenPerLevel.append(campeonString[indexHPRegenPerLevel+17:].split(",")[0])
    #SP Regen
    indexSPRegen = campeonString.find("mpregen")
    listaSPRegen.append(campeonString[indexSPRegen+9:].split(",")[0])
    #SP Regen per Level
    indexSPRegenPerLevel = campeonString.find("mpregenperlevel")
    listaSPRegenPerLevel.append(campeonString[indexSPRegenPerLevel+17:].split(",")[0])
    #Attack
    indexAttack = campeonString.find("attackdamage")
    listaAttack.append(campeonString[indexAttack+14:].split(",")[0])
    #Attack per Level
    indexAttackPerLevel = campeonString.find("attackdamageperlevel")
    listaAttackPerLevel.append(campeonString[indexAttackPerLevel+22:].split(",")[0])
    #Attack Speed
    indexAttackSpeed = campeonString.find(r'"attackspeed"')
    listaAttackSpeed.append(campeonString[indexAttackSpeed+14:].split("}")[0])
    #Attack Speed per Level
    indexAttackSpeedPerLevel = campeonString.find("attackspeedperlevel")
    listaAttackSpeedPerLevel.append(campeonString[indexAttackSpeedPerLevel+21:].split(",")[0])
    f.close()

#Iniciamos los atributos de los campeones, la variable i es para asignar los elementos de las listas
i = 0
for campeon in listaCampeonesObjeto:
    campeon.imagen = listaRutaImagenes[i]
    campeon.hp = [float(listaHP[i]), float(listaHPPerLevel[i])]
    campeon.sp = [float(listaSP[i]), float(listaSPPerLevel[i])]
    campeon.movespeed = int(listaMoveSpeed[i])
    campeon.armor = [float(listaArmor[i]), float(listaArmorperLevel[i])]
    campeon.rmagic = [float(listaMagicResist[i]), float(listaMagicResistPerLevel[i])]
    campeon.attackrange = float(listaAttackRange[i])
    campeon.hpregen = [float(listaHPRegen[i]), float(listaHPRegenPerLevel[i])]
    campeon.spregen = [float(listaSPRegen[i]), float(listaSPRegenPerLevel[i])]
    campeon.attack = [float(listaAttack[i]), float(listaAttackPerLevel[i])]
    campeon.attackspeed = [float(listaAttackSpeed[i]), float(listaAttackSpeedPerLevel[i])]
    i = i +1

#Imprimir objetos para comprobación
for campeon in listaCampeonesObjeto:
    print (campeon.nombre +  " HP:" + str(campeon.hp) + " SP:" + str(campeon.sp) + " MS:" + str(campeon.movespeed) + " Armor:" + str(campeon.armor)
           + " Res. Mag:" + str(campeon.rmagic) + " A. Range:" + str(campeon.attackrange) + " HP.Regen:" + str(campeon.hpregen) + " SP.Regen:"
           + str(campeon.spregen) + " Attack:" + str(campeon.attack) + " A.Speed:" +str(campeon.attackspeed) + " Dir:" + campeon.imagen)

#Crear documento de consejos, escribir a partir del *. FALTA CREAR una funcion que lea el documento y asigne a los objetos los consejos en caso
f = open("Consejos.txt", "r")




