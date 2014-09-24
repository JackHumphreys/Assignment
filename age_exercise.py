age = int(input("How old are you? "))
if age >= 18:
          print("You can vote!")
else:
          print("You can't vote")

print("You are {0} years away from retiring.".format(65-age))

