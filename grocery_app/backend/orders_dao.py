

def insert_order(connection, order):
    cursor = connection.cursor()
    #test

if __name__ == '__name__':
    connection = get_sql_connection()
    print(insert_order(connection, {
        'costumer_name': 'dhaval',
        'grand_total': '500,'
        'datetime': datetime.now(),
        'order_details': [
            {
                'product_id': 1,
                'quantity': 2,
                'total_price':50
            },
            {
                'product_id': 3,
                'quantity': 1,
                'total_price':30
            },
        ]
    }))