import psycopg2
from sql_connection import get_sql_connection
'''
# Connection parameters
user="postgres",
password="Ethio#2014",
host="127.0.0.1",
port=5432,
database="grocery_store"
'''

import psycopg2

def get_all_products(connection):
    # Establish the connection
    '''
    connection = psycopg2.connect(
        user='postgres',
        password='Ethio#2014',
        host='127.0.0.1',
        port=5432,
        database='grocery_store'
    )
    '''
    # Create a cursor object
    cursor = connection.cursor()
    query = ("SELECT products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name "
             "FROM products INNER JOIN uom ON uom.uom_id = products.uom_id")

    # Execute the query
    cursor.execute(query)

    # Initialize response list
    response = []

    # Fetch the results
    records = cursor.fetchall()  # Fetch all results at once

    for record in records:  # Iterate over the fetched records
        product_id, name, uom_id, price_per_unit, uom_name = record  # Unpack the record tuple
        response.append({
            'product_id': product_id,
            'name': name,
            'uom_id': uom_id,
            'price_per_unit': price_per_unit,  # Corrected typo from 'price_pre_unit' to 'price_per_unit'
            'uom_name': uom_name
        })

    # Close the cursor and connection
    cursor.close()
    connection.close()

    return response

def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO products (product_id,name, uom_id, price_per_unit)"
             "VALUES (%s, %s, %s, %s)")
    data = (product['product_id'], product['name'], product['uom_id'], product['price_per_unit'])
    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid


def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products WHERE product_id =" + str(product_id))
    cursor.execute(query)
    connection.commit()

if __name__ == '__main__':
    connection = get_sql_connection()
    print(delete_product(connection, 7))

   



    
