class AgenteInventario:
    def __init__(self):
        self.inventario = {}
    
    def agregar_item(self, item, cantidad):
        if item in self.inventario:
            self.inventario[item] += cantidad
        else:
            self.inventario[item] = cantidad
    
    def obtener_inventario(self):
        return self.inventario
