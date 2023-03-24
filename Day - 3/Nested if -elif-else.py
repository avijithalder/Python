print("Welcome to the Rollercoaster !")

height=int(input("What is your height ?\n"))
age=int(input("What is your age ?\n"))
if(height >= 120):
  print("your can ride")
  if (age<12):
   print("Pay $20")
  elif (age <= 18):
    print("Pay $15")
  else:
    print("pay $10")
else:
  print("Sorry,You can't ride\n")


  
  
