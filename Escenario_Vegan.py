import random
from Clase_Ingredientes_y_receta import(Receta, FrutasyVegetales, Panes, Papa)
from Clase_Estacion_y_Chef import(Estacion,Despensa,TablaDePicar,Freidora, Entrega, MesaNormal)


#Recetas escenario vegan
def EnsaladaFresca():
    '''Ensalada fresca: Tomate picado y lechuga picada'''
    return Receta("Ensalada Fresca", [FrutasyVegetales("Tomate", "picado"), FrutasyVegetales("Lechuga", "picado")])

def WrapVegano():
    '''Wrap vegano: Tortilla, tomate picado, aguacate picado '''
    return Receta("Wrap Vegano", [Panes("Tortilla"), FrutasyVegetales("Tomate", "picado"), FrutasyVegetales("Aguacate", "picado")])
def papaBowl():
    papa = Papa()
    papa.estado = "frito"
    '''Papa bowl: Papa frtia, tomate, lechuga, aguacate'''
    return Receta("Papa Bowl", [papa,FrutasyVegetales("Tomate", "picado"), FrutasyVegetales("Lechuga", "picado"), FrutasyVegetales("Aguacate", "picado")])

def BowlFrutas():
    '''Bowl de frutas: Mango, fresa y banano'''
    return Receta("Bowl de frutras", [   FrutasyVegetales("Mango",   "picado"),FrutasyVegetales("Fresa",   "picado"), FrutasyVegetales("Platano", "picado")])

#Listas de funciones generadoras (cada llamada crea una receta nueva)
RECETAS_VEGAN = [
    EnsaladaFresca,
    WrapVegano,
    papaBowl,
    BowlFrutas
]

#Despensa Escenario Vegan
DESPENSA_VEGAN= [
 (FrutasyVegetales("Tomate"),   480, 100),
    (FrutasyVegetales("Lechuga"),  600, 100),
    (FrutasyVegetales("Aguacate"), 720, 100),
    
    (FrutasyVegetales("Mango"),    480, 270),
    (FrutasyVegetales("Fresa"),    600, 270),
    (FrutasyVegetales("Banano"),   720,270),

    (Panes("Tortilla"),            480, 390),
    (Papa(),                       600, 390),
]

#Cocina
class CocinaVegan:
    #Atributos
    def __init__(self, tiempoIni=180):
        self.tiempo = tiempoIni
        self.chefs = []
        self.ordenes = []
        self.estaciones = []
        self.inicializarEstaciones()
    
    def inicializarEstaciones(self):
        #Estaciones de trabajo
           self.tabla    = TablaDePicar(70, 170)
           self.freidora = Freidora(190, 170)
           self.entrega  = Entrega(310, 170)
           self.mesa     = MesaNormal(290, 290)

           self.estaciones.extend([
            self.tabla,
            self.freidora,
            self.entrega,
            self.mesa,
        ])

        #Despensa
           for ingrediente, x, y in DESPENSA_VEGAN:
            self.estaciones.append(Despensa(x,y,ingrediente))
    
    #Chefs
    def agregarChef(self, chef):
        if len(self.chefs) < 2:
            self.chefs.append(chef)
        else:
            print("Solo pueden haber 2 chefs en la cocina")
    
    #Recetas
    def generarReceta(self):
        nueva = random.choice(RECETAS_VEGAN)()
        self.ordenes.append(nueva)
        print(f"NUEVA ORDEN: {nueva.nombre} "
              f"({len(nueva.lista_ingredientes)} ingredientes, "
              f"{nueva.puntaje} pts)")
        return nueva
    
    def entregarReceta(self, chef, ingredientesEntregados):
        for receta in self.ordenes:
            if receta.compararReceta(ingredientesEntregados):
                chef.puntos += receta.puntaje
                print(f"{chef.nombre} completó '{receta.nombre}' "
                      f"y obtuvo {receta.puntaje} pts.") 
                self.ordenes.remove(receta)
                return True
        print("Receta incorrecta, no coincide con ninguna orden activa.")
        return False
    
    #Temporizador
    def actualizarTiempo(self):
        for receta in self.ordenes[:]:
            eliminar = receta.actualizarTiempo(1)
            if eliminar:
                self.ordenes.remove(receta)
                print(f"Receta '{receta.nombre}' eliminada. "
                      f"Penalización: -{receta.puntaje_original} pts.")
            

##############################
if __name__ == "__main__":
    from Clase_Estacion_y_Chef import Chef
 
    cocina = CocinaVegan(180)
    chef1  = Chef("Chef 1", 100, 300, velocidad=3)
    cocina.agregarChef(chef1)
 
    print("=== Escenario Vegan ===")
    print(f"Estaciones: {[e.nombre for e in cocina.estaciones]}")
    print()
 
    # Generamos 3 recetas aleatorias
    for _ in range(3):
        cocina.generarReceta()
 
    print(f"\nÓrdenes activas: {[r.nombre for r in cocina.ordenes]}")
 
    # Simulamos entregar la Ensalada Fresca correctamente
    tomate  = FrutasyVegetales("Tomate")
    tomate.preparar()   # crudo -> picado
 
    lechuga = FrutasyVegetales("Lechuga")
    lechuga.preparar()  # crudo -> picado
 
    print("\n--- Intentando entregar Ensalada Fresca ---")
    cocina.ordenes.append(EnsaladaFresca())  # nos aseguramos que esté activa
    resultado = cocina.entregarReceta(chef1, [tomate, lechuga])
    print("¿Entrega exitosa?", resultado)
    print("Puntos del chef:", chef1.puntos)