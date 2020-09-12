def nth_power(power):  #Main function behave as a class
    def ofNumber(base): # Nested function
        #print(power*base)
        return pow(base,power)
    return ofNumber # closure



cube= nth_power(3)
del nth_power
#sq= nth_power(2)
print(cube(2))