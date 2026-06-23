import pygame
from menu import boton
from controles import controles
from cocina import Cocina
from Clase_Estacion_y_Chef import Chef, TablaDePicar, Sarten, Freidora, Entrega, Despensa
from Clase_Ingredientes_y_receta import FrutasyVegetales, Proteina, Papa, Panes

# Inicio pygame
pygame.init()

# Tamaño de la ventana del juego
ANCHO = 800
ALTO = 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Crazy Snack Rush TEC")
clock = pygame.time.Clock() # Controla los FPS del juego

# Fuentes
# 
#  para los textos en pantalla
fuente = pygame.font.SysFont("Arial", 40, bold=True)
fuente_titulo = pygame.font.SysFont("Arial", 60, bold=True)
fuente_pequeña = pygame.font.SysFont("Arial", 20) # Para recetas
fuente_pequeña2 = pygame.font.SysFont("Arial", 25) # Para ingrediente en mano

# Botones del menú principal
btn_jugar = boton(300, 250, 200, 50, "Jugar", fuente)
btn_instrucciones = boton(300, 330, 200, 50, "Instrucciones", fuente)
btn_creditos = boton(300, 410, 200, 50, "Creditos", fuente)

# Variable que controla en qué pantalla estamos
# Puede ser "menu", "juego" o "game_over"
pantalla_actual = "menu"
corriendo = True

# Lista donde voy guardando los ingredientes antes de entregarlos
ingredientes_acumulados = []

# Creo la cocina con 180 segundos de tiempo de juego
cocina = Cocina(180)

# Creo los 2 chefs con su posición inicial y velocidad
chef1 = Chef("Chef 1", 100, 300, velocidad=3)
chef2 = Chef("Chef 2", 150, 300, velocidad=3)
cocina.agregarChef(chef1)
cocina.agregarChef(chef2)
chefActivo = chef1 # El chef naranja empieza siendo el activo

# Creo las estaciones de trabajo y las agrego a la cocina
tabla = TablaDePicar(100, 100)    # Aqui se pican los vegetales
sarten = Sarten(200, 100)         # Aqui se cocina la proteina
freidora = Freidora(300, 100)     # Aqui se frien las papas
entrega = Entrega(400, 100)       # Aqui se entregan las recetas terminadas
cocina.agregarEstacion(tabla)
cocina.agregarEstacion(sarten)
cocina.agregarEstacion(freidora)
cocina.agregarEstacion(entrega)

# Creo las despensas donde el chef recoge los ingredientes
despensa_tomate = Despensa(500, 100, FrutasyVegetales("Tomate"))  # Primera D
despensa_carne = Despensa(580, 100, Proteina("Carne"))             # Segunda D
despensa_papa = Despensa(660, 100, Papa())                         # Tercera D
cocina.agregarEstacion(despensa_tomate)
cocina.agregarEstacion(despensa_carne)
cocina.agregarEstacion(despensa_papa)

# Este timer dispara un evento cada 1000ms (1 segundo) para el temporizador
pygame.time.set_timer(pygame.USEREVENT, 1000)

# Funcion que revisa si el chef esta cerca de una estacion para interactuar
def cerca_de_estacion(chef, estacion, distancia=70):
    return (abs(chef.posicion_x - estacion.posicion_x) < distancia and
            abs(chef.posicion_y - estacion.posicion_y) < distancia)

