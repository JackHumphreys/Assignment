wieght = int(input("Please enter weight: "))

grams_mod_100 = int(wieght%100)
grams_div_100 = int(wieght/100)

grams_mod_50 = int(grams_mod_100%100)
grams_div_50 = int(grams_mod_100/100)

grams_mod_10 = int(grams_mod_50%10)
grams_div_10 = int(grams_mod_50/10)

grams_mod_5 = int(grams_mod_10%5)
grams_div_5 = int(grams_mod_10/5)

grams_mod_2 = int(grams_mod_5%2)
grams_div_2 = int(grams_mod_5%2)

grams_mod_1 = int(grams_mod_2%1)
grams_div_1 = int(grams_mod_2/1)

print("Balanced weight- 100g: {0}, 50g: {1}, 10g: {2}, 5g: {3}, 2g: {4}, 1g: {5}".format(grams_div_100, grams_div_50, grams_div_10, grams_div_5, grams_div_2, grams_div_1))

