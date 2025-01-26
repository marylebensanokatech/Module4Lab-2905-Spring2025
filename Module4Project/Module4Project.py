# The DunnDelivery class demonstrates core OOP concepts:
# - Encapsulation: Data (menu, prices) and methods are bundled in the class
# - Abstraction: Complex delivery logic is hidden behind simple method calls
class DunnDelivery:
    def __init__(self):
        # Class attributes demonstrate encapsulation 
        # by keeping related data together
        self.menu = {
            "Energy Drinks": ["Monster", "Rockstar"],
            "Coffee Drinks": ["Latte", "Cappuccino"],
            "Breakfast": ["Bagel", "Muffin", "Scone"],
            "Lunch": ["Falafel Wrap", "Hummus & Pita", "Chicken Wrap"]
        }
        
        # Prices encapsulated within the class
        self.prices = {
            "Monster": 3.99, "Rockstar": 3.99,
            "Latte": 4.99, "Cappuccino": 4.99,
            "Bagel": 2.99, "Muffin": 2.99, "Scone": 2.99,
            "Falafel Wrap": 8.99, "Hummus & Pita": 7.99, "Chicken Wrap": 8.99,        
        }
        
        self.delivery_locations = {
            "Library": 10,  # minutes
            "Academic Success Center": 8,
            "ITEC Computer Lab": 5
        }
    
    def show_menu(self, category=None):
        if category:
            print(f"\n=== {category} ===")
            for item in self.menu[category]:
                print(f"{item}: ${self.prices[item]:.2f}")
        else:
            for category in self.menu:
                print(f"\n=== {category} ===")
                for item in self.menu[category]:
                    print(f"{item}: ${self.prices[item]:.2f}")
    
    def calculate_total(self, items, has_student_id=False):
        total = sum(self.prices[item] for item in items)
        if has_student_id and total > 10:
            total *= 0.9
        return total
    
    def estimate_delivery(self, location, current_hour):
        base_time = self.delivery_locations[location]
        if (9 <= current_hour <= 10) or (11 <= current_hour <= 13):
            return base_time + 5
        return base_time

    def print_order(self, location, items, current_hour, has_student_id=False):
        print("\n=== Order Summary ===")
        print(f"Delivery to: {location}")
        print("\nItems ordered:")
        for item in items:
            print(f"- {item}: ${self.prices[item]:.2f}")
        
        total = self.calculate_total(items, has_student_id)
        delivery_time = self.estimate_delivery(location, current_hour)
        
        print(f"\nSubtotal: ${sum(self.prices[item] for item in items):.2f}")
        if has_student_id and total < sum(self.prices[item] for item in items):
            print("Student Discount Applied!")
        print(f"Total after discount: ${total:.2f}")
        print(f"Estimated delivery time: {delivery_time} minutes")

# Example usage
def main():
    delivery = DunnDelivery()
    delivery.show_menu("Coffee Drinks")
    
    # Sample order at 9:30 AM (peak morning hour)
    order = ["Latte", "Bagel"]
    delivery.print_order("ITEC Computer Lab", order, 9, has_student_id=True)

if __name__ == "__main__":
    main()

