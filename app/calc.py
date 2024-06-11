import app
from math import sqrt
from math import log10

class InvalidPermissions(Exception):
    pass

class Calculator:
    def add(self, x, y):
        self.check_types(x, y)
        return x + y

    def substract(self, x, y):
        self.check_types(x, y)
        return x - y

    def multiply(self, x, y):
        self.check_types(x, y)
        return x * y

    def divide(self, x, y):
        self.check_types(x, y)
        if y == 0:
            raise TypeError("Division by zero is not possible")

        return x / y

    def power(self, x, y):
        self.check_types(x, y)
        return x ** y

    def check_types(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Parameters must be numbers")
       
    def sqrt(self, x):
        self.check_type(x)
        if x < 0:
            raise TypeError("Square of negative numbers it's not posible on real numbers.")
        return sqrt (x) 
    
    def logbase10(self, x):
        self.check_type(x)
        if x < 0:
            raise TypeError("Log base 10 for negative numbers is not possible")
        if x == 0:
            raise TypeError("Log base 10 for 0 is infinite")
        return log10(x) 
        
    def check_types(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Parameters must be numbers")

    def check_type(self, x):
        if not isinstance(x, (int, float)):
            raise TypeError("Parameter must be number")

