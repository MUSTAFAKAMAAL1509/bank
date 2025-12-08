bank_accounts = {}
def create_account():
    print("\n--- Create New Account ---")
    name = input("Enter Account Holder Name: ").strip()
    pin = input("Set a 4-digit PIN: ").strip()
    if not pin.isdigit() or len(pin) != 4:
        print("❌ Invalid PIN! Please use 4 digits only.")
        return
    if name in bank_accounts:
        print("❌ Account already exists!")
        return
    initial_deposit = float(input("Enter Initial Deposit Amount: ₹"))
    bank_accounts[name] = {"pin": pin, "balance": initial_deposit}
    print(f"✅ Account created successfully for {name} with ₹{initial_deposit:.2f}\n")
def deposit():
    print("\n--- Deposit Money ---")
    name = input("Enter Account Holder Name: ").strip()
    pin = input("Enter your 4-digit PIN: ").strip()
    if name in bank_accounts and bank_accounts[name]["pin"] == pin:
        amount = float(input("Enter amount to deposit: ₹"))
        bank_accounts[name]["balance"] += amount
        print(f"✅ ₹{amount:.2f} deposited successfully! New balance: ₹{bank_accounts[name]['balance']:.2f}\n")
    else:
        print("❌ Invalid account name or PIN!\n")
def withdraw():
    print("\n--- Withdraw Money ---")
    name = input("Enter Account Holder Name: ").strip()
    pin = input("Enter your 4-digit PIN: ").strip()
    if name in bank_accounts and bank_accounts[name]["pin"] == pin:
        amount = float(input("Enter amount to withdraw: ₹"))
        if amount <= bank_accounts[name]["balance"]:
            bank_accounts[name]["balance"] -= amount
            print(f"✅ ₹{amount:.2f} withdrawn successfully! Remaining balance: ₹{bank_accounts[name]['balance']:.2f}\n")
        else:
            print("❌ Insufficient balance!\n")
    else:
        print("❌ Invalid account name or PIN!\n")
def check_balance():
    print("\n--- Balance Inquiry ---")
    name = input("Enter Account Holder Name: ").strip()
    pin = input("Enter your 4-digit PIN: ").strip()
    if name in bank_accounts and bank_accounts[name]["pin"] == pin:
        print(f"💰 Account Holder: {name}\nCurrent Balance: ₹{bank_accounts[name]['balance']:.2f}\n")
    else:
        print("❌ Invalid account name or PIN!\n")
def view_all_accounts():
    print("\n--- All Account Holders ---")
    if not bank_accounts:
        print("No accounts found!\n")
    else:
        print("Name\t\tBalance (₹)")
        print("-" * 25)
        for name, info in bank_accounts.items():
            print(f"{name}\t\t{info['balance']:.2f}")
        print()
while True:
    print("===== MINI BANKING SYSTEM =====")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. View All Accounts")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ").strip()

    if choice == "1":
        create_account()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        view_all_accounts()
    elif choice == "6":
        print("🙏 Thank you for using Mini Banking System!")
        break
    else:
        print("❌ Invalid choice! Please try again.\n")
