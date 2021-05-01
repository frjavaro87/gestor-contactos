#utilizando las clases......

class Automovil:

    def _init_(self):
        self.Carmodel = "prius"
        self.puertas = 2
        self.motor = 1
        self.tipomotor = "Hibrido"

    def CaracteristicasAuto(self):

        print(f'El {self.Carmodel} es un auto de {self.puertas} y de motor {self.tipomotor}')

    def CrearAutoNuevo(self):
        self.Carmodel = input("Ingrese el nombre del modelo: ")
        self.puertas = int(input("Ingrese el numero de puertas: "))
        self.motor = int(input("Cuántos motores tiene el auto?: "))
        self.tipomotor = input("Ingrese el tipo de motor: ")

def main():
    Auto = Automovil()

    for i in range(3):

        Auto.CrearAutoNuevo()
        Auto.CaracteristicasAuto()

    print("Todos los modelos han sido cargados")

if __name__ == '__main__':

    main()
