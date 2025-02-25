class Vehicle:
    def __init__(self, typeVehicle: str, name: str, model: str, horses: float, quantyWheels: int):
        self.typeVehicle: str = typeVehicle
        self.model: str = model
        self.name: str = name
        self.horses: float = horses
        self.quantyWheels: int = quantyWheels
        self.isOn: bool = False

    def getTypeVehicle(self) -> str:
        return self.typeVehicle
    
    def getModel(self) -> str:
        return self.model
    
    def getName(self) -> str:
        return self.name
    
    def getHorses(self) -> float:
        return self.horses
    
    def getQuantityWheels(self) -> int:
        return self.quantyWheels
    
    def getIsOn(self) -> bool:
        return self.isOn

    def start(self) -> None:
        if not self.isOn:
            print(f"Ligando o(a) {self.typeVehicle}") 
        else: 
            print("Veiculo já esta ligado!")

    def off(self) -> None:
        if self.isOn:
            print(f"Desligando o(a) {self.typeVehicle}") 
        else: 
            print("Veiculo já esta desligado!")

    def maxVelocity(self) -> None:
        division: float = (self.horses / 60) * 25
        print(f"Velocidade maxima {division:.2f}Km/h")

    def makeSound() -> None:
        NotImplementedError("Implemente o metodo!")

class Car(Vehicle):
    def __init__(self, typeVehicle, name, model, horses, quantyWheels, quantityDoors: int):
        super().__init__(typeVehicle, name, model, horses, quantyWheels)

        self.quantyDoors: int = quantityDoors

    def makeSound():
        print("Vrum Vrum! tututututu!")

class Bike(Vehicle):
    def __init__(self, typeVehicle, name, model, horses, quantyWheels):
        super().__init__(typeVehicle, name, model, horses, quantyWheels)

    def makeSound() -> None:
        print("randaandandandan!")

if __name__ == "__main__":
    motocycle: Bike = Bike("Moto", "Harley", "Harley-Davidson", 400, 2)
    car: Car = Car("Carro", "Supra", "Toyota", 550, 4, 2)

    motocycle.maxVelocity()
    car.maxVelocity()