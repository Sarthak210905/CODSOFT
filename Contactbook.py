class Contact:
    def __init__(self, naam, number, mail, address):
        self.naam = naam
        self.number = number
        self.mail = mail
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, naam, number, mail, address):
        new_contact = Contact(naam, number, mail, address)
        self.contacts.append(new_contact)
        print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        for contact in self.contacts:
            print("Name: ",contact.naam, "Phone:",contact.number, "Email: ",contact.mail, "Address: ",contact.address)

    def search_contact(self, search_term):
        results = [contact for contact in self.contacts if search_term in contact.naam or search_term in contact.number]
        if not results:
            print("No contacts found.")
            return
        for contact in results:
            print("Name: ",contact.naam, "Phone:",contact.number, "Email: ",contact.mail, "Address: ",contact.address)
    def update_contact(self, naam, new_number=None, new_mail=None, new_address=None):
        for contact in self.contacts:
            if contact.naam == naam:
                if new_number:
                    contact.number = new_number
                if new_mail:
                    contact.mail = new_mail
                if new_address:
                    contact.address = new_address
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, naam):
        for contact in self.contacts:
            if contact.naam == naam:
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

def main():
    contact_book = ContactBook()
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            naam = input("Enter Name: ")
            number = input("Enter Phone number: ")
            mail = input("Enter Email: ")
            address = input("Enter Address: ")
            contact_book.add_contact(naam, number, mail, address)
        elif choice == '2':
            if not contact_book.contacts:
                print("No contacts found.")
                continue
            else:
             contact_book.view_contacts()
        elif choice == '3':
            if not contact_book.contacts:
                print("No contacts to search.")
                continue
            else:
             search_term = input("Enter Name or number number to search: ")
             contact_book.search_contact(search_term)
        elif choice == '4':
            if not contact_book.contacts:
                print("No contacts to update.")
                continue
            else:
             naam = input("Enter the Name of the contact to update: ")
             new_number = input("Enter new Phone number (leave blank to keep current): ")
             new_mail = input("Enter new Email (leave blank to keep current): ")
             new_address = input("Enter new address (leave blank to keep current): ")
             contact_book.update_contact(naam, new_number, new_mail, new_address)
        elif choice == '5':
            if not contact_book.contacts:
                print("No contacts to delete.")
                continue
            else:
             naam = input("Enter the naam of the contact to delete: ")
             contact_book.delete_contact(naam)
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


main()
