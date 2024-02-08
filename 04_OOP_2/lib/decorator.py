# Decorators - reduce redundancy within classes
# Inheritance - reduce redundancy across classes

# 1. ✅ First Class Functions
# "[We can] assign them to variables, store them in data structures, pass them as arguments
# to other functions, and even return them as values from other functions."
# See more => http://bit.ly/3YQh8KR

# my_variable = '123'
# my_variable = def 

    # Create functions to be used as callbacks 

# def walk(pet):
#   print(f'{pet} has been walked!')

# def feed(pet):
#   print(f'{pet} has been fed!')

    # Create a higher-order function that will take a callback as an argument

# Higher Order Function => Accepts a callback function as parameter and executes this function inside   
# def execute_task(func):
  
#   # Callback function invocation
#   return func("Rose")

# execute_task(walk)
# execute_task(feed)

# 2. ✅ Create a higher-order function that returns a function. If you print the invocation of this high-order function and run the script, you will see the function returning the feed function.

# def execute_task():
#   def feed(pet):
#     return f'{pet} has been fed!'
#   return feed

# print(execute_task()) # feed function reference

# Now change return to print and execute the high order function passing the pet argument.

# def execute_task():
#   def feed(pet):
#     print(f'{pet} has been fed!')
  
#   return feed
  # return feed, walk => returns a tuple with function references


# execute_task() => feed function reference. It's not invoking feed, it's just referencing it. You need to pass an argument to it so it can be invoked.
# execute_task()('Rose')

# Or you ca do:

# feed = execute_task()
# feed('Rose')

# 3. ✅ Decorator

# Create a function that:
    # - takes a (callback) function as an argument
    # - has an inner function defined, which executes the callback function
    # - returns the inner function

# Tools:

    # .format() => method (string)
    # https://www.geeksforgeeks.org/python-string-format-method/

    # .round() => format actual calculation of discount
    # https://www.geeksforgeeks.org/round-function-python/

# Decorator
def coupon_calculator(func):
  
  #Inner function
    def report_price():
        print(f"Initial price = $35.00")
        final_price = func(35.00)
        print(f"Newly discounted price = ${final_price}")
        # breakpoint()
    
    return report_price 

# Callback function to calculate new price
def calculate_price(price):

    # We end up with a floating point number rounded to the nearest hundreth
    # .2f => two decimal point floating number
    # return '{:.2f}'.format(price / 2)
    return '{:.2f}'.format(round(price / 2, 2))


# Try using a decorator with / without pie syntax '@'

# Without pie syntax 

# report_price = coupon_calculator(calculate_price)
# report_price()
# # or
# coupon_calculator(calculate_price)()

# With pie syntax

# @coupon_calculator
# def calculate_price(price):
#     return '{:.2f}'.format(round(price / 2, 2))

# calculate_price()

# @coupon_calculator
# def other_function(price):
#     return '{:.2f}'.format(price / 3)

# other_function()