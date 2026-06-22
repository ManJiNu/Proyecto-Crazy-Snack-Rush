from cocina import Cocina 
from Clase_Estacion_y_Chef import (Chef, TablaDePicar,Sarten,Freidora,Entrega)

#####################CREACION DE LA COCINA#################
cocina = Cocina(180)
#####################CREACION DE CHEFS#####################
chef1 = Chef(
    nombre = "Chef 1",
    posicion_x=0,
    posicion_y=0,
    velocidad=5
)

chef2 = Chef(
    nombre ="Chef 2",
    posicion_x=50,
    posicion_y=0,
    velocidad=5

)

cocina.agregarChef(chef1)
cocina.agregarChef(chef2)
####################CREACION DE ESTACIONES################
tabla = TablaDePicar(100,100)
sarten = Sarten(200,100)
freidora = Freidora(300,100)
entrega = Entrega(400,100)

cocina.agregarEstacion(tabla)
cocina.agregarEstacion(sarten)
cocina.agregarEstacion(freidora)
cocina.agregarEstacion(entrega)
####################PRUEBAS###############################

print("COCINA CREADA")
print (f"TIEMPO INICIAL: {cocina.tiempo}")
print (f"CANTIDAD DE CHEFS:{len(cocina.chefs)}")
print(f"CANTIDAD DE ESTACIONES:{len(cocina.estaciones)}")

print("\nCHEFS REGISTRADOS:") #\n se usa para indicar la cantidad
for chef in cocina.chefs:
    print(f"-{chef.nombre}")

print("\nESTACIONES REGISTRADAS:")
for estacion in cocina.estaciones:
    print(f"-{estacion.nombre}")

print("\nGENERANDO ORDEN...")
recetaGenerada = cocina.generarReceta()
print(cocina.ordenes)
print ("\nPROBANDO ENTREGA...")
ingredientesPrueba = recetaGenerada.lista_ingredientes#Me compara las 2 recetas 
cocina.entregarReceta(
    chef1,
    ingredientesPrueba
)
print (f"PUNTOS DE {chef1.nombre}:{chef1.puntos}")
print(cocina.ordenes)
print("\nPROBANDO TEMPORIZADOR...")
cocina.actualizarTemporizador()
print(f"TIEMPO RESTANTE:{cocina.tiempo}")


print("\nORDENES ACTIVAS:")#Para ver las ordenes que se estan ejecutando
for receta in cocina.ordenes:
    print(receta)

print("n\PROBANDO ESTACIONES") #En esta seccion pruebo si sirve el procesamiento de ingredientes
##Pruebo si el tomate se pica##
tomate = FrutasyVegetales("Tomate")
print(
    f"ESTADO INICIAL TOMATE:"
    f"{tomate.estado}"
)
tabla.procesarIngredientes(tomate) #AL PASAR POR LA TABLA EL ESTADO DEBERIA CAMBIAR A PICADO
print(
    f"ESTADO FINAL DEL TOMATE:"
    f"{tomate.estado}"
)
 ##Pruebo si la carne se cocina##
carne = Proteina("Carne")
print(
   f"ESTADO INICIAL CARNE:"
   f"{carne.estado}"
)
sarten.procesarIngredientes(carne)
print(
   f"ESTADO FINAL CARNE:"
   f"{carne.estado}"
)

##Pruebo si la papa se frie##
papa = Papa()
print(
    f"ESTADO INICIAL PAPA:"
    f"{papa.estado}"
)
freidora.procesarIngredientes(papa)
print(
    f"ESTADO FINAL PAPA:"
    f"{papa.estado}"
)