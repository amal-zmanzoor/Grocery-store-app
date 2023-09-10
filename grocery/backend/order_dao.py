# Writing a function to insert an order
from sql_connection import get_sql_connection
from datetime import datetime

def insert_order(connection, order):
    cursor = connection.cursor()
    order_query = ("INSERT INTO orders "
                   "(customer_name, total, date)"
                   "VALUES (%s, %s, %s)")
    order_data = (order['customer_name'], order['grand_total'], datetime.now())

    # Inserting one record
    cursor.execute(order_query, order_data)
    order_id = cursor.lastrowid

    order_details_query = ("INSERT INTO order_details "
                            "(order_id, product_id, quantity, total_price)"
                            "VALUES (%s, %s, %s, %s)")
    order_details_data = []
    for order_detail_record in order['order_details']:
        # Inserting many records
        # Each record in the order_details_data list has an order_id, product_id, quantity, total_price
        order_details_data.append([
            order_id,
            int(order_detail_record['product_id']),
            float(order_detail_record['quantity']),
            float(order_detail_record['total_price'])
        ])
    
    cursor.executemany(order_details_query, order_details_data)

    connection.commit()

    return order_id

if __name__ == '__main__':
    connection = get_sql_connection()
    print(insert_order(connection,{
        # Place an order which will be a dictionary
        'customer_name': 'Hulk',
        'grand_total': '500',
        'order_details': [
            {
                'product_id': 1,
                'quantity': 2,
                'total_price': 50
            },
            {
                'product_id': 3,
                'quantity': 1,
                'total_price': 30
            },
        ]

    }))