import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template, request, redirect, url_for, flash
import pickle
from product import Product, export_to_excel

app = Flask(__name__)
app.secret_key = 'supersecretkey'

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

@app.route('/')
def index():
    products = load_data()
    return render_template('index.html', products=products)

@app.route('/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        manufacturer = request.form['manufacturer']
        type_number = request.form['type_number']
        project = request.form['project']
        order_processor = request.form['order_processor']
        date_of_purchase = request.form['date_of_purchase']
        storage_period = int(request.form['storage_period'])
        value_before_tax = float(request.form['value_before_tax'])
        tax_rate = float(request.form['tax_rate'])
        location = request.form['location']
        
        product = Product(name, manufacturer, type_number, project, order_processor, date_of_purchase, storage_period, value_before_tax, tax_rate, location)
        
        products = load_data()
        products.append(product)
        save_data(products)
        
        flash('Product added successfully!')
        return redirect(url_for('index'))
    
    return render_template('add_product.html')

@app.route('/modify/<type_number>', methods=['GET', 'POST'])
def modify_product(type_number):
    products = load_data()
    product = next((p for p in products if p.type_number == type_number), None)
    
    if request.method == 'POST':
        if product:
            product.name = request.form['name']
            product.manufacturer = request.form['manufacturer']
            product.project = request.form['project']
            product.order_processor = request.form['order_processor']
            product.date_of_purchase = request.form['date_of_purchase']
            product.storage_period = int(request.form['storage_period'])
            product.value_before_tax = float(request.form['value_before_tax'])
            product.tax_rate = float(request.form['tax_rate'])
            product.location = request.form['location']
            product.taxable_value = product.value_before_tax * (1 + product.tax_rate / 100)
            
            save_data(products)
            flash('Product modified successfully!')
            return redirect(url_for('index'))
    
    return render_template('modify_product.html', product=product)

@app.route('/delete/<type_number>')
def delete_product(type_number):
    products = load_data()
    products = [p for p in products if p.type_number != type_number]
    save_data(products)
    flash('Product deleted successfully!')
    return redirect(url_for('index'))

@app.route('/export')
def export():
    products = load_data()
    export_to_excel(products)
    flash('Data exported to Excel successfully!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
