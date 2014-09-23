import math

width = float(input("Please enter width of pool: "))
length = float(input("Please enter length of pool: "))
depth = float(input("Please enter depth of pool: "))

main_section_volume = float(length*width*depth)
circle_radius = float(width/2)
circle_area = float(math.pi*(circle_radius*circle_radius))
half_circle_volume = float((circle_area/2)*depth)

pool_volume = float(main_section_volume+half_circle_volume)

print("The volume of the pool is: {0}".format(pool_volume))
