weight=float(input("Enter Your Weight in kg\n"))
height=float(input("Enter Your height in m\n"))

bmi= round(weight/ height ** 2)

if bmi<18.5:
  print("Your bmi is {bmi},You are underweight")
elif bmi<25:
  print("Your bmi is {bmi},You have a normal weight")
elif bmi<30:
  print("Your bmi is {bmi},You are overweight")
elif bmi<35:
  print("Your bmi is {bmi},You are obese")
else:
  print("Your bmi is {bmi},You are clinically obese")

  
  
