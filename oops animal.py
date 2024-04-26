class Animal:
    def __init__(self, cat, dog, hen, snake, legs):
        self.animal_cat=cat
        self.animal_dog=dog
        self.animal_hen=hen
        self.animal_snake=snake
        self.animal_legs=legs
        
        
    def sound(self):
        print(f"{self.animal_cat}is meow meow")
        print(f"{self.animal_dog}is bow bow")
        print(f"{self.animal_hen}is khooo khooo")
        print(f"{self.animal_snake}is shhhhhhh")
    
    
    def legs(self):
        print(f"{self.animal_legs}")
        
cat=Animal("cat 4 legs ",4)
dog=Animal("dog 4 legs ",4)
hen=Animal("hen 2 legs ",2)
snake=Animal("snake 0 legs ",0)

cat.legs()
cat.sound()
dog.legs()
dog.sound()
hen.legs()
hen.sound()
snake.legs()
snake.sound()