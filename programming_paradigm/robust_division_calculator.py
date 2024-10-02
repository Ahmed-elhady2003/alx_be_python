class safe_divide:
    def __init__(self)

    def safe_divide(float(numerator),float(denominator)):
        try:
           result= numerator/denominator



        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
        except ValueError:
            print("Error: Please enter numeric values only.") 
            return   
        else:
            return result