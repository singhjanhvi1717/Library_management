#functions to be used in the loop
#start_menu()
#simple_intrest()
#compound_intrest()
#emi()

#display welcome message
#make functions
#make loop to call functions based on user input
#end loop on user request

print("Welcome to your comprehensive financial analysis tool.\nMake informed decisions with accurate calculations.")
def startmenu():
  print("What would you like to calculate today?")
  print("1. Simple Interest\n2. Compound Interest\n3. EMI Calculator\n4. Exit")
  input1=int(input("Enter your choice (1-4): "))
  return input1


def simple_interest():
  while True:
    try:
      principal=float(input("Enter the principal amount: "))
      rate=float(input("Enter the rate of interest (in %): "))
      time=float(input("Enter the time period (in years): "))
      
      if principal<=0 or rate<=0 or time<=0:
        print("Please enter positive values for principal, rate, and time.")
        continue

      si=(principal*rate*time)/100
      print(f"The Simple Intrest is :{si}")
      break 
    except ValueError:
      print("Invalid input. Please enter numeric values for principal, rate, and time.")  


def compound_interest():
  while True:
    try:
      principal=float(input("Enter the principal amount: "))
      rate=float(input("Enter the rate of intrest in percentage (%):"))
      time=float(input("Enter the time period (in years): "))
      if principal<=0 or rate<=0 or time<=0:
        print("Please enter positive values for principal, rate, and time.")
        continue

      ci=principal*(1+(rate/100))**time - principal
      print(f"The Compund Intrest is :{ci}")
      break
    except ValueError:
      print("Invalid input. Please enter numeric values for principal, rate, and time.")

def emi():
  while True:
    try:
      principal=float(input("Enter the principal amount: "))
      rate=float(input("Enter the rate of intrest in percetage (%):"))
      time=float(input("Enter the time period (in years): "))
      if principal<=0 or rate<=0 or time<=0:
        print("Please enter positive values for principal, rate, and time.")
        continue
      monthly_rate_of_intrest=rate/(12*100)
      total_months=time*12 
      e_m_i = principal*monthly_rate_of_intrest*(1+monthly_rate_of_intrest)**total_months/((1+monthly_rate_of_intrest)**total_months-1)
      print(f"The EMI is :{e_m_i}")
      break
    except ValueError:
      print("Invalid input. Please enter numeric values for principal, rate, and time.")


while True:
  try:
    choice=startmenu()
    if choice==1:
      simple_interest()
    elif choice==2:
      compound_interest()
    elif choice==3:
      emi()
    elif choice==4:
      print("Thank you for using the financial analysis tool. Goodbye!")
      break
    else:
      print("Invalid choice. Please enter a number between 1 and 4.")
  except ValueError:
    print("Invalid input. Please enter a number.")

