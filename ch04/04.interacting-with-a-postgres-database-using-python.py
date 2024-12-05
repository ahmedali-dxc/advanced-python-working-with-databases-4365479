import psycopg2

def insert_sale(_cursor, _order_num, _cust_name, _prod_number, _prod_name, _quantity, _price, _discount):
    order_total = _quantity * _price
    if _discount != 0:
        order_total = order_total * _discount

    sales_data = {
        'order_num': _order_num,
        'cust_name': _cust_name,
        'prod_number': _prod_number,
        'prod_name': _prod_name,
        'quantity': _quantity,
        'price': _price,
        'discount': _discount,
        'order_total': order_total
    }

    _cursor.execute('''INSERT INTO SALES VALUES (%(order_num)s, %(cust_name)s, %(prod_number)s, %(prod_name)s, 
                    %(quantity)s, %(price)s, %(discount)s, %(order_total)s)''', sales_data)

if __name__ == "__main__":
    conn = psycopg2.connect(database="red30", user="postgres", password="postgres", host="localhost", port="5432")
    cursor = conn.cursor()

    print("Input sale data:\n")
    order_num = int(input("What is the order number?\n"))
    cust_name = input("What is the customer name?\n")
    prod_number = input("What is the product number?\n")
    prod_name = input("What is the product name?\n")
    quantity = int(input("How many were bought?\n"))
    price = float(input("What is the price of the product?\n"))
    discount = float(input("What is the discount, if there is one?\n"))

    print("Inputting sale data:\n")
    insert_sale(cursor, order_num, cust_name, prod_number, prod_name, quantity, price, discount)

    conn.commit()
    conn.close()