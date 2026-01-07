from prettytable import PrettyTable

def display_table(data_list):
    table = PrettyTable()
    table.field_names = ["Product Name", "Price ($)", "Quantity"]
    
    for item in data_list:
        table.add_row([
            item["name"], 
            f"{item['price']:.2f}", # Format decimal
            item["quantity"]
        ])
        
    print(table)