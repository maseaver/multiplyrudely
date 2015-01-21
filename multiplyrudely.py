import sys

intro = "I can multiply two integers together.\nNo funny business with spelling them out though. I can't read words.\nAnd it's gonna get weird if you make them too big. "
prompt = "Gimme an integer. "
success = "Good job! "
error = "Fuck you, asshole. "
surrender = "I give up!"
result = "The product is "


def is_integer( s ):
    try:
        int( s )
        return True
    except ValueError:
        return False

def query( ):
    factor = raw_input( prompt )
    attempts = 0

    if is_integer( factor ):
        print success
        return int( factor )

    else:  
        while is_integer( factor ) == False and attempts < 9:
            print error
            factor = raw_input( prompt )
            attempts = attempts + 1

        if attempts >= 9 and is_integer( factor ) == False:
            print surrender
            sys.exit(0)

        else:
            print success
            return int( factor )

if __name__ == '__main__':
    # only execute this stuff at runtime, rather than import time.

    print intro
    factor1 = query( )
    factor2 = query( )
    product = factor1 * factor2

    print result + str( product ) + "."
