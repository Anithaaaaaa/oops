class Location:
    def __init__(self, longitude, latitude):
        self.longitude=longitude
        self.latitude=latitude
        
    def __add__(self,other):
        return (f"{self.longitude+other.longitude},{self.latitude+other.latitude}")
    
    def __eq__(self,next):
        return (f"{self.longitude+next.longitude/2},{self.latitude+next.latitude/2}")
    
l1=Location(1234,-1432)
l2=Location(123,-143)
print(l1+l2)

a=1234
b=-1432
c=123
d=-143
l3=(a+c)/2
l4=(b+d)/2
print(l3+l4)
