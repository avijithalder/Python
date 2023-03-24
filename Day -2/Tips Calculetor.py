#tip calculetor 

print("Welcome to the tip calculator.\n") #normal print

bill=float((input("What was the total bill ?\n$"))) #input bill in float type

tip=int((input("What Percentage tip would you like to give ? 10, 12, or 15?\n"))) #input tip in integer type

people=int(input("How many people to split the bill ?\n")) #input people in int type


calculate= (((tip / 100) * bill) + bill) #calculation
total = round((calculate)/people,2)  #,2 mens how many number need after .0000

print("Each person should pay : \n$",total)  #print total 
