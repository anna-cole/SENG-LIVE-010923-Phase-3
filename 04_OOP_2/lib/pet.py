#!/usr/bin/env python3
# Class Attributes and Methods 

import ipdb

class Pet:

# 4. ✅ Define a class attribute (total_pets) and set it to 0

    # Class Attribute. You get this by Pet.total_pets (from the class) or fido.total_pets (from the instance) in the breakpoint()
    total_pets = 0

    # What happens with our instances when we update a class attribute? It updates the instance too. Pet.total_pets += 1 will increment the class attribute and also the instance fido.total_pets will be 1

    def __init__(self, name, age, breed, temperament):
        self.name = name
        self.age = age
        self.breed = breed
        self.temperament = temperament

        # Without class method
        # Pet.total_pets += 1
        
        # With class method
        Pet.increase_pets()

# ipdb.set_trace()

# 5. ✅. Update the class attribute whenever an instance is initialized

# 6. ✅. Create a class method increase_pets that will increment total_pets
    
    # replace Pet.total_pets += 1 in __init__ with increase_pets()
        
    # Instance Method
    def print_pet_details(self):
        print(f'''
            name:{self.name}
            age:{self.age}
            breed:{self.breed}
            temperament:{self.temperament}
        ''')

    # Class Method
        
    @classmethod # Step 1 keyword
    def increase_pets(cls): # Step 2 cls parameter (it's analogous to self in the instance method)
        cls.total_pets += 1

        # Perform other behaviours
        print('One new pet added')

# ipdb.set_trace()