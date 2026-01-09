from login_sys import log
from display_product import display_table
# 1. استدعاء دالة الشراء من الملف الجديد
from shopping_cart import start_shopping 

products = [
    {"name": "Water", "price": 80.0, "quantity": 1500},
    {"name": "Soda",  "price": 130.0, "quantity": 1500},
    {"name": "Chips", "price": 50.0,  "quantity": 200}, # منتجات إضافية للتجربة
    {"name": "Bread", "price": 45.0,  "quantity": 100}
]

if __name__ == "__main__":
    is_logged_in = log()
    
    if is_logged_in:
        print("Loading Data...")
        
        # عرض المنتجات
        display_table(products)
        
        # 2. بدء عملية الشراء
        start_shopping(products)
        
        # (اختياري) عرض الجدول مرة أخرى لرؤية الكميات بعد التحديث
        print("\n--- Updated Inventory ---")
        display_table(products)
        
    else:
        print("Access Denied.")