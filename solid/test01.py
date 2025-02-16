class Animal:
    def make_a_sound(self) -> None:
        raise NotImplementedError("Implemente o metodo!")
    
    def move(self) -> None:
        raise NotImplementedError("Implemente o metodo!")
    

class Cat(Animal):
    def make_a_sound(self):
        print("Miau Miau")

    def move(self):
        print("Foi pra frente!")


cat = Cat()
cat.move()