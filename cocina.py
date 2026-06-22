#########Esta seccion de codigo es para la clase cocina########
import random #Me genera cualquier receta sin patron alguno
from Clase_Ingredientes_y_receta import (
    Receta,
    FrutasyVegetales,
    Proteina,
    Panes,
    Papa
)
class Cocina:
    def __init__(self,tiempoInicial):
        self.tiempo = tiempoInicial
        self.chefs = [] #Guarda a los 2 chefs, empieza vacia
        self.ordenes = []#Recetas generadas para entregar
        self.estaciones = [] #Administrada por cocina
    
    def generarReceta(self):
        #Lo que procede aqui es importar la clase receta para para trabajar con ellas(esperar recetas del companero al que le tocan)
        recetasDisponibles = [
            Receta(
                "Hamburguesa",
                [
                    Proteina("Carne","cocinado"),
                    Panes("Pan")
                ]
            ),
            Receta(
                "Papas Fritas",
                [
                    Papa()
                ]
            ),
            Receta(
                "Ensalada",
                [
                    FrutasyVegetales("Tomate", "picado"),
                    FrutasyVegetales("Lechuga", "picado")
                ]
            )
        ]   
        nuevaReceta = random.choice(recetasDisponibles)
        self.ordenes.append(nuevaReceta)
        print(f"NUEVA ORDEN GENERADA:{nuevaReceta.nombre}") #Nota:Crear objeto Receta real y agregarlo a self.ordenes
        return nuevaReceta

        #Creacion del objeto
        #nuevaReceta = Receta(recetaSeleccionada)
        #self.ordenes.append(nuevaReceta)
        #return nuevaReceta

     ####Este bloque me da el temporizador para las recetas, tiempo de ronda en general########

    def actualizarTemporizador(self): #Me dice si la partida termina o no y disminuye el tiempo con cada receta
        if self.tiempo>0:
            self.tiempo -=1 #Reduzco el tiempo
            self.actualizarTiempoRecetas()#Me reduce el tiempo de las recetas activas
        else:
            print("TIEMPO TERMINADO! GAME OVER") #si el tiempo ya es menor a 0 entonces termina la partida
    def actualizarTiempoRecetas(self): #Esto me administra cuanto duran las recetas activdas
        for receta in self.ordenes[:]:
            eliminar = receta.actualizarTiempo(1)
            if eliminar:
                self.ordenes.remove(receta)
                print("RECETA ELIMINADA.PENALIZACION") #TODOo # Aplicar penalización al jugador

    def agregarChef(self, ChefObjeto):#Agrega un chef a la lista
        if len(self.chefs)<2:
            self.chefs.append(ChefObjeto)
        else:
            print("SOLO PUEDEN HABER 2 CHEFS EN LA COCINA")
    def agregarEstacion(self,estacionObjeto): #Para estaciones
        self.estaciones.append(estacionObjeto)

    def entregarReceta(self,chef,ingredientesEntregados): #En esta seccion quiero comparar la receta actual con la que hizo el jugador.
        for receta in self.ordenes: #Recorre todas las recetas activas
            if receta.compararReceta(ingredientesEntregados):
                chef.puntos+= receta.puntaje #Aqui estoy poniendo puntos si lo hicieron bien
                print(
                    f"{chef.nombre} hizo "#Aqui estoy poniendo lo que pasa si tienen bien la receta
                    f"{receta.nombre} y obtuvo "
                    f"{receta.puntaje} puntos "
                )
                self.ordenes.remove(receta)#Cuando se valida elimina la orden
                return True 
        print("RECETA EQUIVICADA, NO COINCIDE")
        return False #En caso contrario pues no coincide y se alerta al usuario

if __name__ == "__main__":

    mi_cocina = Cocina(180)

    print(f"Tiempo inicial: {mi_cocina.tiempo}s")

    mi_cocina.generarReceta()

    mi_cocina.actualizarTemporizador()

    print(f"Tiempo restante: {mi_cocina.tiempo}s")