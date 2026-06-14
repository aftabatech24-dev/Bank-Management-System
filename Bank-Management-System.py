#BANK MANAGEMENT SYSTEM 
print("=====BANK SYSTEM=====")
def deposit_amount(deposit):
    print(f"₹{deposit} Deposited Successfully ")
    return deposit
def withdraw_money(withdraw):
    print(f"₹{withdraw} withdrawal Successfully ")
    return withdraw
def show_balance(balance):
    print(f"Your balance is {balance}")    
def show_history(history):
    for i in history:
        print(i)    
exit_loop=False
for i in range(3):
    if exit_loop:
        break
    attempt=2-i
    PIN=1234
    pin=int(input("Enter 4 digit pin: "))
    if pin==PIN:
        balance=5000
        history=[]
        while True:
            print("1.Deposit")
            print("2.Withdraw")
            print("3.Check balance")
            print("4.History")
            print("5.Exit")
            choice=int(input("Enter choise "))
            if choice == 1:
                amount=int(input("Enter Amount: "))
                if amount<=0:
                    print("Amount must be greater than 0")
                    continue 
                else:    
                    d1=deposit_amount(amount)
                    balance+=d1
                    history.append(f"Deposit {d1}")
            elif choice == 2:
                money=int(input("Enter Amount to withdraw "))
                if money<=0:
                    print("Amount must be greater than zero") 
                    continue 
                elif money>balance:
                    print("Insufficient balance") 
                    continue
                else :
                    w1=withdraw_money(money)
                    balance-=w1
                    history.append(f"Withdraw {w1}")
            elif choice == 3:
                show_balance(balance)
            elif choice == 4:
                if len(history)==0:
                    print("No transaction found")
                else:    
                    show_history(history) 
            elif choice == 5:
                exit_loop=True
                break
            else:
                print("Invalid Choice") 
                continue  
        print("Thank you for using Bank Management System")         
    else:
        print("Wrong pin!!!")
        print(f"{attempt} attempt left")
        continue
else:        
    print("Try Again after some time!!!! ")                  
