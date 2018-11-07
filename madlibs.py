"""
This program is an example of Mad Libs word game on Codecademy.
Author: Ozge
"""

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."
STORY2 = "Roses are %s. %s are blue. I love %s."
print ("Mad Libs is starting!")
choice = input("Choose a story; 1 or 2? :")
if choice == "1":
	print ("you chose first story")
	name = input("Enter a name: ")
	adj1 = input("Tell me an adjective, and click enter. ")
	adj2 = input("Tell me an adjective, and click enter. ")
	adj3 = input("Tell me an adjective, and click enter. ")
	verb = input("Tell me a verb, and click enter. ")
	noun1 =input("Tell me a noun, and click enter. ")
	noun2 =input("Tell me another noun, and click enter. ")
	animal =input("Enter an animal: ")
	food = input("Enter a food: ")
	fruit = input("Enter a fruit: ")
	superhero = input("Enter a superhero: ")
	country = input("Enter a country: ")
	dessert = input("Enter a dessert: ")
	year = input("Enter a year: ")
	print (STORY % (name, adj1, adj2, animal, food, verb, noun1, fruit, adj3, name, superhero, name, country, name, dessert, name, year, noun2))
elif choice == "2":
	print ("you chose second story")
	color = input("Enter a color :")
	plural_noun = input("Enter a plural noun :")
	famous_person = input("Enter a your favorite famous person :")
	print (STORY2 % (color, plural_noun, famous_person))

else:
	print("You didnt make any choice:(")














