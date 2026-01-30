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
def simple_intrest(principal_amt,rate_of_intrest,time_period):
  princiapl_amt=float(input("Enter the principal amount: "))
  rate_of_intrest=float(input("Enter the rate of interest (in %): "))
  time_period=float(input("Enter the time period (in years): "))
  simple_intrest=(princiapl_amt*rate_of_intrest*time_period)/100
  print(f"The Simple Intrest is :{simple_intrest}")
  def compound_intrest(principal_amt,rate_of_intrest,time_period):
    principal_amt=float(input("Enter the principal amount: "))
    rate_of_intrest=float(input("Enter the rate of intrest in percetage (%):"))
    time_period=float(input("Enter the time period (in years): "))
    compound_intrest=principal_amt*(1+(rate_of_intrest/100))**time_period - princiapl_amt
    print(f"The Compund Intrest is :{compound_intrest}")
def emi(princiapl_amt,rate_of_intrest,time_period):
  princiapl_amt=float(input("Enter the principal amount: "))
  rate_of_intrest=float(input("Enter the rate of intrest in percetage (%):"))
  time_period=float(input("Enter the time period (in months): "))
  monthly_rate_of_intrest=rate_of_intrest/(12*100)
  toatal_months=time_period*12
  emi=princiapl_amt*monthly_rate_of_intrest(1+monthly_rate_of_intrest)**toatal_months/(1+monthly_rate_of_intrest)**toatal_months-1
  print(f"The EMI is :{emi}")