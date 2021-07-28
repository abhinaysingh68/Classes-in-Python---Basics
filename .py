# Classes-in-Python---Basics

class Car:
    def __init__(self, windows,door,enginetype,tyre):
        self.windowCount=windows
        self.doorCount=door
        self.engine=enginetype
        self.tyreType=tyre
        self.totalDoor=door+1
    def tyre_desc(self, tyrewidth):
        self.tyreWidth=tyrewidth
        return ("This car has {} tyres.".format(self.tyreType))+(" Tyre width is {} inches.".format(self.tyreWidth))


car1=Car(4,5,"Petrol","Tubless")

car2=Car(2,3,"Diesel","Tube")


#Print
car2.totalDoor


#Print
car1.tyre_desc(8)



class WW(Car):
    def __init__(self,windows,door,enginetype,tyre, ai, hybrid):
        super().__init__(windows, door, enginetype, tyre)
        self.aiAvailable=ai
        self.hybridEngine=hybrid
    def hybridInfo(self):
        return ("This car runs on {} technologies".format(self.aiAvailable)) + (" and has {} engine").format(self.hybridEngine)


ww1=WW(4,5,"Mix","Tubeless","AI", "Hybrid")
ww2=WW(2,3,"Mix","Tubeless","AI", "Non Hybrid")

#Print
ww1.tyre_desc(8)


#Print
ww2.tyreType


#Print
ww2.hybridInfo()






