
print("------------------------CALCULATOR------------------------ ")
while True:
   print("----------1. Addition----------")
   print("----------2. Subtraction----------")
   print("----------3. Multiplication----------")
   print("----------4. Division----------")
   print("----------5. Exit----------")
   print("Enter Your Choice (1-5): ", end="")
   choice = int(input())
   if choice>=1 and choice<=4:
      print("\nEnter Two Numbers: ", end="")
      num1 = float(input())
      num2 = float(input())
   if choice==1:
      res = num1 + num2
      print("\nResult =", res)
   elif choice==2:
      res = num1 - num2
      print("\nReults =", res)
   elif choice==3:
      res = num1 * num2
      print("\nResult =", res)
   elif choice==4:
      res = num1 / num2
      print("\nResult =", res)
   elif choice==5:
      break
   else:
      print("\nInvalid Input!..Try Again!")
   print("------------------------")