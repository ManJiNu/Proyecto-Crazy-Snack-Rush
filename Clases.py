#Clase Ingrediente(Padre)
class Ingrediente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estado = "crudo"
    def preparar(self):
        self.estado = "preparado" 
    def __repr__(self): ###
        return f"Ingrediente({self.nombre})"
        
#Subclase de Frutas y Vegetales, hija de de la clase ingrediente
class FrutasYVegetales(Ingrediente):
    pass

#Subclase de Proteínas, hija de de la clase ingrediente
class Proteina(Ingrediente):
    pass

#Subclase de Panes, hija de de la clase ingrediente
class Panes(Ingrediente):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.estado = "preparado"

#Subclase de Papas, hija de de la clase ingrediente
class Papa(Ingrediente):
    def __init__(self):
        super().__init__("Papa")

#Clase Receta
class Receta:
    def __init__(self, nombre, lista_ingredientes):
        self.nombre = nombre
        self.lista_ingredientes = lista_ingredientes
        self.puntuaje = 10 * len(lista_ingredientes)
        self.tiempo = 15 * len(lista_ingredientes)
    def __repr__(self): ###
        return f"Receta({self.nombre})"


#Clase Estacion
class Estacion:
    def __init__(self, x, y ):
        self.pos_x = x
        self.pos_y = y
        self.pos_ocupado = False
        self.ingrediente = None

#Subclase Despensa, hija de la clase Estación
class Despensa(Estacion):
    def __init__(self, x, y, ingrediente_tipo):
        super().__init__(x,y)
        self.ingrediente_tipo = ingrediente_tipo

#Subclase Tabla de picar, hija de la clase Estación
class TablaDePicar(Estacion):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.tiempo = 2

#Subclase Sarten, hija de la clase Estación
class Sarten(Estacion):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.tiempo = 4

#Subclase Freidora, hija de la clase Estación
class Freidora(Estacion):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.tiempo = 5

#Subclase Enrega, hija de la clase Estación
class Entrega(Estacion):
    pass


#Clase Chef
class Chef:
    def __init__(self, x,y, velocidad):
        self.posicion_x = x
        self.posicion_y = y
        self.ingrediente_a_mano = None
        self.velocidad = velocidad 
    def mover_arriba(self):
        self.posicion_y -= self.velocidad
    def mover_abajo(self):
        self.posicion_y += self.velocidad
    def mover_derecha(self):
        self.posicion_x += self.velocidad
    def mover_izquierda(self):
        self.posicion_x -= self.velocidad
    def recoger_ingrediente(self, ingrediente):
        self.ingrediente_a_mano = ingrediente
    def soltar_ingrediente(self):
        self.ingrediente_a_mano = None


#Clase Cocina
class Cocina:
    def __init__(self):
        self.lista_estaciones_mapa = []
        self.lista_chefs = []
        self.recetas_activas = []
        self.puntuaje = 0
        self.tiempo = 0
    def agregar_estacion(self, estacion):
        self.lista_estaciones_mapa.append(estacion)
    def agregar_chef(self, chef):
        self.lista_chefs.append(chef)
    def agregar_receta(self, receta):
        self.recetas_activas.append(receta)
    def entregar_receta(self, receta):
        self.recetas_activas.remove(receta)
        self.puntuaje += receta.puntuaje 
        

tomate = FrutasYVegetales("Tomate")
carne = Proteina("Carne")
pan = Panes("Pan")

hamburguesa = Receta("Hamburguesa", [tomate, carne, pan])

cocina = Cocina()
cocina.agregar_receta(hamburguesa)
print(cocina.recetas_activas)

cocina.entregar_receta(hamburguesa)
print(cocina.recetas_activas)
print(cocina.puntuaje)
print(tomate)  