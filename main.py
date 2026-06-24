import pygame 
import random
import sys
from cocina import Cocina 
from Clase_Estacion_y_Chef import (Chef, TablaDePicar,Sarten,Freidora,Entrega,Despensa,MesaNormal)
from Clase_Ingredientes_y_receta import (FrutasyVegetales,Proteina,Papa,Panes)
from controles import controles #Integro el archivo de Luis de controles 
from menu import boton
import os #Tuve que meter esta porque no queria encontrar las imagenes



#####################CREACION DE LA COCINA#################
cocina = Cocina(180)
#####################CREACION DE CHEFS#####################
chef1 = Chef(
    nombre = "Chef 1",
    posicion_x=200,
    posicion_y=300,
    velocidad=5
)

chef2 = Chef(
    nombre ="Chef 2",
    posicion_x=400,
    posicion_y=300,
    velocidad= 5
)

cocina.agregarChef(chef1)
cocina.agregarChef(chef2)
####################CREACION DE ESTACIONES################
#Las reubico para que todo salga ordenado en pantalla
tabla = TablaDePicar(100,250)
sarten = Sarten(100,400)
freidora = Freidora(640,250)
entrega = Entrega(640,400)
##################Agrego despensas para interactuar con ingredientes nuevos########
despensa_tomate = Despensa(150,110,"Tomate")
despensa_carne = Despensa(270,110,"Carne")
despensa_pan = Despensa(390,110,"Pan")
despensa_papa = Despensa(510,110,"Papa")
mesa_platos = MesaNormal(630, 110)
cocina.agregarEstacion(tabla)
cocina.agregarEstacion(sarten)
cocina.agregarEstacion(freidora)
cocina.agregarEstacion(entrega)
cocina.agregarEstacion(despensa_tomate)
cocina.agregarEstacion(despensa_carne)
cocina.agregarEstacion(despensa_pan)
cocina.agregarEstacion(despensa_papa)
cocina.agregarEstacion(mesa_platos)
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
print("--PRUEBAS DE CONSOLA TERMINADAS CON EXITO. CORRIENDO PYGAME....ENGAGE---")

##############################################################################################
#INICIO PANTALLA PYGAME EN ESTE MOMENTO
############################################################################################
pygame.init()
ANCHO = 880
ALTO = 600
ventana = pygame.display.set_mode((ANCHO, ALTO)) #Configuro dimensiones de las ventanas #Bloque de Manfred
pygame.display.set_caption("Crazy Snack Rush TEC")
clock = pygame.time.Clock()
#Configuro fuentes 
fuente = pygame.font.SysFont("Allegro", 40, bold=True)
fuente_titulo = pygame.font.SysFont("Allegro", 60, bold=True)
fuente_pequeña = pygame.font.SysFont("Allegro", 20) 
fuente_pequeña2 = pygame.font.SysFont("Allegro", 25)
#CREACION DE LOS BOTONES#
fuente_botones = pygame.font.SysFont("Arial", 30, bold=True)
btn_jugar = boton(300, 410, 200, 45, "Jugar", fuente_botones)
btn_instrucciones = boton(300, 470, 200, 45, "Instrucciones", fuente_botones)
btn_creditos = boton(300, 530, 200, 45, "Créditos", fuente_botones)
#BOTONES DE SELECCION DE ESCENARIO
btn_es1 = pygame.Rect(100, 250, 180, 120)
btn_es2 = pygame.Rect(310, 250, 180, 120)
btn_es3 = pygame.Rect(520, 250, 180, 120)
#Reubico chefs
chef1.posicion_x, chef1.posicion_y = 200,300
chef2.posicion_x, chef2.posicion_y = 400, 300
#Configuro estado de inicio de la partida
pantalla_actual = "menu"
chef_activo = chef1
tiempo_ultima_receta = pygame.time.get_ticks()

#Genero una nueva orden si no hay nada
if len(cocina.ordenes) == 0:
    cocina.generarReceta()
#############IMAGEN MENU DE INICIO###############
ruta_carpeta = os.path.dirname(__file__)
ruta_imagen = os.path.join(ruta_carpeta, "Opening.jpg")
imagen_fondo = pygame.image.load(ruta_imagen)
imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO, ALTO))
imagen_cocina_raw = pygame.image.load("Game1.jpg").convert()
imagen_cocina = pygame.transform.scale(imagen_cocina_raw, (800, 600))
####imagenes implementos de cocina##########
img_tabla = pygame.image.load("TablaPicar.png").convert_alpha()
img_tabla = pygame.transform.scale(img_tabla, (110, 110))

img_sarten = pygame.image.load("Horno.png").convert_alpha()
img_sarten = pygame.transform.scale(img_sarten, (110, 110))

