class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

class ContactManagementSystem:
    def __init__(self):
        self.contacts = {}

    def add_contact(self):
        print("Enter contact name:")
        name = input()
        print("Enter contact phone number:")
        phone_number = input()
        print("Enter contact email:")
        email = input()
        contact = Contact(name, phone_number, email)
        self.contacts[name] = contact
        print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("Contact list is empty.")
        else:
            print("Contact List:")
            for contact in self.contacts.values():
                print("Name:", contact.name,
                      ", Phone:", contact.phone_number,
                      ", Email:", contact.email)

    def edit_contact(self):
        print("Enter the name of the contact to edit:")
        name = input()
        contact = self.contacts.get(name)
        if not contact:
            print("Contact not found.")
            return
        print("Enter new phone number (Leave blank to keep existing):")
        phone_number = input()
        if phone_number:
            contact.phone_number = phone_number
        print("Enter new email (Leave blank to keep existing):")
        email = input()
        if email:
            contact.email = email
        print("Contact edited successfully.")

    def delete_contact(self):
        print("Enter the name of the contact to delete:")
        name = input()
        contact = self.contacts.pop(name, None)
        if not contact:
            print("Contact not found.")
        else:
            print("Contact deleted successfully.")

if __name__ == "__main__":
    cms = ContactManagementSystem()
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        print("Enter your choice:")
        
        choice = input()

        if choice == '1':
            cms.add_contact()
        elif choice == '2':
            cms.view_contacts()
        elif choice == '3':
            cms.edit_contact()
        elif choice == '4':
            cms.delete_contact()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
