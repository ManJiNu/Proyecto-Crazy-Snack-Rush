import pygame

FONDO =(15,20,40)
FONDO_PANEL   = (25,  35,  65)   
ACENTO        = (255, 200,  50)  
ACENTO_HOVER  = (255, 230, 120) 
TEXTO_CLARO   = (240, 240, 240)
TEXTO_OSCURO  = (15,  20,  40)
BOTON_NORMAL  = (40,  60, 110)
BOTON_HOVER   = (60,  90, 160)
BOTON_BORDE   = (255, 200,  50)
ESTRELLAS     = (200, 200, 255)

class boton:
    def __init__(self,x, y, ancho, alto, texto, fuente):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.texto = texto
        self.fuente = fuente
        self.hover = False
    def dibujar(self,superficie):
        color_fondo = BOTON_HOVER if self.hover else BOTON_NORMAL
        color_texto = ACENTO_HOVER if self.hover else ACENTO
        sombra = self.rect.move(4,4)
        pygame.draw.rect(superficie, (0, 0, 0, 80), sombra, border_radius=10)
        #Fondo del boton
        pygame.draw.rect(superficie, color_fondo, self.rect, width=2, border_radius=10)

        text_surf = self.fuente.render(self.texto, True, color_texto)
        texto_rect = texto_surf.get_rect(center=self.rect.center)
        superficie.blit(texto_surf, texto_rect)
 
    def actualizar_hover(self, pos_mouse):
        self.hover = self.rect.collidepoint(pos_mouse)
 
    def fue_clickeado(self, evento):
        return (
            evento.type == pygame.MOUSEBUTTONDOWN
            and evento.button == 1
            and self.rect.collidepoint(evento.pos))