img_freidora = pygame.image.load("Freidora.png").convert_alpha()
img_freidora = pygame.transform.scale(img_freidora, (110, 110))

img_entrega = pygame.image.load("Mostrador.png").convert_alpha()
img_entrega = pygame.transform.scale(img_entrega, (110, 110))

img_mesa = pygame.image.load("Mesa.png").convert_alpha()
img_mesa = pygame.transform.scale(img_mesa, (110, 110))

img_plato = pygame.image.load("Plato.png").convert_alpha()
img_plato = pygame.transform.scale(img_plato, (60, 60))

img_crater_tomate = pygame.image.load("Tomate.png").convert_alpha()
img_crater_tomate = pygame.transform.scale(img_crater_tomate, (110, 110))

img_crater_carne = pygame.image.load("Carne.png").convert_alpha()
img_crater_carne = pygame.transform.scale(img_crater_carne, (110, 110))

img_crater_pan = pygame.image.load("Panes.png").convert_alpha()
img_crater_pan = pygame.transform.scale(img_crater_pan, (110, 110))

img_crater_papa = pygame.image.load("Papas.png").convert_alpha()
img_crater_papa = pygame.transform.scale(img_crater_papa, (110, 110))
#-------------CICLO PRINCIPAL DE INTERFAZ---------------------------------------------------------------------------------------------------------
running = True
while running: #DELTA TIME, obtengo el tiempo transcurrido
    dt = clock.tick(30) / 1000.0
    eventos = pygame.event.get() #####Obtencion de eventos. Esto es obligatorio en Pygame la verdad siempre esta segun lo que he visto####
    pos_mouse = pygame.mouse.get_pos()#Rastrea el puntero del mouse
    for event in eventos:
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        ##Eventos click del menu de inicio##
        if pantalla_actual == "menu":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if btn_jugar.rect.collidepoint(pos_mouse):
                    pantalla_actual = "seleccion_escenario"
        #Eentos click de la seleccion de escenario            
        elif pantalla_actual == "seleccion_escenario":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if btn_es1.collidepoint(pos_mouse):
                    pantalla_actual = "juego"  
                elif btn_es2.collidepoint(pos_mouse):
                    pantalla_actual = "juego"
                elif btn_es3.collidepoint(pos_mouse):
                    pantalla_actual = "juego"
                            
        elif pantalla_actual =="juego":  
            chef_activo = controles(event, chef_activo, cocina.chefs) 
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_SPACE, pygame.K_e]:
                    rect_chef = pygame.Rect(chef_activo.posicion_x, chef_activo.posicion_y, 40, 40)
                    rango_alcance = rect_chef.inflate(30, 30) # Caja de rango estirada

                    for est in cocina.estaciones: #A continuacion describo las acciones que pueden hacer los chefs. EXISTEN 3
                        rect_est = pygame.Rect(est.posicion_x, est.posicion_y, 110, 110)

                        if rango_alcance.colliderect(rect_est):
                            print("Colision con:", est.nombre)  
                         #SI ES DESPENSA Y EL CHEF NO TIENE NADA EN LA MANO SACO ALGO NUEOV
                            if isinstance(est, Despensa) and chef_activo.ingrediente_a_mano is None:
                                if est.ingrediente_tipo == "Tomate":
                                    chef_activo.recoger_ingrediente(FrutasyVegetales("Tomate"))
                                elif est.ingrediente_tipo == "Carne":
                                    chef_activo.recoger_ingrediente(Proteina("Carne"))
                                elif est.ingrediente_tipo == "Pan":
                                    chef_activo.recoger_ingrediente(Panes("Pan"))
                                elif est.ingrediente_tipo == "Papa":
                                    chef_activo.recoger_ingrediente(Papa())
                                break

                             #SI ES ALGO POR TRANSFORMAR MODIFICO SU ESTADO USANDO LOS METODOS QUE HICE. 
                        elif chef_activo.ingrediente_a_mano is not None:
                            item = chef_activo.ingrediente_a_mano
                            print("ESTOY CERCA DE UNA ESTACION")
                            print(type(est))
                            print(type(item))
                            
                            if isinstance(est, TablaDePicar) and isinstance(item, FrutasyVegetales): #PROCESAR
                                print("Uso la tabla")
                                est.procesarIngredientes(item)
                                break
                            elif isinstance(est, Sarten) and isinstance(item, Proteina):
                                est.procesarIngredientes(item)
                                break
                            elif isinstance(est, Freidora) and isinstance(item, Papa):
                                est.procesarIngredientes(item)
                                break
            
                            elif isinstance(est, Entrega): #ENTREGAR
                                comida = [chef_activo.ingrediente_a_mano]
                                exito = cocina.deliverReceta(chef_activo, comida) 
                                break
                        
                        if isinstance(est, MesaNormal):
                            if chef_activo.ingrediente_a_mano is not None and est.objeto_encima is None:
                                est.objeto_encima = chef_activo.ingrediente_a_mano
                                chef_activo.ingrediente_a_mano = None
                                print(f"Soltaste {est.objeto_encima.nombre} en la mesa")
                                break
                            elif chef_activo.ingrediente_a_mano is None and est.objeto_encima is not None:
                                chef_activo.ingrediente_a_mano = est.objeto_encima
                                est.objeto_encima = None
                                print(f"Recogiste {chef_activo.ingrediente_a_mano.nombre} de la mesa")
                                break


    if pantalla_actual == "menu":
        ventana.blit(imagen_fondo,(0,0))
        btn_jugar.hover = btn_jugar.rect.collidepoint(pos_mouse)
        btn_instrucciones.hover = btn_instrucciones.rect.collidepoint(pos_mouse)
        btn_creditos.hover = btn_creditos.rect.collidepoint(pos_mouse)
        for btn in [btn_jugar, btn_instrucciones, btn_creditos]:
            color_fondo = (240, 128, 128) if btn.hover else (173, 216, 230)
            color_borde = (255, 255, 255) if btn.hover else (120, 180, 210)
            pygame.draw.rect(ventana, (40, 50, 75), btn.rect.move(4, 4), border_radius=10)
            pygame.draw.rect(ventana, color_fondo, btn.rect, border_radius=10)
            pygame.draw.rect(ventana, color_borde, btn.rect, width=3, border_radius=10)

        #Ajusto la posicion de los botones##
        btn_jugar.dibujar(ventana)
        btn_instrucciones.dibujar(ventana)
        btn_creditos.dibujar(ventana)    
    #############PANTALLA DE SELECCION##########
    elif pantalla_actual == "seleccion_escenario":
        ventana.fill((15, 15, 20))
        ####Titulo de seleccion######
        fuente_titulo_sel = pygame.font.SysFont("Arial", 36, bold=True)
        texto_titulo = fuente_titulo_sel.render("SELECCIONA TU COCINA", True, (255, 255, 255))
        ventana.blit(texto_titulo, (240, 100))

        hover_es1 = btn_es1.collidepoint(pos_mouse)
        hover_es2 = btn_es2.collidepoint(pos_mouse)
        hover_es3 = btn_es3.collidepoint(pos_mouse)
        fuente_interna = pygame.font.SysFont("Arial", 26, bold=True) #Para texto dentro de los botones
        #Boton cocina 1
        color_es1 = (240, 128, 128) if hover_es1 else (173, 216, 230)
        pygame.draw.rect(ventana, (40, 50, 75), btn_es1.move(4, 4), border_radius=10)
        pygame.draw.rect(ventana, color_es1, btn_es1, border_radius=10)
        txt_es1 = fuente_interna.render("Fast Food", True, (40, 40, 40))
        rect_txt1 = txt_es1.get_rect(center=btn_es1.center)
        ventana.blit(txt_es1, rect_txt1)
        #Boton cocina 2
        color_es2 = (240, 128, 128) if hover_es2 else (173, 216, 230)
        pygame.draw.rect(ventana, (40, 50, 75), btn_es2.move(4, 4), border_radius=10)
        pygame.draw.rect(ventana, color_es2, btn_es2, border_radius=10)
        txt_es2 = fuente_interna.render("Texas BBQ", True, (40, 40, 40))
        rect_txt2 = txt_es2.get_rect(center=btn_es2.center)
        ventana.blit(txt_es2, rect_txt2)
        #Boton cocina 3
        color_es3 = (240, 128, 128) if hover_es3 else (173, 216, 230)
        pygame.draw.rect(ventana, (40, 50, 75), btn_es3.move(4, 4), border_radius=10)
        pygame.draw.rect(ventana, color_es3, btn_es3, border_radius=10)
        txt_es3 = fuente_interna.render("Vegan", True, (40, 40, 40))
        rect_txt3 = txt_es3.get_rect(center=btn_es3.center)
        ventana.blit(txt_es3, rect_txt3)
    #################### Fin###################################3
    elif pantalla_actual == "juego": 
        for event in eventos:
            chef_activo = controles(event, chef_activo, cocina.chefs) #Aqui empiezo a gestionar los controles del archivo de controles para la clase de chefs en la ocina

        cocina.tiempo -= dt #DELTA TIME. Controlo los tiempos
        if cocina.tiempo <=0:
            pantalla_actual = "game_over"

