#Exceptions in Python
class month_to_season:
    def set_month(self):
        self.month = int(input("Enter the number of the month:"))       #Typecast to int
        try:
            if self.month < 1 or self.month > 12:
                raise ValueError                #Raise exception
            else:
                return True
        except ValueError:                      #Handle exception
            print(self.month,"is not a valid Month number. Please try again")
            return False

    def show_season(self):
        season = ["Spring","Summer","Autumn","Winter"]
        if self.month < 4:
            print("It is ", season[0])
        elif self.month >=4 and self.month < 8:
            print("It is ", season[1])
        elif self.month >=8 and self.month < 11:
            print("It is ", season[2])
        elif self.month >10:
            print("It is ", season[3])

Seasons = month_to_season()
while Seasons.set_month() != True:  #Evaluate return value as condition
    pass                            #Define empty while loop
Seasons.show_season()               #Define statement outside of while

        
#Multiple exception examples
try:
    a = 20
    b = a/0
except ZeroDivisionError:
    result = "ZeroDivisionError"
except Exception:
    result = "Exception"
    print("Reached end of except.")
except BaseException:
    result = "BaseException"
finally:
    print("Exception:",result)      #Output: Exception: ZeroDivisionError


#Order of exception execution matters
try:
    if result: del result
    a = 20
    b = a/0
except BaseException:
    result = "BaseException"
except ZeroDivisionError:
    result = "ZeroDivisionError"
except Exception:
    result = "Exception"
finally:
    print("Exception:",result)      #Output: Exception: BaseException


#Else in exception
try:
    if result: del result
    a = 20
    b = a/5
except ZeroDivisionError:
    result = "ZeroDivisionError"
except Exception:
    result = "Exception"
except BaseException:
    result = "BaseException"
else:
    result = b
finally:
    print("Exception/Result:",result)      #Output: Exception/Result: 4.0



