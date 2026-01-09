# shopping_cart.py

def start_shopping(products_list):
    """
    دالة للتعامل مع عملية الشراء وحساب الفاتورة وتحديث المخزون
    """
    total_bill = 0
    
    print("\n--- Welcome to the Shopping Cart ---")

    while True:
        product_name = input("\nEnter product name (or 'exit' to finish): ").strip().lower()
        if product_name == 'exit':
            break
        
        # البحث عن المنتج داخل القائمة التي تم تمريرها للدالة
        # Search for product inside the passed list
        product = next((p for p in products_list if p['name'].lower() == product_name.lower()), None)
        
        if product is None:
            print("Product not found. Please try again.")
            continue

        try:
            print(f"Available Quantity for {product['name']}: {product['quantity']}")
            quantity_input = input(f"How many {product['name']} do you want? ")
            
            # التحقق من أن المدخل رقم
            if not quantity_input.isdigit(): 
                print("Invalid input! Please enter a number.")
                continue
                
            quantity_required = float(quantity_input)
            
            if quantity_required <= 0:
                print("Quantity must be greater than zero.")
                continue
                
            if quantity_required > product['quantity']:
                print("Insufficient quantity!")
                continue

            # --- Calculations ---
            discount_percentage = 0.05
            price_before_disc = quantity_required * product['price']
            
            discount_amount = price_before_disc * discount_percentage 
            final_price = price_before_disc - discount_amount

            # --- Updates (تحديث القائمة الأصلية مباشرة) ---
            product['quantity'] -= quantity_required
            total_bill += final_price
            
            print(f"Success! Price for {product['name']}: ${final_price:.2f}")
            
            another = input("Something else? (y/n): ").lower()
            if another != 'y':
                break
                
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    # --- Final Output ---
    print(f"\nTotal amount to pay: ${total_bill:.2f}")
    print("Thank you for shopping with us!")