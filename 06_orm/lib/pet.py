# Pet Attributes: 
# name: TEXT 
# species: TEXT
# breed: TEXT 
# temperament: TEXT

# https://docs.python.org/3/library/sqlite3.html#tutorial
import sqlite3

# https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection
CONN = sqlite3.connect('lib/resources.db')

# https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor
CURSOR = CONN.cursor()

class Pet:

    # ✅ 1. Add "__init__" with "name", "species", "breed", "temperament", and "id" (Default: None) Attributes
    # We need to make sure we create the instances before persisting them on the DB

    def __init__(self, name, species, breed, temperament, id=None):
        self.name = name
        self.species = species
        self.breed = breed
        self. temperament = temperament
        self.id = id

    # ✅ 2. Add "create_table" Class Method to Create "pets" Table If Doesn't Already Exist. Pet class => pets table. It will be a class method, not an instance method. It would be wrong to call this from an instance, i.e. spot.create_table(), makes more sense to create this table from the class rather than from the instance Pet.create_table()
        
    @classmethod
    def create_table(cls):
        sql = '''
            CREATE TABLE IF NOT EXISTS pets 
                (id INTEGER PRIMARY KEY,
                name TEXT,
                species TEXT,
                breed TEXT,
                temperament TEXT)
        '''
        CURSOR.execute(sql)

    # ✅ 3. Add "drop_table" Class Method to Drop "pets" Table If Exists
        
    @classmethod
    def drop_table(cls):
        sql = '''
            DROP TABLE IF EXISTS pets
        '''
        CURSOR.execute(sql)

    # ✅ 4. Add "save" Instance Method to Persist New "pet" Instances to DB
        
    def save(self):
        sql = '''
            INSERT INTO pets (name, species, breed, temperament)
            VALUES (?, ?, ?, ?)
        '''
        CURSOR.execute(sql, (self.name, self.species, self.breed, self.temperament))
        
    # ✅ 5. Add "create" Class Method to Initialize and Save New "pet" Instances to DB
        
        # Repeated action that we're abstracting out into 'create'

    @classmethod
    def create(cls, name, species, breed, temperament):
        
        # This is the __init__ method for a class method that instantiates
        # Create instance of pet class
        pet = cls(name, species, breed, temperament)
        #or pet = Pet(name, species, breed, temperament)
        
        # Persist instance to DB
        pet.save()

        return pet

    # ✅ 6. Add "new_from_db" Class Method to Retrieve Newest (latest) "pet" Instance w/ Attributes From DB

    @classmethod
    # row here is a tuple (id, name, etc)
    # this method recreates the object from the tuple of records (row) coming from the DB
    def create_instance(cls, row):

        # Reinstantiating the instance of the Pet Class 
        pet = cls(
            id = row[0],
            name = row[1],
            species = row[2],
            breed = row[3],
            temperament = row[4]
        )
        return pet

    # ✅ 7. Add "get_all" Class Method to Retrieve All "pet" Instances From DB

    @classmethod
    def get_all(cls):
        sql = '''
            SELECT * FROM pets
        '''
        # This will return a list of rows, use the class method new_from_db to convert the row to instance and return the instance. 
        return [cls.create_instance(row) for row in CURSOR.execute(sql).fetchall()]
        

    # ✅ 8. Add "find_by_name" Class Method to Retrieve "pet" Instance by "name" Attribute From DB

        # If No "pet" Found, return "None"
    
    @classmethod
    def find_by_name(cls, name):
        sql = '''
            SELECT * FROM pets
            WHERE name = ?
            LIMIT 1
        '''
        row = CURSOR.execute(sql, (name,)).fetchone()
        
        if not row:
            return None
        # Instantiate Pet class with Tuple value (row) and pass it to a function that converts it to instance
        return cls.create_instance(row)


    # ✅ 9. Add "find_by_id" Class Method to Retrieve "pet" Instance by "id" Attribute From DB

        # If No "pet" Found, return "None"
    
    @classmethod
    def find_by_id(cls, id):
        sql = '''
            SELECT * FROM pets
            WHERE id = ?
            LIMIT 1
        '''
        row = CURSOR.execute(sql, (id,)).fetchone()
        
        if not row:
            return None
        # Instantiate Pet class with Tuple value (row) and pass it to a function that converts it to instance
        return cls.create_instance(row)

    # ✅ 10. Add "find_or_create_by" Class Method to:

        #  Find and Retrieve "pet" Instance w/ All Attributes

        # If No "pet" Found, Create New "pet" Instance w/ All Attributes
    
    # Pet.find_or_create_by('grace', 'cat', 'siamese', 'mysterious')
        # If we find a record, return that record expressed as a Python object
        # If we don't, instantiate / persist the new pet object
    
    @classmethod
    def find_or_create_by(cls, name=None, species=None, breed=None, temperament=None):
        instance = cls.find_by_name(name)
        
        if not instance:
            cls.create(name, species, breed, temperament)
            return Pet.find_by_name(name)
            # or
            # new_instance = cls.create(name, species, breed, temperament)
            # return (new_instance).name
            
        return instance

    # Or

    # @classmethod
    # def find_or_create_by(cls, name=None, species=None, breed=None, temperament=None):
    #     sql = """
    #         SELECT * FROM pets
    #         WHERE (name, species, breed, temperament) = (?, ?, ?, ?)
    #         LIMIT 1
    #     """
    #     row = CURSOR.execute(sql, (name, species, breed, temperament)). fetchone()

    #     if not row:
    #         sql = '''
    #             INSERT INTO pets (name, species, breed, temperament)
    #             VALUES (?, ?, ?, ?)
    #         '''
    #         CURSOR.execute(sql, (name, species, breed, temperament))

    #         return Pet.find_by_name(name)
        
    #     return Pet.create_instance(row)

    # ✅ 11. Add "update" instance method to Find "pet" Instance by "id" and Update All Attributes
    # spot.name = 'new name'
    # spot.breed =  'new breed'
    # spot.update()
    
    def update(self):
        # Note that we dont have to pass an id as argument, because the method has access to the id through the instance via self. 
        
        sql = '''
            UPDATE pets
            SET name = ?,
                species = ?,
                breed = ?,
                temperament = ?
            WHERE id = ?
        '''
        CURSOR.execute(sql, (self.name, self.species, self.breed, self.temperament, self.id))



