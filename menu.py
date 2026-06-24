import pygame

FONDO =(15,20,40)
#FONDO_PANEL   = (25,  35,  65)   
#ACENTO        = (255, 200,  50)  
#ACENTO_HOVER  = (255, 230, 120) 
#TEXTO_CLARO   = (240, 240, 240)
#TEXTO_OSCURO  = (15,  20,  40)
FONDO_BOTON_NORMAL = (30, 40, 70)       # Azul oscuro 
FONDO_BOTON_HOVER  = (235, 94, 40)      # Naranja 
TEXTO_NORMAL       = (15,  20,  40)    # Blanco claro
TEXTO_HOVER        = (15,  20,  40)    # Blanco 
COLOR_BORDE        = (255, 230, 120)     # Amarillo dorado 
#ESTRELLAS     = (200, 200, 255)

class boton:
    def __init__(self,x, y, ancho, alto, texto, fuente):
        self.rect = pygame.Rect(x - 25, y, ancho + 50, alto)
        self.texto = texto
        self.fuente = fuente
        self.hover = False
    def dibujar(self,superficie):
        color_fondo = FONDO_BOTON_HOVER if self.hover else FONDO_BOTON_NORMAL
        color_texto = TEXTO_HOVER if self.hover else TEXTO_NORMAL
        sombra = self.rect.move(5, 5)
        pygame.draw.rect(superficie, (15, 15, 25), sombra, border_radius=12) #Sombra negritam
        pygame.draw.rect(superficie, color_fondo, self.rect, border_radius=12) #Fondo del boton
        pygame.draw.rect(superficie, COLOR_BORDE, self.rect, width=3, border_radius=12) #COLOR BORDE
        text_surf = self.fuente.render(self.texto, True, color_texto)
        texto_rect = text_surf.get_rect(center=self.rect.center) #Renderizar
        superficie.blit(text_surf, texto_rect)



        #color_fondo = BOTON_HOVER if self.hover else BOTON_NORMAL
        #color_texto = ACENTO_HOVER if self.hover else ACENTO
        #sombra = self.rect.move(4,4)
        #pygame.draw.rect(superficie, (0, 0, 0, 80), sombra, border_radius=10)
        #Fondo del boton
    
 
    def actualizar_hover(self, pos_mouse):
        self.hover = self.rect.collidepoint(pos_mouse)
 
    def fue_clickeado(self, evento):
        return (
            evento.type == pygame.MOUSEBUTTONDOWN
            and evento.button == 1
            and self.rect.collidepoint(evento.pos)
            )

