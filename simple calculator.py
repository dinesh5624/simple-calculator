def add(x,y):
  return x+y
def subtract(x,y):
  return x-y
def multiple (x,y):
  return x*y
def divide(x,y):
  if y !=0:
    return x/y
  else:
    return"Error!Division by zero."
def calculator():
  print("simple calculator")
  print("choose operation:")
  print("1.Add")
  print("2.Subtract")
  print("3.Multiply")
  print("4.Divide")
  while True:
    choice=input("Enter choice(1/2/3/4):")
    if choice in ['1','2','3','4']:
      num1=float(input("Enter first number:"))
      num2=float(input("Enter second number:"))
      if choice =='1':
       print(f"the result is :{add(num1,num2)}")
      elif choice=='2':
        print(f"the result is :{subtract(num1,num2)}")
      elif choice=='3':
        print(f"the result is :{multiply(num1,num2)}")
      elif choice=='4':
        print(f"the result is:{divide(num1,num2)}")
      next_calculation=input("Do you want to perform another calculation?(yes/no):")
      if next_calculation.lower()!='yes':
         break
  else:
     print("invalid input")
  #run the calculator
calculator()
