from abc import ABC, abstractmethod

# Clase abstracta Producto
class Producto(ABC):
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def mostrar_detalles(self):
        pass

# Subclase Electronico
class Electronico(Producto):
    def __init__(self, nombre: str, precio: float, garantia: int):
        super().__init__(nombre, precio)
        self.garantia = garantia

    def mostrar_detalles(self):
        print(f"Electrónico: {self.nombre} - Precio: ${self.precio} - Garantía: {self.garantia} meses")

# Subclase Alimento
class Alimento(Producto):
    def __init__(self, nombre: str, precio: float, caducidad: str):
        super().__init__(nombre, precio)
        self.caducidad = caducidad

    def mostrar_detalles(self):
        print(f"Alimento: {self.nombre} - Precio: ${self.precio} - Caducidad: {self.caducidad}")

# Subclase Ropa
class Ropa(Producto):
    def __init__(self, nombre: str, precio: float, talla: str):
        super().__init__(nombre, precio)
        self.talla = talla

    def mostrar_detalles(self):
        print(f"Ropa: {self.nombre} - Precio: ${self.precio} - Talla: {self.talla}")

# Función principal que demuestra polimorfismo
def main():
    inventario = [
        Electronico("Laptop HP", 15000.0, 12),
        Alimento("Leche deslactosada", 25.50, "2025-09-30"),
        Ropa("Hoodie Negra", 699.99, "M")
    ]

    print("INVENTARIO DE PRODUCTOS:\n")
    for producto in inventario:
        producto.mostrar_detalles()

if __name__ == "__main__":
    main()