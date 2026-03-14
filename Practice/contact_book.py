contacts={}

def add_contact():
    name = input("Enter name ")
    phone = int(input("Enter number "))
    contacts[name]= phone
    print("contact added successfully")

def view_contact():
    for name, phone in contacts.items():
        print(name,":", phone)

def search_contact():
    name = input("Enter name to search ")
    if name in contacts:
        print("Phone number: ", contacts[name])
    else:
        print("name not found")

def update_contact():
    name = input("Enter name to be updated ")
    if name in contacts:
        phone = int(input("Enter number to be updated "))
        contacts[name] = phone
        print("Contact updated successfully")
    else:
        print("Name not found")

def remove_contact():
    name = input("Enter name to be deleted")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully")
    else:
        print("Name not found")

def total_contact():
    total = 0
    for name in contacts:
        total = total + 1
    print("Total contacts are ", total)

while True:
    print("\nContact Book\n")
    print("1. Add contact")
    print("2. View contact")
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Total contacts")
    print("7. Exit")
    choice = input("Enter choice ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contact()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        remove_contact()
    elif choice == '6':
        total_contact()
    elif choice == '7':
        print("Exiting ")
        break
    else:
        print("Invalid choice")