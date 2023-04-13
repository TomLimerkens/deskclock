from dataclasses import dataclass
#define person

class Person:
    #initialise object
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name
    
    #print format
    def __str__(self) -> str:
        return f'first_name:"{self.first_name}",last_name:"{self.last_name}"'
    

@dataclass
class DcPerson:
    firstname : str
    lastname : str
    year : int = 2023
    street : str = ""
    city : str = ""

    def __str__(self) -> str:
        return f'{self.firstname},{self.lastname},{self.year},{self.street},{self.city}'
        

    def __init__(self, firstname: str, lastname : str, year : int = 2023, street : str = "", city : str = "") -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.year = year
        self.street = street
        self.city = city
    
#test implementation
p1 = DcPerson('Tom', 'Limerkens', 1976, 'Oeverstraat', 'Hasselt')
p2 = DcPerson('Jean','Limerkens', 1952, 'Venhovenstraat', 'Gruitrode')

print(f'P1 = {p1}')
print(f'P2 = {p2}')



p = Person('Tom','Limerkens')

print(p)