import random

class Automovil:
    
    def __init__(self, color: str, marca: str, velocidad: float, aceleracion: float):
        self.ruedas = 4
        self.color = color
        self.marca = marca
        self.velocidad = velocidad
        self.aceleracion = aceleracion

    def __str__(self):
        return (f"Automóvil {self.marca} de color {self.color}:\n"
                f"  • Ruedas: {self.ruedas}\n"
                f"  • Velocidad: {self.velocidad:.1f} km/h\n"
                f"  • Aceleración: {self.aceleracion:.2f} m/s²")


def crear_auto_aleatorio() -> Automovil:
    colores = ["Rojo", "Azul", "Negro", "Blanco", "Verde", "Amarillo"]
    marcas = ["Toyota", "Ford", "Chevrolet", "Honda", "BMW", "Tesla"]
    
    color = random.choice(colores)
    marca = random.choice(marcas)
    
    velocidad = random.uniform(40, 120)
    
    aceleracion = random.uniform(1.0, 5.0)
    return Automovil(color, marca, velocidad, aceleracion)


if __name__ == "__main__":
    
    auto_nuevo = crear_auto_aleatorio()
    print(auto_nuevo)