#GENERADOR DE RECETAS CADA 15 MINUTOS##
        ahora = pygame.time.get_ticks()
        if ahora - tiempo_ultima_receta> 15000: 
            if len (cocina.ordenes)<3: #Ella me genera un maximo de 3 recetas por estos minutos 
                cocina.generarReceta()
            tiempo_ultima_receta = ahora                       
 #Actualizo lo que duran las recetas, aqui entra en juego la reduccion de puntos 
        for receta in list(cocina.ordenes):
            if receta.actualizarTiempo(dt):
                cocina.ordenes.remove(receta)

#Aqui me di cuenta que se van de la pantalla asi que mejor puse esto para que respetaran los limites de la cuadricula
        if chef_activo.posicion_x < 0: chef_activo.posicion_x = 0
        if chef_activo.posicion_x > ANCHO - 40: chef_activo.posicion_x = ANCHO - 40
        if chef_activo.posicion_y < 110: chef_activo.posicion_y = 110        
        if chef_activo.posicion_y > ALTO - 40: chef_activo.posicion_y = ALTO - 40                         

#Fondito
        ventana.blit(imagen_cocina, (0, 0))
        tiempo_texto = fuente.render(f"TIEMPO:{int(cocina.tiempo)}s", True,(0,0,0))
        ventana.blit(tiempo_texto,(20,20))       
        puntos_texto = fuente.render(f"Puntos C1: {chef1.puntos} | C2: {chef2.puntos}", True, (0, 0, 0))
        ventana.blit(puntos_texto, (400, 20))                 

