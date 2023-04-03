#test classes


#create timezone class
class ClockTimeZone:
    def __init__(self, country, city):
        self.country = country
        self.city = city
        self.citycode = ""
        self.timezonecode = ""
    
    def __str__(self):
        return f"Time in {self.city},{self.country} is TBD"
    
    def findOffset(self):
        return 1
    
    def timeAtLoc(self):
        return 1
    
    
hometown = ClockTimeZone("Belgium", "Hasselt")

print(hometown)
print(hometown.timeAtLoc())