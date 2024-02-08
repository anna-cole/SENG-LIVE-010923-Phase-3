import ipdb

# 7. ✅. Create a subclass of Pet called Cat
    
    # import Pet from lib.pet
from lib.pet import Pet

  # 8. ✅. Create Cat class + __init__ that takes all the parameters from Pet and an
# additional parameter called indoor (Boolean)

class Cat(Pet):
  
    def __init__(self, name, age, breed, temperament, indoor):
    
    # self.name = name
    # self.age = age
    # self.breed = breed
    # self.temperament = temperament
    # self.indoor = indoor

    # Use super to pass the Pet parameters to the super class. Following DRY principle, reduce code redundancy. YOu can only use super because Cat class is an inheritance (subclass) of the Pet class. 
        # super() => Pet class
        super().__init__(name, age, breed, temperament)
    
    # Add an indoor attribute
        self.indoor = indoor

# ipdb.set_trace()

# 9. ✅. Create a method unique to the Cat subclass called talk which returns the string "Meow!" DON'T FORGET THE SELF PARAMETER. This will only gonna work for the cat instances, not pet instances

    def talk(self):
      print("Meow!")

# ipdb.set_trace()

# 10. ✅. Create a method called print_pet_details to match the print_pet_details in Pet    
        
        # Add super().print_pet_details() and print the indoor attribute
      
    def print_pet_details(self):
        # Inherited behaviors from Pet class
        # super() => Pet class
        super().print_pet_details()
        
        print(f'''
            indoor: {self.indoor}
        ''')