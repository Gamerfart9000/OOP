class Dog:
    
    species = "Canis familiaris"

    
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    
    def details(self):
        print("Name:", self.name)
        print("Breed:", self.breed)
        print("Species:", Dog.species)
       



dog1 = Dog("Tyson", "Golden Retriever")
dog2 = Dog("Rocky", "German Shepherd")


dog1.details()
dog2.details()