# Loop principal, corre 60 veces por segundo hasta que el jugador cierre el juego
while corriendo:

    # Reviso todos los eventos que ocurren (teclas, clicks, tiempo)
    for evento in pygame.event.get():

        # Si el jugador cierra la ventana, salgo del loop
        if evento.type == pygame.QUIT:
            corriendo = False

        # Cada segundo reduzco el tiempo de la cocina
        if evento.type == pygame.USEREVENT:
            if pantalla_actual == "juego":
                cocina.actualizarTemporizador()
                if cocina.tiempo <= 0:
                    pantalla_actual = "game_over" # Se acabo el tiempo

        # Si clickean Jugar, genero una receta y cambio a pantalla de juego
        if btn_jugar.fue_clickeado(evento):
            cocina.generarReceta()
            pantalla_actual = "juego"
            ingredientes_acumulados = []

        if btn_instrucciones.fue_clickeado(evento):
            print("INSTRUCCIONES")

        if btn_creditos.fue_clickeado(evento):
            print("CREDITOS")

        # Logica que solo corre cuando estamos en el juego
        if pantalla_actual == "juego":
            # Muevo al chef con WASD y cambio con TAB
            chefActivo = controles(evento, chefActivo, cocina.chefs)

            # Si el jugador presiona E, interactua con la estacion mas cercana
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_e:
                for estacion in cocina.estaciones:
                    if cerca_de_estacion(chefActivo, estacion):

                        # Si es despensa y tengo las manos vacias, recojo el ingrediente
                        if isinstance(estacion, Despensa):
                            if chefActivo.ingrediente_a_mano is None:
                                chefActivo.recoger_ingrediente(estacion.ingrediente_tipo)
                                print(f"Recogiste: {estacion.ingrediente_tipo.nombre}")

                        # Si es entrega, agrego el ingrediente y valido la receta
                        elif isinstance(estacion, Entrega):
                            if chefActivo.ingrediente_a_mano:
                                ingredientes_acumulados.append(chefActivo.ingrediente_a_mano)
                                chefActivo.soltar_ingrediente()
                                print(f"Ingrediente agregado, total: {len(ingredientes_acumulados)}")
                                resultado = cocina.entregarReceta(chefActivo, ingredientes_acumulados)
                                if resultado: # Si la receta fue correcta, limpio la lista
                                    ingredientes_acumulados = []

                        # Si es tabla, sarten o freidora, proceso el ingrediente
                        else:
                            if chefActivo.ingrediente_a_mano:
                                estacion.procesarIngredientes(chefActivo.ingrediente_a_mano)
                                print(f"Procesado en {estacion.nombre}")

    # Dibujo la pantalla segun en cual estemos
    if pantalla_actual == "menu":
        ventana.fill((173, 224, 255))
        titulo = fuente_titulo.render("Crazy Snack Rush TEC", True, (50, 50, 50))
        ventana.blit(titulo, (80, 100))
        pos_mouse = pygame.mouse.get_pos()
        btn_jugar.actualizar_hover(pos_mouse)
        btn_instrucciones.actualizar_hover(pos_mouse)
        btn_creditos.actualizar_hover(pos_mouse)
        btn_jugar.dibujar(ventana)
        btn_instrucciones.dibujar(ventana)
        btn_creditos.dibujar(ventana)

    elif pantalla_actual == "juego":
        ventana.fill((200, 230, 200))

        # Muestro el tiempo restante y los puntos del chef activo
        tiempo_texto = fuente.render(f"Tiempo: {cocina.tiempo}", True, (50, 50, 50))
        ventana.blit(tiempo_texto, (550, 20))
        puntaje_texto = fuente.render(f"Puntos: {chefActivo.puntos}", True, (50, 50, 50))
        ventana.blit(puntaje_texto, (550, 60))

        # Muestro las recetas que hay que preparar
        y_receta = 20
        for receta in cocina.ordenes:
            texto_receta = fuente_pequeña.render(f"{receta.nombre} - {receta.puntaje}pts", True, (50, 50, 50))
            ventana.blit(texto_receta, (20, y_receta))
            y_receta += 30

        # Muestro el ingrediente que tiene el chef en mano
        if chefActivo.ingrediente_a_mano:
            ing_texto = fuente_pequeña2.render(
                f"En mano: {chefActivo.ingrediente_a_mano.nombre} ({chefActivo.ingrediente_a_mano.estado})",
                True, (50, 50, 50))
            ventana.blit(ing_texto, (20, ALTO - 40))

        # Dibujo cada estacion como un cuadro cafe con la primera letra de su nombre
        for estacion in cocina.estaciones:
            pygame.draw.rect(ventana, (139, 90, 43), (estacion.posicion_x, estacion.posicion_y, 60, 60))
            nombre = fuente.render(estacion.nombre[0], True, (255, 255, 255))
            ventana.blit(nombre, (estacion.posicion_x + 20, estacion.posicion_y + 15))

        # Dibujo los chefs, naranja = activo, azul = inactivo
        for chef in cocina.chefs:
            color = (255, 100, 0) if chef == chefActivo else (0, 100, 255)
            pygame.draw.rect(ventana, color, (chef.posicion_x, chef.posicion_y, 40, 40))

    # Pantalla que aparece cuando se acaba el tiempo
    elif pantalla_actual == "game_over":
        ventana.fill((50, 50, 50))
        game_over_texto = fuente_titulo.render("GAME OVER", True, (255, 50, 50))
        ventana.blit(game_over_texto, (220, 200))
        puntos_texto = fuente.render(f"Puntos: {chef1.puntos + chef2.puntos}", True, (255, 255, 255))
        ventana.blit(puntos_texto, (300, 320))

    # Actualizo la pantalla y limito a 60 FPS
    pygame.display.flip()
    clock.tick(60)

pygame.quit()