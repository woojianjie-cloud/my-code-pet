# Define a class called Pet
# A class is like a blueprint for creating objects
class Pet:
    
    # This method runs automatically when a new Pet is created
    # It sets up the pet's name, species, and starting happiness
    def __init__(self, name, species):
        self.name = name          # Store the pet's name
        self.species = species    # Store the pet's species
        self.happiness = 50       # Set starting happiness level
    
    # This method displays the pet's current statistics
    def stats(self):
        print("name:", self.name)
        print("Species:", self.species)
        print("Happiness:", self.happiness)
    
    # This method increases happiness when the pet is fed
    def feed(self):
        self.happiness = self.happiness + 10
        print("Pet is eating")
        print("Happiness is now:", self.happiness)
    
    # This method increases happiness when the pet plays
    def play(self):
        self.happiness = self.happiness + 25
        print("Pet is playing")
        print("Happiness is now:", self.happiness)
    
    # This method decreases happiness when the pet gets sick
    def sick(self):
        self.happiness = self.happiness - 25
        print("Pet is sick")
        print("Happiness is now:", self.happiness)
    
    # This method slightly increases happiness when medicine is given
    def medi(self):
        self.happiness = self.happiness + 3
        print("Pet is sick")
        print("Happiness is now:", self.happiness)

# Create a Pet object named "cat"
# "Sunbeam" is the pet's name and "maker" is the species
cat = Pet("Sunbeam", "maker")

# Call different methods to interact with the pet
cat.stats()
cat.play()
cat.feed()
cat.sick()
cat.sick()
cat.medi()
cat.play()
