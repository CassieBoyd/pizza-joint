"""
Create a Pizza type for representing pizzas in Python. Think about some basic properties that would define a pizza's values; things like size, crust type, and toppings would help. Define those in the __init__ method so each instance can have its own specific values for those properties.
"""

class Pizza:
    def __init__(self):
        self.crust = ""
        self.size = ""
        self.toppings = []
        self.sauce = ""
    def add_toppings(self, topping):
        self.toppings.append(topping)
    def print_order(self):
        if len(self.toppings) == 1:
            print(f"I would like a {self.size}-inch, {self.crust} pizza with {''.join(self.toppings)}.")

        # If more than one topping, .join method is used on toppings list 
        elif len(self.toppings) > 1:
            print(f"I would like a {self.size}-inch, {self.crust} pizza with {', '.join(self.toppings[:-1])} and {self.toppings[-1]}")

# https://stackoverflow.com/questions/44574485/joining-words-together-with-a-comma-and-and/44574565
            # print("I would like a {}-inch, {} pizza with {} and {}".format(self.size, self.crust,', '.join(self.toppings[:-1]), self.toppings[-1]))


            
            # print(f"I would like a {self.size}-inch, {self.crust} pizza with {' and '.join(self.toppings)}")
            # print(*self.toppings, sep = ", ")
            
            # sentence = f"I would like a {self.size}-inch, {self.crust} pizza with "
            # print(f"I would like a {self.size}-inch, {self.crust} pizza with {' and '.join(self.toppings)}")
            
            # {*self.toppings, sep = " and "}

"""
Add a method for interacting with a pizza's toppings, called add_topping.
"""


"""
Add a method for outputting a description of the pizza (sample output below).

"I would like a 16-inch, deep-dish pizza with Pepperoni and Olives."
"""


meat_lovers = Pizza()
meat_lovers.size = 16
meat_lovers.crust = "Deep dish"
meat_lovers.add_toppings("Pepperoni")
meat_lovers.add_toppings("Olives")
meat_lovers.add_toppings("Mushrooms")
meat_lovers.add_toppings("Pineapple")
meat_lovers.print_order()  
