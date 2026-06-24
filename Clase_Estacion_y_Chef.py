from Clase_Ingredientes_y_receta import Ingredientes, FrutasyVegetales, Proteina, Panes, Papa
from Clase_Ingredientes_y_receta import Receta

# CLASS ESTACION
# Clase base que representa una estación de trabajo en la cocina
class Estacion:
    def __init__(self, nombre, posicion_x, posicion_y):
        # Nombre de la estación
        self.nombre = nombre
        # Posición de la estación en el mapa
        self.posicion_x = posicion_x
        self.posicion_y = posicion_y
        # Indica si la estación está ocupada
        self.ocupado = False
        # Ingrediente que está encima de la estación
        self.ingrediente_encima = None
        # Lista de ingredientes que acepta la estación
        self.ingredientes_aceptados = []
    def generarReceta(self):
        # Método base, cada subclase lo sobreescribe
        pass

    def procesarIngredientes(self, ingrediente): #Aqui hago un metodo para procesar y modificar los igredientes 
        pass
# Subclase que provee ingredientes ilimitados de un tipo específico
class Despensa(Estacion):
    def __init__(self, posicion_x, posicion_y, ingrediente_tipo):
        super().__init__("Despensa", posicion_x, posicion_y)
        # Tipo de ingrediente que provee esta despensa
        self.ingrediente_tipo = ingrediente_tipo

# Subclase para cortar vegetales y frutas
class TablaDePicar(Estacion):
    def __init__(self, posicion_x, posicion_y):
        super().__init__("Tabla de Picar", posicion_x, posicion_y)
        # Tiempo en segundos para procesar el ingrediente
        self.tiempo = 2
    def generarReceta(self):
        # Genera una receta predefinida con vegetales para la tabla de picar
        tomate = FrutasyVegetales("Tomate", "picado")
        lechuga = FrutasyVegetales("Lechuga", "picado")
        return Receta("Ensalada", [tomate, lechuga])
    def procesarIngredientes(self, ingrediente): #Basicamente lo que hice aqui fue cambiar a que el ingrediente fue picado
        ingrediente.preparar()
        print (
            f"{ingrediente.nombre} fue picado" #Me indica al usuario que fue picado
        )
        return ingrediente 

# Subclase para cocinar proteínas
class Sarten(Estacion):
    def __init__(self, posicion_x, posicion_y):
        super().__init__("Sarten", posicion_x, posicion_y)
        # Tiempo en segundos para procesar el ingrediente
        self.tiempo = 4
    def generarReceta(self):
        # Genera una receta predefinida con proteína para el sartén
        carne = Proteina("Carne", "cocinado")
        pan = Panes("Pan")
        return Receta("Hamburguesa", [carne, pan])
    
    def procesarIngredientes(self, ingrediente):
        ingrediente.preparar()

        print(f"{ingrediente.nombre} fue cocinado")

        return ingrediente
class MesaNormal:
    def __init__(self, posicion_x, posicion_y): #Para poner la comida en el plato
        self.nombre = "Mesa"
        self.posicion_x = posicion_x
        self.posicion_y = posicion_y
        self.objeto_encima = None        

# Subclase para freír papas
class Freidora(Estacion):
    def __init__(self, posicion_x, posicion_y):
        super().__init__("Freidora", posicion_x, posicion_y)
        # Tiempo en segundos para procesar el ingrediente
        self.tiempo = 5
    def generarReceta(self):
        # Genera una receta predefinida con papas fritas
        papa = Papa()
        papa.estado = "frito"
        return Receta("Papas Fritas", [papa])
    def procesarIngredientes(self, ingrediente):
        ingrediente.preparar()
        print(
            f"{ingrediente.nombre} fue frito" #Me indica que modifique tal comida al freir
        )
        return ingrediente

# Subclase donde se entregan las recetas completadas
class Entrega(Estacion):
    def __init__(self, posicion_x, posicion_y):
        super().__init__("Entrega", posicion_x, posicion_y)





#CLASS CHEF
# Clase base que representa al personaje controlado por el jugador en la cocina.
class Chef:
    def __init__(self, nombre, posicion_x, posicion_y, velocidad=0, ingrediente_a_mano=None):
        # Inicializa el chef con los atributos: nombre, puntos, posición, velocidad e ingrediente en mano
        self.nombre = nombre
        self.puntos = 0
        self.posicion_x = posicion_x
        self.posicion_y = posicion_y
        self.velocidad = velocidad
        self.ingrediente_a_mano = ingrediente_a_mano

    # Metodos de la clase Chef
    def mover_arriba(self):
        # Mueve el chef hacia arriba restando la velocidad a la posición Y
        self.posicion_y -= self.velocidad

    def mover_abajo(self):
        # Mueve el chef hacia abajo sumando la velocidad a la posición Y
        self.posicion_y += self.velocidad

    def mover_derecha(self):
        # Mueve el chef hacia la derecha sumando la velocidad a la posición X
        self.posicion_x += self.velocidad

    def mover_izquierda(self):
        # Mueve el chef hacia la izquierda restando la velocidad a la posición X
        self.posicion_x -= self.velocidad

    def recoger_ingrediente(self, ingrediente):
        # Recoge un ingrediente y lo guarda en la mano del chef
        self.ingrediente_a_mano = ingrediente

    def soltar_ingrediente(self):
        # Suelta el ingrediente que el chef tiene en mano
        self.ingrediente_a_mano = None
    
#tabla = TablaDePicar(100, 200)
#print(tabla.nombre)
#print(tabla.generarReceta())

#chef = Chef("Manfred", 100, 200, velocidad=5)
#print(chef.nombre)
#print(chef.puntos)