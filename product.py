import pickle

class Product:
    def __init__(self, name, manufacturer, type_number, project, order_processor, date_of_purchase, storage_period, value_before_tax, tax_rate):
        self.name = name
        self.manufacturer = manufacturer
        self.type_number = type_number
        self.project = project
        self.order_processor = order_processor
        self.date_of_purchase = date_of_purchase
        self.storage_period = storage_period
        self.value_before_tax = value_before_tax
        self.tax_rate = tax_rate

    def calculate_taxable_value(self):
        return self.value_before_tax * (1 + self.tax_rate / 100)

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def modify_product(self, type_number, updated_product):
        for i, product in enumerate(self.products):
            if product.type_number == type_number:
                self.products[i] = updated_product
                return True
        return False

    def delete_product(self, type_number):
        self.products = [p for p in self.products if p.type_number != type_number]

    def search_product(self, keyword):
        return [p for p in self.products if keyword.lower() in p.name.lower()]

    def export_to_excel(self, filename):
        data = {
            "Name": [p.name for p in self.products],
            "Manufacturer": [p.manufacturer for p in self.products],
            "Type Number": [p.type_number for p in self.products],
            "Project": [p.project for p in self.products],
            "Order Processor": [p.order_processor for p in self.products],
            "Date of Purchase": [p.date_of_purchase for p in self.products],
            "Storage Period": [p.storage_period for p in self.products],
            "Value Before Tax": [p.value_before_tax for p in self.products],
            "Tax Rate": [p.tax_rate for p in self.products],
            "Taxable Value": [p.calculate_taxable_value() for p in self.products],
        }
        with open(filename, 'w') as file:
            file.write(str(data))

    def save_to_file(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.products, f)

    def load_from_file(self, filename):
        try:
            with open(filename, 'rb') as f:
                self.products = pickle.load(f)
        except FileNotFoundError:
            print("No previous data found, starting fresh.")
        except Exception as e:
            print(f"An error occurred while loading data: {e}")
