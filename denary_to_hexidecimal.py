#Jack Humphreys
#18/09/2014
#Hexidecimal Exercise

denary_value = int(input("Please enter denary number: "))

binary_string = ""

while denary_value > 0 :
    binary_string = str(denary_value%2)+binary_string
    denary_value = (denary_value//2)



print("Your binary equivalent is: {0}".format(binary_string))



