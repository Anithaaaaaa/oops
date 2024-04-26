class Bike:
    def __init__(self,name,cc):
        self.bike_name=name
        self.bike_cc=cc
        
    def Type(self):
        if self.bike_cc<200:
            print(f"{self.bike_name}is normal bike")
        else:
            print(f"{self.bike_name} is superbike")
        
Duke=Bike("RC390",390)
RE=Bike("classic350",350)
Hero=Bike("splendor",110)

b=input(" Enter the bike:")
if b=="Duke":
    Duke.Type()
elif b=="RE":
    RE.Type()
else:
    Hero.Type()