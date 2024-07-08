from product import Product, Inventory

def display_menu():
    print("Digiteam Inventory Management")
    print("1. Add Product")
    print("2. Modify Product")
    print("3. Delete Product")
    print("4. Search Product")
    print("5. Export to Excel")
    print("6. Save and Exit")
    print("7. Exit without Saving")

def get_product_details():
    print("Getting product details from user...")
    name = input("Enter product name: ")
    manufacturer = input("Enter manufacturer: ")
    type_number = input("Enter type number: ")
    project = input("Enter project: ")
    order_processor = input("Enter order processor: ")
    date_of_purchase = input("Enter date of purchase (YYYY-MM-DD): ")
    storage_period = int(input("Enter storage period (years): "))
    value_before_tax = float(input("Enter value before tax: "))
    tax_rate = float(input("Enter tax rate (%): "))
    print("Product details collected.")
    return Product(name, manufacturer, type_number, project, order_processor, date_of_purchase, storage_period, value_before_tax, tax_rate)

def main():
    print("Starting Inventory Management CLI")
    inventory = Inventory()
    inventory.load_from_file('inventory_data.pkl')

    while True:
        display_menu()
        choice = input("Enter your choice: ")
        print(f"User selected choice: {choice}")

        if choice == '1':
            product = get_product_details()
            inventory.add_product(product)
            print("Product added successfully.")

        elif choice == '2':
            type_number = input("Enter type number of the product to modify: ")
            updated_product = get_product_details()
            if inventory.modify_product(type_number, updated_product):
                print("Product modified successfully.")
            else:
                print("Product not found. Modification failed.")

        elif choice == '3':
            type_number = input("Enter type number of the product to delete: ")
            inventory.delete_product(type_number)
            print("Product deleted successfully.")

        elif choice == '4':
            keyword = input("Enter keyword to search: ")
            found_products = inventory.search_product(keyword)
            if found_products:
                for product in found_products:
                    print(f"Name: {product.name}, Type Number: {product.type_number}, Project: {product.project}")
            else:
                print("No products found matching the keyword.")

        elif choice == '5':
            file_name = input("Enter the filename to export (with .xlsx extension): ")
            inventory.export_to_excel(file_name)
            print("Data exported to Excel successfully.")

        elif choice == '6':
            inventory.save_to_file('inventory_data.pkl')
            print("Data saved successfully. Exiting the program.")
            break

        elif choice == '7':
            print("Exiting the program without saving.")
            break

        else:
            print("Invalid choice. Please try again.")

    # Ensure to save data before exiting
    inventory.save_to_file('inventory_data.pkl')

if __name__ == "__main__":
    main()
