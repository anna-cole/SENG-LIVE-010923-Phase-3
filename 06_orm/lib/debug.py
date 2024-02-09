#!/usr/bin/env python3

from owner import Owner, CONN, CURSOR
from pet import Pet, CONN, CURSOR

Owner.create_table()
frank = Owner("frank", "555-555-5555", "frank@gmail.com", "555 Somewhere St.")
frank.save()

ana = Owner.create("ana", "3434343", "ana@gmail.com", "123 St")

# Pet.create_table()
# spot = Pet("spot", "dog", "chihuahua", "feisty")
# spot.save()

# or 
# Pet.create("spot", "dog", "chihuahua", "feisty")
# This will instantiate the instance and persist in the DB

# This method is 2 in 1: it will create and save at the same time
# Pet.create("grace", "cat", "siamese", "mysterious")

import ipdb; ipdb.set_trace()
