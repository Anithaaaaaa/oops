class Petshop:
    def __init__(self, name, habitat, legs):
        self.name = name
        self.habitat = habitat
        self.legs = legs

    def display_info(self):
        print(f"{self.name} is a {self.habitat} animal.")
        if self.legs == 0:
            print(f"It has no legs.")
        else:
            print(f"It has {self.legs} legs.")

snake = Petshop("Snake", "terrestrial", 0)
snake.display_info()

fish =Petshop("Fish", "aquatic", 0)
fish.display_info()

dog = Petshop("Dog", "terrestrial", 4)
dog.display_info()

frog = Petshop("Frog", "aquatic", 4)
frog.display_info()
