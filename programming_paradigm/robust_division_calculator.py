class safe_divide:
    def __init__(self)#, numerator, denominator):
       # self.numerator = numerator
       # self.denominator = denominator

    def safe_divide(numerator,denominator):
        try:
           result= numerator/denominator



        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
        except ValueError:
            print("Error: Please enter numeric values only.") 
            return   
        else:
            return result