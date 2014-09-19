#Jack Humphreys
#Garden Area Exercise
#16/09/2014

garden_length = float(input("Please enter length in metres: "))
garden_width = float(input("Please enter width in metres: "))

area = float(garden_length*garden_width)

price = float(input("Please enter price per square metre: "))

print("The cost of turfing: {0}".format(area*price))
