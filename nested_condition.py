x = int(input("Enter a number: "))
if x % 2  == 0:
  print("Even")
else:
  print("Odd")
  if x % 3:
    print("And not divisible by 3")