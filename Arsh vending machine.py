class VendingMachine:
    def __init__(self):
        # Initialize the vending machine with a menu of items and their prices
        self.menu = {
            '1': {'name': 'Coke', 'price': 1.50},
            '2': {'name': 'Pepsi', 'price': 1.50},
            '3': {'name': 'Water', 'price': 1.00},
            '4': {'name': 'Chips', 'price': 1.25},
            '5': {'name': 'Chocolate Bar', 'price': 1.75},
            '6': {'name': 'Gum', 'price': 0.75}
        }
        self.balance = 0.0  # User's balance
        self.change = 0.0   # Change to be returned

    def display_menu(self):
        # Display the menu of items
        print("Welcome to the Vending Machine!")
        print("Please select an item by entering the corresponding number:")
        for key, item in self.menu.items():
            print(f"{key}: {item['name']} - ${item['price']:.2f}")

    def insert_money(self):
        # Allow the user to insert money
        while True:
            try:
                amount = float(input("Please insert money (enter 0 to finish): $"))
                if amount < 0:
                    print("Please enter a positive amount.")
                elif amount == 0:
                    break
                else:
                    self.balance += amount
                    print(f"You have inserted: ${amount:.2f}. Current balance: ${self.balance:.2f}")
            except ValueError:
                print("Invalid input. Please enter a valid amount.")

    def select_item(self):
        # Allow the user to select an item from the menu
        while True:
            choice = input("Enter the number of the item you want to purchase: ")
            if choice in self.menu:
                item = self.menu[choice]
                if self.balance >= item['price']:
                    self.balance -= item['price']
                    print(f"Dispensing {item['name']}...")
                    self.change = self.balance  # Remaining balance is the change
                    self.balance = 0.0  # Reset balance after purchase
                    print(f"Thank you for your purchase! Your change is: ${self.change:.2f}")
                    break
                else:
                    print(f"Insufficient balance. You need ${item['price'] - self.balance:.2f} more.")
            else:
                print("Invalid selection. Please choose a valid item number.")

    def run(self):
        # Main method to run the vending machine
        self.display_menu()
        self.insert_money()
        self.select_item()
        print("Thank you for using the Vending Machine!")

# Create an instance of the VendingMachine class and run it
if __name__ == "__main__":
    vending_machine = VendingMachine()
    vending_machine.run()