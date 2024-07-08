import datetime
import pandas as pd

class Product:
    def __init__(self, name, manufacturer, type_number, project, order_processor, date_of_purchase, storage_period, value_before_tax, tax_rate, location):
        self.name = name
        self.manufacturer = manufacturer
        self.type_number = type_number
        self.project = project
        self.order_processor = order_processor
        self.date_of_purchase = datetime.datetime.strptime(date_of_purchase, '%Y-%m-%d').date()
        self.storage_period = storage_period
        self.value_before_tax = value_before_tax
        self.tax_rate = tax_rate
        self.location = location
        self.taxable_value = self.value_before_tax * (1 + self.tax_rate / 100)

    def to_dict(self):
        return {
            'Name': self.name,
            'Manufacturer': self.manufacturer,
            'Type Number': self.type_number,
            'Project': self.project,
            'Order Processor': self.order_processor,
            'Date of Purchase': self.date_of_purchase.strftime('%Y-%m-%d'),
            'Storage Period (years)': self.storage_period,
            'Value Before Tax': self.value_before_tax,
            'Tax Rate (%)': self.tax_rate,
            'Taxable Value': self.taxable_value,
            'Location': self.location
        }

    def __repr__(self):
        return f"Product(Name='{self.name}', Manufacturer='{self.manufacturer}', Type Number='{self.type_number}', Project='{self.project}', " \
               f"Order Processor='{self.order_processor}', Date of Purchase='{self.date_of_purchase.strftime('%Y-%m-%d')}', " \
               f"Storage Period (years)={self.storage_period}, Value Before Tax={self.value_before_tax}, Tax Rate (%)={self.tax_rate}, " \
               f"Taxable Value={self.taxable_value}, Location='{self.location}')"

def export_to_excel(products, filename='inventory.xlsx'):
    df = pd.DataFrame([product.to_dict() for product in products])
    df.to_excel(filename, index=False)

if __name__ == "__main__":
    # Example usage for testing purposes
    product = Product('Laptop', 'Lenovo', '12345', 'Project X', 'John Doe', '2023-01-15', 3, 800.0, 10.0, 'office')
    print(product)
    print(product.to_dict())
