class Operation :
    nombre1 = 0
    nombre2 = 0
    def __init__(self, nombre1, nombre2): # Constructeur
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def str(self) :
        return (f"Le nombre1 est {self.nombre1} \nLe nombre2 est {self.nombre2}")

a = Operation(10, 5)

print(a.str())