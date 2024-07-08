import pickle
from product import Product, export_to_excel

def load_data(filename='inventory_data.pkl'):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        print("No previous data found, starting fresh.")
        return []

def save_data(products, filename='inventory_data.pkl'):
    with open(filename, 'wb') as file:
        pickle.dump(products, file)

def display_totals(products):
    total_tax_free = sum(p.value_before_tax for p in products)
    total_taxable = sum(p.taxable_value for p in products)
    print(f"Total Value Before Tax: {total_tax_free}")
    print(f"Total Taxable Value: {total_taxable}")

def sort_and_display(products):
    sort_key = input("Enter the field to sort by (e.g., Name, Location, Project): ")
    sorted_products = sorted(products, key=lambda p: getattr(p, sort_key.lower(), ''))
    for product in sorted_products:
        print(product.to_dict())
    display_totals(products)

def main():
    products = load_data()

    while True:
        print("Digiteam Inventory Management")
        print("1. Add Product")
        print("2. Modify Product")
        print("3. Delete Product")
        print("4. Search Product")
        print("5. Export to Excel")
        print("6. Sort and Display Products")
        print("7. Save and Exit")
        print("8. Exit without Saving")

        choice = input("Enter your choice: ")
        print(f"User selected choice: {choice}")

        if choice == '1':
            name = input("Enter product name: ")
            manufacturer = input("Enter manufacturer: ")
            type_number = input("Enter type number: ")
            project = input("Enter project: ")
            order_processor = input("Enter order processor: ")
            date_of_purchase = input("Enter date of purchase (YYYY-MM-DD): ")
            storage_period = int(input("Enter storage period (years): "))
            value_before_tax = float(input("Enter value before tax: "))
            tax_rate = float(input("Enter tax rate (%): "))
            location = input("Enter location (e.g., office, Vaste-locker): ")
            product = Product(name, manufacturer, type_number, project, order_processor, date_of_purchase, storage_period, value_before_tax, tax_rate, location)
            products.append(product)
            print("Product added successfully.")

        elif choice == '2':
            type_number = input("Enter the type number of the product to modify: ")
            product = next((p for p in products if p.type_number == type_number), None)
            if product:
                product.name = input(f"Enter new name ({product.name}): ") or product.name
                product.manufacturer = input(f"Enter new manufacturer ({product.manufacturer}): ") or product.manufacturer
                product.project = input(f"Enter new project ({product.project}): ") or product.project
                product.order_processor = input(f"Enter new order processor ({product.order_processor}): ") or product.order_processor
                product.date_of_purchase = input(f"Enter new date of purchase ({product.date_of_purchase}): ") or product.date_of_purchase
                product.storage_period = int(input(f"Enter new storage period ({product.storage_period}): ") or product.storage_period)
                product.value_before_tax = float(input(f"Enter new value before tax ({product.value_before_tax}): ") or product.value_before_tax)
                product.tax_rate = float(input(f"Enter new tax rate ({product.tax_rate}): ") or product.tax_rate)
                product.location = input(f"Enter new location ({product.location}): ") or product.location
                product.taxable_value = product.value_before_tax * (1 + product.tax_rate / 100)
                print("Product modified successfully.")
            else:
                print("Product not found.")

        elif choice == '3':
            type_number = input("Enter the type number of the product to delete: ")
            products = [p for p in products if p.type_number != type_number]
            print("Product deleted successfully.")

        elif choice == '4':
            search_term = input("Enter product name or type number to search: ")
            found_products = [p for p in products if p.name == search_term or p.type_number == search_term]
            for product in found_products:
                print(product.to_dict())

        elif choice == '5':
            export_to_excel(products)
            print("Data exported to Excel successfully.")

        elif choice == '6':
            sort_and_display(products)

        elif choice == '7':
            save_data(products)
            print("Data saved successfully. Exiting the program.")
            break

        elif choice == '8':
            print("Exiting the program without saving.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
