class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name:str, number:str, email:str):
        self.contacts[name] = {"number": number,
                               "email": email}

    def remove_contact(self, name:str) -> dict | None:
        return self.contacts.pop(name, None)

    def find_contact(self, name:str) -> str:
        return self.contacts.get(name)

    def list_contacts(self) -> str:
        contacts = ""
        for name, details in self.contacts.items():
            contacts += f"{name}: Phone number: {details['number']} Email: {details['email']}\n"
        return contacts
        #return "\n".join(
        #   f"{name}: Phone number: {details['number']} Email: {details['email']}"
        #   for name, details in self.contacts.items()   
        #)

contacts = ContactBook()

contacts.add_contact("Collins", "0748224299", "collinsgodiah@gmail.com")
contacts.add_contact("Nereah", "0722223445", "nereahopiyo@gmail.com")
contacts.add_contact("Ronald", "0711223456", "ronaldotego@gmail.com")

contacts.remove_contact("Ronald")
print(contacts.remove_contact("Nicole"))

print(contacts.find_contact("Nereah"))
print(contacts.list_contacts())