class safe_divide:
    def __init__(self)#, numerator, denominator):
       # self.numerator = numerator
       # self.denominator = denominator

    def safe_divide(numerator,denominator):
        try:
           result= numerator/denominator



        except ZeroDivisionError:
            print("cannot divid by zero")
        except ValueError:
            print("undifine value") 
            return   
        else:
            print(result)