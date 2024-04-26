#encapsulation
class Student:
    def __init__(self,name,roll_number,password):
            self.name=name #public atribute
            self._roll_number=roll_number #protected attribute
            self.__password=password     #private attribute
            
    def display_details(self):
        print("name:", self.name)
        print("roll_number:", self._roll_number)
        print("passwor:", self.__password)
        
    def get_password(self):     #getter method
        return self.__password
    
    def set_password(self, new_password):
        self.__password = new_password
             
student = Student("Allice", "A001", "secure_password")
print("name (public):", student.name)
print("roll number (protected):", student._roll_number)
print("password (private):", student.get_password())

student.set_password("new_password")
student.display_details()