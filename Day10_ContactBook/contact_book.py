from random import choice

contacts=[]

def add_contact():
    name=input("Enter name: ")
    phone=input("Enter Phone no: ")
    email=input("Enter email: ")
    contacts.append({"name":name,"phone":phone,"email":email})
    print("Contact added sucessfully")

def view_contact():
    if not contacts:
        print("Not Found")
    else:

        for idx,contact in enumerate(contacts,start=1):
            print(f"{idx},{contact['name']}| {contact['phone']} | {contact['email']}")
        print()

def search_contact():
    search_name=input("Enter name to be search: ")
    found=False
    for contact in contacts:
        if contact['name'].lower() == search_name.lower():
            print(f"Found: {contact['name']} | {contact['phone']} | {contact['email']}")
            found=True
            break
    if not found:
        print("Contact not found,\n")


def contact_book():
    while True:
        print("===Contact Book ===")
        print("1.Add Contact")
        print("2.View contact")
        print("3.Search contact")
        print("4.Exit")

        choice=input("Enter your choice")


        if choice=='1':
           add_contact()
        elif choice=='2':
           view_contact()
        elif choice=='3':
            search_contact()
        elif choice=='4':
            print("Exiting Contact Book")
            break
        else:
            print("Invalid Choice,Try again!")

contact_book()
