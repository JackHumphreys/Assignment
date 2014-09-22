#Jack Humphreys
#Swimming Pool Volume
#22/09/2014

length = float(input("Please enter length of pool in metres: "))
width = float(input("Please enter width of pool in metres: "))
maximum_depth = float(input("Please enter maximum depth of pool in metres: "))
minimum_depth = float(input("Please enter minimum depth of pool in metres: "))

volume = (length*width*(maximum_depth*minimum_depth)/2)
print("Volume of pool in cubic metres is: {0}".format(volume))
print("Litre of water to fill the pool is: {0}".format(volume*1000))
