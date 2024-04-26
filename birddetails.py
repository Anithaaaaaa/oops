class birds:
    def __init__(self, name, color, size, legs):
        self.name = name
        self.color = color
        self.size = size
        self.legs = legs

    def print_features(self):
        
        print("The", self.name, "is", self.color, "in color.")
        print("It is", self.size, "in size and has", self.legs, "legs.")
        if self.legs != 0:
            print(f"it can fly")
        else:
            print(f"It cant fly") 

peacock= birds("peacock", "bule", "large", 2)
peacock.print_features()
crow=birds("crow","black","small",2)
crow.print_features()