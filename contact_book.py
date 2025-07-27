def add_contact(filename):
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    
    with open(filename, "a") as file:
        file.write(f"{name},{phone},{email}\n")
    print("Contact added successfully!")

def view_contacts(filename):
    try:
        with open(filename, "r") as file:
            print("\n--- All Contacts ---")
            for line in file:
                name, phone, email = line.strip().split(",")
                print(f"Name: {name} | Phone: {phone} | Email: {email}")
    except FileNotFoundError:
        print("No contacts found.")

def search_contact(filename):
    search_name = input("Enter name to search: ").lower()
    found = False
    try:
        with open(filename, "r") as file:
            for line in file:
                name, phone, email = line.strip().split(",")
                if name.lower() == search_name:
                    print(f"Name: {name} | Phone: {phone} | Email: {email}")
                    found = True
                    break
        if not found:
            print("Contact not found.")
    except FileNotFoundError:
        print("No contacts found.")

def delete_contact(filename):
    name_to_delete = input("Enter name to delete: ").lower()
    updated = []
    found = False

    try:
        with open(filename, "r") as file:
            for line in file:
                name, phone, email = line.strip().split(",")
                if name.lower() != name_to_delete:
                    updated.append(line)
                else:
                    found = True

        with open(filename, "w") as file:
            file.writelines(updated)

        if found:
            print("Contact deleted.")
        else:
            print("Contact not found.")
    except FileNotFoundError:
        print("No contacts file found.")

def main():
    filename = "contacts.txt"
    
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_contact(filename)
        elif choice == "2":
            view_contacts(filename)
        elif choice == "3":
            search_contact(filename)
        elif choice == "4":
            delete_contact(filename)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-5.")

if __name__ == "__main__":
    main()
