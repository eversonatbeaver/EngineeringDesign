def make_star():
	print("")
	print("       \****__              ____          ")                                  
	print("         |    *****\_      --/ *\-__       ")                                 
	print("         /_          (_    ./ ,/----'      ")                                 
	print("           \__         (_./  /             ")                                 
	print("              \__           \___----^__    ")                                 
	print("               _/   _                  \   ")                                 
	print("        |    _/  __/ )\ \ _____         *\ ")                                 
	print("        |\__/   /    ^ ^       \_________| ")

number_of_stars = input("How many stars? ")

if number_of_stars > 0:
	for x in range(0, number_of_stars):
		make_star()
	print("")
else:
	print("There must be a valid number")
