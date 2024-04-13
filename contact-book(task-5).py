import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        # Contact list
        self.contacts = {}


        # Entry widgets
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)
        self.address_entry = tk.Entry(root)
        self.address_entry.grid(row=3, column=1, padx=5, pady=5)
        
        # Labels
        tk.Label(root, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(root, text="Phone:").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(root, text="Email:").grid(row=2, column=0, padx=5, pady=5)
        tk.Label(root, text="Address:").grid(row=3, column=0, padx=5, pady=5)
        
        
        # Buttons
        tk.Button(root, text="Add Contact", command=self.add_contact).grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="we")
        tk.Button(root, text="Update Contact", command=self.update_contact).grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="we")
        tk.Button(root, text="Remove Contact", command=self.remove_contact).grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="we")
        tk.Button(root, text="View Contacts", command=self.view_contacts).grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky="we")

    
    # Function to update a contact
    def update_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()

        if name in self.contacts:
            self.contacts[name] = {"Phone": phone, "Email": email, "Address": address}
            messagebox.showinfo("Success", f"Contact '{name}' updated successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Warning", f"Contact '{name}' not found.")

    # Function to remove a contact
    def remove_contact(self):
        name = self.name_entry.get().strip()

        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Success", f"Contact '{name}' removed successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Warning", f"Contact '{name}' not found.")
    
    # Function to add a contact
    def add_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()

        if name:
            self.contacts[name] = {"Phone": phone, "Email": email, "Address": address}
            messagebox.showinfo("Success", f"Contact '{name}' added successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Warning", "Name cannot be empty.")

    # Function to view contacts
    def view_contacts(self):
        contacts_text = ""
        for name, details in self.contacts.items():
            contacts_text += f"Name: {name}\n"
            contacts_text += f"Phone: {details['Phone']}\n"
            contacts_text += f"Email: {details['Email']}\n"
            contacts_text += f"Address: {details['Address']}\n\n"
        if contacts_text:
            messagebox.showinfo("Contacts", contacts_text)
        else:
            messagebox.showinfo("Contacts", "No contacts to display.")

    # Function to clear entry widgets
    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

root = tk.Tk()
app = ContactBook(root)
root.mainloop()
