###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

def exponent(base, power):
    if power == 0:
        return 1
    return base * exponent(base, power - 1)


print(exponent(3, 4))
