class Animal:
    def speak(self):
        pass
    
class Dog(Animal):
    def speak(self):
        return "woof!"
    
class Cat(Animal):
    def speak(self):
        return "meow!"
    
class Sindhi(Animal):
    def speak(self):
        return "satpatdudum!"

class Dummi(Animal):
    def speak(self):
        return "abadiiii!"

def make_Animal_speak(animal):
    print(animal.speak())

dog=Dog()
cat=Cat()
sindhi=Sindhi()
dummi=Dummi()
make_Animal_speak(dog)
make_Animal_speak(cat)
make_Animal_speak(sindhi)
make_Animal_speak(dummi)    
    