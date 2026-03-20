expense = {}

def add_expense():
    name = input("Enter expense name ")
    amount = int(input("Enter amount "))
    expense[name] = amount
    print("Expense added successfully")

def remove_expense():
    name = input("Enter expense name to be removed ")
    if name in expense:
        del expense[name]
        print("Expense removed succcessfully")
    else:
        print("Expense not found")

def view_expense():
    for name, amount in expense.items():
        print(name, ":", amount)

def total_expense():
    total = 0
    for name in expense:
        total = total +expense[name]
    print("Total expense is ", total)

def highest_expense():
    highest = 0
    for name in expense:
        if expense[name] > highest:
            highest = expense[name]
    print("Highest expense is ", highest)

def averag_expense():
    total = 0
    average = 0
    for name in expense:
        total = total + expense[name]
        average = total/ len(expense)
    print("Average expense is ", average)

def find_expense():
    name = input("Enter expense name to search ")
    if name in expense:
        print("Amount: ", expense[name])
    else:
        print("Expense not found")

while True:
    print("Expense Tracker\n")
    print("1. Add expense")
    print("2. Remove expense")
    print("3. View expense")
    print("4. Total expense")
    print("5. Highest expense")
    print("6. Average expense")
    print("7. Find expense")
    print("8. Exit")
    choice = input("Enter choice ")

    if choice == '1':
        add_expense()
    elif choice == '2':
        remove_expense()
    elif choice == '3':
        view_expense()
    elif choice == '4':
        total_expense()
    elif choice == '5':
        highest_expense()
    elif choice == '6':
        averag_expense()
    elif choice == '7':
        find_expense()
    elif choice == '8':
        break 
    else:
        print("Invalid choice")