#Vista vertical de la lista de ordenes pendientes
        y_orden = 70
        for receta in cocina.ordenes:
            rec_texto = fuente_pequeña.render(f"Orden: {receta.nombre} ({int(receta.tiempo_restante)}s)", True, (0, 100, 0))
            ventana.blit(rec_texto, (20, y_orden))
            y_orden += 25

#Mensaje arribita que me dice que ingrediente lleva el chef encima
        if chef_activo.ingrediente_a_mano:
            ing_texto = fuente_pequeña2.render(
                f"En mano:{chef_activo.ingrediente_a_mano.nombre} ({chef_activo.ingrediente_a_mano.estado})",
                True,(50,50,50))
            ventana.blit(ing_texto,(20,ALTO -40))

#IDENTIFICO LA ESTACION PARA ELEGIR LA IMAGEN YA CARGADA
        for est in cocina.estaciones:
            # = pygame.Rect(est.posicion_x, est.posicion_y, 110, 110)
            sprite_actual = None
            if isinstance(est, TablaDePicar):
                sprite_actual = img_tabla
            elif isinstance(est, Sarten):
                sprite_actual = img_sarten
            elif isinstance(est, Freidora):
                sprite_actual = img_freidora
            elif isinstance(est, Entrega):
                sprite_actual = img_entrega
            elif isinstance(est, MesaNormal):
                sprite_actual = img_mesa
            elif isinstance(est, Despensa):
                if est.ingrediente_tipo == "Tomate":
                    sprite_actual = img_crater_tomate
                elif est.ingrediente_tipo == "Carne":
                    sprite_actual = img_crater_carne
                elif est.ingrediente_tipo == "Pan":
                    sprite_actual = img_crater_pan
                elif est.ingrediente_tipo == "Papa":
                    sprite_actual = img_crater_papa
            

            if sprite_actual:
                ventana.blit(sprite_actual, (est.posicion_x, est.posicion_y))
            else:
                pygame.draw.rect(ventana, (139, 90, 43), (est.posicion_x, est.posicion_y, 110, 110), border_radius=4)
            if isinstance(est, MesaNormal) and est.objeto_encima is not None:
                ventana.blit(img_plato, (est.posicion_x + 25, est.posicion_y + 15))
            nombre_letra = fuente_pequeña.render(est.nombre[0] if not isinstance(est, Despensa) else f"D:{est.ingrediente_tipo[0]}", True, (255, 255, 255))
            ventana.blit(nombre_letra, (est.posicion_x + 5, est.posicion_y - 18))

                # Dibujo de los chefs (Naranja para el activo, Azul para el inactivo)
        for chef in cocina.chefs:
            color_c = (255, 100, 0) if chef == chef_activo else (0, 100, 255)
            pygame.draw.rect(ventana, color_c, (chef.posicion_x, chef.posicion_y, 40, 40), border_radius=4)
    elif pantalla_actual == "game_over":
        ventana.fill((50, 50, 50))
        texto_game_over = fuente_titulo.render("GAME OVER", True, (255, 0, 0))
        ventana.blit(texto_game_over, (ANCHO // 2 - 180, ALTO // 2 - 50))

        txt_res = fuente_pequeña2.render(f"Puntaje Final Combinado: {chef1.puntos + chef2.puntos}", True, (255, 255, 255))
        ventana.blit(txt_res, (ANCHO // 2 - 160, ALTO // 2 + 30))


    # AGREGA LOS ESPACIOS AQUÍ ABAJO PARA QUE QUEDE ASÍ ENTRADA:
    pygame.display.flip()
