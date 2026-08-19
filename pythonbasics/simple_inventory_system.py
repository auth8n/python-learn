class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name:str, price:float, quantity:int):
        if name not in self.items:
            self.items[name] = {
                "price": price,
                "quantity": quantity
            }
        else:
            self.items[name].update({
                "price": price,
                "quantity": quantity
            })        

    def remove_item(self, name:str):
        if name in self.items:
            self.items.pop(name, None)

    def get_item(self, name:str):
        if name in self.items:
            return self.items[name]

    def list_items(self):
        result = ""
        for item in self.items:
            for key, value in self.items[item].items():
                result += f"{key}: {value}\n"
        return result

items = Inventory()

items.add_item("Dell Laptop", 4500, 2)
items.add_item("HP Laptop", 4000, 3)
items.add_item("iPhone 15", 3700, 1)

items.remove_item("Dell Laptop")

print(items.get_item("HP Laptop"))
print(items.list_items())