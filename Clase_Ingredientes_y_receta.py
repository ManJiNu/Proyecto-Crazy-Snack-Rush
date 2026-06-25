class Ingredientes:
    def __init__(self, nombre, estado="crudo"):
        self.nombre = nombre
        self.estado = estado
    
    def preparar(self):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}({self.nombre}, {self.estado})"
    
class FrutasyVegetales(Ingredientes):
    def __init__(self, nombre, estado="crudo"):
        super().__init__(nombre, estado)
    
    def preparar(self):
        if self.estado == "crudo":
            self.estado = "picado"

class Proteina(Ingredientes):
    def __init__(self, nombre, estado="crudo"):
        super().__init__(nombre, estado)
        self.cocinada = False
    
    def preparar(self):
        if self.estado == "crudo":
            self.estado = "cocinado"
            self.cocinada = True
        elif self.estado == "cocinado":
            self.estado = "quemado"

class Panes(Ingredientes):
    def __init__(self, nombre, estado="preparado"):
        super().__init__(nombre, estado)
    
    def preparar(self):
        pass

class Papa(Ingredientes):
    def __init__(self, nombre="Papa"):
        super().__init__(nombre, "crudo")

    def preparar(self):
        """Se usa en la Freidora: crudo pasa a frito."""
        if self.estado == "crudo":
            self.estado = "frito"

class Plato:
    def __init__(self):
        self.ingredientes_adentro=[] #Lista para ir acumulando ingredientes
        self.esta_sucio = False #Para lavar platos si me diera tiempo de hacerlo
    def agregar_ingrediente(self, ingrediente):
        if ingrediente.estado in ["picado", "cocinado", "preparado", "frito"]:
            self.ingredientes_adentro.append(ingrediente)
            print (f"Se agregó {ingrediente.nombre} al plato. Contenido actual: {self.ingredientes_adentro}")
            return True
        else:
            print(f"¡No puedes poner {ingrediente.nombre} crudo en el plato!")
            return False 

class Receta:
    def __init__(self, nombre, lista_ingredientes):
        self.nombre = nombre
        self.lista_ingredientes  = lista_ingredientes
        self.puntaje = 10 * len(lista_ingredientes)
        self.puntaje_original = self.puntaje
        self.tiempo = 60 * len(lista_ingredientes)
        self.tiempo_restante = self.tiempo
    
    def compararReceta(self, ingredientes_entregados):
        if len(ingredientes_entregados) != len(self.lista_ingredientes):
            return False
        pendientes = list(self.lista_ingredientes)
        
        for entregado in ingredientes_entregados:
            encontrado = None #Se le hizo un cambio para comparar los ingredientes realmente
            for requerido in pendientes:
                if (
                    type(entregado) == type(requerido)
                    and entregado.nombre == requerido.nombre
                    and entregado.estado == requerido.estado
                ):
                    encontrado = requerido
                    break
            if encontrado is None:
                return False
            pendientes.remove(encontrado)
        return True

    def actualizarTiempo(self, delta_tiempo):

        '''
         Disminuye el tiempo restante. Si llega a 0, reduce el puntaje
        a la mitad y reinicia el contador. Retorna True si la receta
        debe eliminarse (puntaje llegó a 0).
        '''
        self.tiempo_restante -= delta_tiempo
        if self.tiempo_restante  <= 0:
            self.reducir_puntaje()
            self.tiempo_restante = self.tiempo

            if self.puntaje <= 0:
                return True
            
        return False
    def reducir_puntaje(self):
        self.puntaje = self.puntaje // 2
    
    def __repr__(self):
        return f"Receta({self.nombre}, puntaje = {self.puntaje}, tiempo restante ={self.tiempo_restante})"



    




    