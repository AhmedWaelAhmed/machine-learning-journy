from login_sys import log
from display_product import display_table

products = [
    {"name": "Water", "price": 80.0, "quantity": 1500},
    {"name": "Soda",  "price": 130.0, "quantity": 1500}
]

if __name__ == "__main__":
    is_logged_in = log()
    
    if is_logged_in:
        print("Loading Data...")
        display_table(products)
    else:
        print("Access Denied.")
        