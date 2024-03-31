from flask import Flask, request, jsonify, render_template
import products_dao
from sql_connection import get_sql_connection

app = Flask(__name__)

connection = get_sql_connection()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/manage_products')
def manage_products():
    # Assuming you have a function to get products data
    connection = get_sql_connection()
    # This is a placeholder function call - replace with actual function from products_dao
    products = []  # Replace with actual data retrieval logic
    return render_template('manage_product.html', products=products)

@app.route('/orders')
def orders():
    # You would likely fetch orders from your database here
    # For now, this just renders the orders page
    return render_template('order.html')

@app.route('/getproducts', methods=['GET'])
def get_products():
    products = products_dao.get_all_products(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

   





if __name__=="__main__":
    print("Starting Python Flask Server For Grocery Store Management System")
    app.run(port=5000)



