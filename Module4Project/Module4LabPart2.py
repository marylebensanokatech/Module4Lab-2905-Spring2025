class DunnDelivery:
    def __init__(self):
        # Enhanced menu with seasonal drinks to provide more variety
        self.menu = {
            "Energy Drinks": ["Monster", "Rockstar"],
            "Coffee Drinks": [
                "Latte", "Cappuccino",
                "Peppermint Hot Chocolate",  # Winter warmer
                "Maple Cinnamon Latte",      # Winter warmer
                "Iced Lavender Coffee"       # Summer cooler
            ],
            "Breakfast": ["Bagel", "Muffin", "Scone"],
            "Lunch": ["Falafel Wrap", "Hummus & Pita", "Chicken Wrap"]
        }
        
        # Updated prices including new seasonal drinks
        self.prices = {
            "Monster": 3.99, "Rockstar": 3.99,
            "Latte": 4.99, "Cappuccino": 4.99,
            "Peppermint Hot Chocolate": 5.49,
            "Maple Cinnamon Latte": 5.49,
            "Iced Lavender Coffee": 5.29,
            "Bagel": 2.99, "Muffin": 2.99, "Scone": 2.99,
            "Falafel Wrap": 8.99, "Hummus & Pita": 7.99, "Chicken Wrap": 8.99,        
        }
        
        self.delivery_locations = {
            "Library": 10,  # minutes
            "Academic Success Center": 8,
            "ITEC Computer Lab": 5
        }
        
        # Dictionary to store delivery ratings
        self.delivery_ratings = {}
        
        # Counter for order IDs
        self.order_counter = 0
    
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
    
    def find_items_under_price(self, max_price):
        """
        Searches for all menu items under a specified price point.
        This helps budget-conscious students find affordable options.
        
        Args:
            max_price (float): Maximum price to search for
            
        Returns:
            dict: Categories and their items under the specified price
        """
        affordable_items = {}
        for category, items in self.menu.items():
            category_items = [item for item in items if self.prices[item] <= max_price]
            if category_items:
                affordable_items[category] = category_items
        return affordable_items
    
    def calculate_total(self, items, has_student_id=False, priority_delivery=False):
        total = sum(self.prices[item] for item in items)
        # Add priority delivery fee if selected
        if priority_delivery:
            total += 2.00
        # Apply student discount after all other charges
        if has_student_id and total > 10:
            total *= 0.9
        return total
    
    def estimate_delivery(self, location, current_hour, priority_delivery=False):
        base_time = self.delivery_locations[location]
        # Add rush hour delay
        if (9 <= current_hour <= 10) or (11 <= current_hour <= 13):
            base_time += 5
        # Subtract priority delivery time if selected
        if priority_delivery:
            base_time = max(2, base_time - 3)  # Ensure minimum 2-minute delivery time
        return base_time

    def rate_delivery(self, order_id, rating):
        """
        Allows customers to rate their delivery experience.
        
        Args:
            order_id (int): Unique identifier for the order
            rating (int): Rating from 1 to 5 stars
            
        Returns:
            bool: True if rating was successful, False otherwise
        """
        if not (1 <= rating <= 5):
            print("Error: Rating must be between 1 and 5 stars")
            return False
        
        self.delivery_ratings[order_id] = rating
        print(f"Thank you for rating your delivery! (Order #{order_id}: {rating} stars)")
        return True

    def print_order(self, location, items, current_hour, has_student_id=False, priority_delivery=False):
        self.order_counter += 1
        order_id = self.order_counter
        
        print("\n=== Order Summary ===")
        print(f"Order #: {order_id}")
        print(f"Delivery to: {location}")
        print("\nItems ordered:")
        for item in items:
            print(f"- {item}: ${self.prices[item]:.2f}")
        
        total = self.calculate_total(items, has_student_id, priority_delivery)
        delivery_time = self.estimate_delivery(location, current_hour, priority_delivery)
        
        print(f"\nSubtotal: ${sum(self.prices[item] for item in items):.2f}")
        if priority_delivery:
            print("Priority Delivery Fee: $2.00")
        if has_student_id and total < sum(self.prices[item] for item in items):
            print("Student Discount Applied!")
        print(f"Total after all charges and discounts: ${total:.2f}")
        print(f"Estimated delivery time: {delivery_time} minutes")
        if priority_delivery:
            print("Priority delivery selected - your order will arrive 3 minutes faster!")
        print(f"\nPlease keep your order number ({order_id}) to rate your delivery later!")
        return order_id

def main():
    delivery = DunnDelivery()
    
    # Show the enhanced coffee drinks menu
    print("=== New Seasonal Drinks Added! ===")
    delivery.show_menu("Coffee Drinks")
    
    # Show budget-friendly options
    print("\n=== Budget-Friendly Options (Under $5) ===")
    affordable = delivery.find_items_under_price(5.00)
    for category, items in affordable.items():
        print(f"\n{category}:")
        for item in items:
            print(f"- {item}: ${delivery.prices[item]:.2f}")
    
    # Sample order with priority delivery at 9:30 AM (peak morning hour)
    print("\n=== Sample Order ===")
    order = ["Maple Cinnamon Latte", "Bagel"]
    order_id = delivery.print_order(
        "ITEC Computer Lab",
        order,
        9,
        has_student_id=True,
        priority_delivery=True
    )
    
    # Sample delivery rating
    delivery.rate_delivery(order_id, 5)

if __name__ == "__main__":
    main()