#Write a program that asks the user to enter a mass in medieval units: talents (leiviskä), pounds (naula), and lots (luoti). The program converts the input to full kilograms and grams and outputs the result to the user:

#One talent is 20 pounds.
#One pound is 32 lots.
#One lot is 13,3 grams.

talent_str = input("enter talents: ")
pounds_str = input("enter pounds: ")
lots_str = input("enter lots: ")

talent_to_gr = (20 * 32 * 13.3) * float(talent_str)
pound_to_gr = (32 * 13.3) * float(pounds_str)
lot_to_gr = 13.3 * float(lots_str)

result = (float(talent_to_gr) + float(lot_to_gr) + float(pound_to_gr))
kilo = int(result / 1000)
grams = float(result) - int(kilo * 1000)
#print("the weight in modern units: " + )
print(result)
print("the weight in modern units: " + str(kilo) + " kilograms " + f"and{grams: .2f}" + " grams")

