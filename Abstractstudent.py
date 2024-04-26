from abc import ABC, abstractmethod

class AbstractStudent(ABC):
    def __init__(self, branch, rno, marks):
        self.branch=branch
        self.rno=rno
        self.marks=marks
        
    @abstractmethod
    def display_details(self):
        pass