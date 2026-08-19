class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name:str, price:float, quantity:int):
        self.items[name] = {"price": price,
                            "quantity": quantity}    

    def remove_item(self, name:str):
        self.items.pop(name, None)

    def get_item(self, name:str):
        return self.items.get(name)

    def list_items(self):
        result = ""

        for name, details in self.items.items():
            result += f"{name}: Price=${details['price']}, Quantity={details['quantity']}\n"
        return result

items = Inventory()

items.add_item("Dell Laptop", 4500, 2)
items.add_item("HP Laptop", 4000, 3)
items.add_item("iPhone 15", 3700, 1)

items.remove_item("Dell Laptop")

print(items.get_item("HP Laptop"))
print(items.list_items())