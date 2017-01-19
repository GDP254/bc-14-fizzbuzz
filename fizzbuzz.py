
def fizz_buzz(fbval):
    if type(fbval) is int:
        print "Check if value has a remainder when divided by 3"
        three_mod = fbval % 3;
        print "Check if value has a remainder when divided by 5"
        five_mod = fbval % 5;
        
        print "if division by both 3 and 5 does not provide a remainder:"
        print " FizzBuzz"
        print "else if both operations provide remainders:"
        print " return value"
        print "else if only division by 3 does not provide a remainder:"
        print " Fizz"
        print "else (only division by 5 does not provide a remainder):"
        print " Buzz"
        
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


