
name  = input("Plz enter your name : ")
print("Helllo ",name)

message = """
How may i help you sir .
Please select any of them option,
Type 1 >>>> CHECK BALANCE.
Type 2 >>>> DEPOSIT.
Type 3 >>>> WITHDRAWL.
"""
print(message)
task = int(input("Plz insert your option : "))
available_amount = 5000

if task >=1 and task <=3:  # in btwn 1 - 3 
    print("Welcome to you in virtual bank!")

    #check balance
    if task == 1:
        print("Your available balance is : ",available_amount)

    # deposit amount
    elif task == 2:
        deposit_amount = int(input("plz enter deposit amout : "))

        if deposit_amount >=500:
            # available_amount =  available_amount + deposit_amount
            available_amount += deposit_amount 
            print("you have successfully deposited amount : ",deposit_amount)
            print("Your available balance is : ",available_amount)

        else:
            print("Plz enter more than 500 rupees!")


    # withdrawl amount 
    else:
        withdrawl_amount = int(input('Plz enter withdrawl amount : '))
        if withdrawl_amount <= available_amount:
            available_amount -= withdrawl_amount
            print("You have successfully withrdrawl your amount : ",withdrawl_amount)
            print("Your available balance is : ",available_amount)

        else:
            print('you have no sufficient balance in your account!')
else:
    print("Plz choose correct input in between 1 to 3 !")




#<<<<<<<<<<<<<<<<practics atm symulation>>>>>>

name=("plese inter your name ")
print("hello ,name")
message= """
how may i help you sir.
plese select any of them option ,
type 1>>>>check balance.
type 2 >>>>deposit.
type3>>>>withdrawl.
"""
print(message)
task= int(input("plz insert your option:"))
available_amount = 10000

if task==1:
  print("your avillable balance is :",available_amount)


  # deposit amount 

elif task==2:
    deposit_amount=int(input("plz enter deposit amount: "))
    if deposit_amount>=500:
     
     # available_amount=available_amount+deposit_amount
     available_amount+=deposit_amount
     print("you have sucessfully deposit amount:",deposit_amount)
     print("your avillable balance is :",available_amount)
    else:
     print("plz enter more than 500 rupees")

     # withdrawl amount
# else:

#     withdrawl_amount= int (input('plz inter withdrawl_amount:,'))
#     if withdrawl_amount<=available_amount:
#        available_amount-=withdrawl_amount
#        print("you have sucessfully withdrawl your amount:",withdrawl_amount)
#        print("your avillble balance is :",available_amount)
#     else:
#        print("you have no sufficient balance in tyour account!")
# else:
# print("plz choose correct input in between 1 to 3!")



else:
     withdrawl_amount = int(input('Plz enter withdrawl amount : '))
if withdrawl_amount <= available_amount:
            available_amount -= withdrawl_amount
            print("You have successfully withrdrawl your amount : ",withdrawl_amount)
            print("Your available balance is : ",available_amount)
else:
  print('you have no sufficient balance in your account!')
else:
print("Plz choose correct input in between 1 to 3 !")