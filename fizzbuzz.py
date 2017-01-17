
def fizz_buzz(fbval):
    if type(fbval) is int:
        three_mod = fbval % 3;
        five_mod = fbval % 5;
        
        if three_mod == 0 and five_mod == 0:
            #divisible by both three and five
            return "FizzBuzz"
        elif three_mod > 0 and five_mod > 0:
            #not divisible by both three and five
            return fbval
        elif three_mod == 0:
            #only divisible by three
            return "Fizz"
        else:
            #only divisible by five
            return "Buzz"
    else:
        raise ValueError("This funciton only accepts integer values")


