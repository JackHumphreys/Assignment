#Jack Humphreys
#Minimum Currency amount
#19/09/2014

currency_1 = int(input("Please enter amount in pounds: "))

c_twenty = currency_1%20
c_twenty_1 = currency_1//20

c_ten = c_twenty%10
c_ten_1 = c_twenty//10

c_five = c_ten%5
c_five_1 = c_ten//5

c_two = c_five%2
c_two_1 = c_five//2

c_one = c_two%1
c_one_1 = c_two//1

print("Minimum amount of notes and coins - £20's: {0}, £10's: {1}, £5's: {2}, £2's: {3}, £1's: {4}".format(c_twenty_1, c_ten_1, c_five_1, c_two_1, c_one_1))
