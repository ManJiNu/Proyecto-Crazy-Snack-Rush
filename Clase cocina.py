#########Esta seccion de codigo es para la clase cocina########
import random #Me genera cualquier receta sin patron alguno
class Cocina:
    def __init__(self,tiempoInicial):
        self.tiempoInicial = tiempoInicial
        self.chefs = [] #Guarda a los 2 chefs, empieza vacia
        self.ordenes = []#Recetas generadas para entregar
        self.estaciones = [] #Administrada por cocina
    
    def generarReceta(self):
        #Lo que procede aqui es importar la clase receta para para trabajar con ellas(esperar recetas del companero al que le tocan)
        recetasDisponibles = ["Panini", "Hamburguesa", "Ensalada de frutas", "Papas locas", "Brisket", "Tacos de birria", "Jugo de tomate"]
        recetaSeleccionada = random.choice(recetasDisponibles)
        print(f"NUEVA ORDEN GENERADA:{recetaSeleccionada}")

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
            receta.maxTimeReceta -=1
            if receta.maxTimeReceta ==0:
                receta.puntosReceta //=2 #Si se acaba el tiempo los puntos se reducen a la mitad
                print(f"LA RECETA HA EXPIRADO. PUNTOS REDUCIDOS A: {receta.puntosReceta}")

                if receta.puntosReceta <=0: #Si la puntuacion llega a 0 (elegir con equipo penalizacion)
                    self.ordenesRemove(receta)
                    print("RECETA ELIMINADA.PENALIZACION")
    def agregarChef(self, ChefObjeto):#Agrega un chef a la lista
        if len(self.chefs)<2:
            self.chefs.append(ChefObjeto)
        else:
            print("SOLO PUEDEN HABER 2 CHEFS EN LA COCINA")
    def agregarEstacion(self,estacionObjeto): #Para estaciones
        self.estaciones.append(estacionObjeto)

if __name__ == "__main__":
    # Creamos una cocina con 180 segundos de juego
    mi_cocina = Cocina(tiempoInicial=180)
    
    # Simulamos el paso del tiempo y generación de órdenes
    print(f"Tiempo inicial: {mi_cocina.tiempo}s")
    mi_cocina.generar_receta()
    
    # Simulamos que pasa 1 segundo
    mi_cocina.actualizar_temporizador()
    print(f"Tiempo restante: {mi_cocina.tiempo}s")


