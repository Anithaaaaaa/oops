class Student:
    def __init__(self,name,rno):
        self.student_name = name
        self.student_rno = rno
        
    def display_info(self):
        print(f"student name{self.student_name}, and studentr no{self.student_rno}")
        
class details(Student):
    def __init__(self, name, rno, marks):
        super().__init__(name, rno)
        self.student_marks = marks
        
    def display_info(self):
        super().display_info()
        print(f"marks she obtained {self.student_marks}")
        
user = details("anitha", "3", "97")
user.display_info()