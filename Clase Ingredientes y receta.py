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
        """Se usa en la Freidora: crudo -> frito."""
        if self.estado == "crudo":
            self.estado = "frito"



class Receta:
    
    




    