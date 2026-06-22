import pygame #Pygame es la libreria para hacer el juego

#Funcion de manejo de los personajes, el TAB es la tecla para cambior de un chef a otro
def controles(evento, chefActivo, chefs, teclaCambio=pygame.K_TAB):
    if evento.type == pygame.KEYDOWN:
        if evento.key == teclaCambio:
            iActual = chefs.index(chefActivo) #iActual quiere decir indice actual
            chefActivo = chefs[(iActual + 1) % len(chefs)] #Selecciona el siguiente chef de forma circular, cada que el jugador quiera cambiar de chef
    
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w]:
        chefActivo.mover_arriba()
    if teclas[pygame.K_s]:
        chefActivo.mover_abajo()
    if teclas[pygame.K_d]:
        chefActivo.mover_derecha()
    if teclas[pygame.K_a]:
        chefActivo.mover_izquierda()
    return chefActivo
