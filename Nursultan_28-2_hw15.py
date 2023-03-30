import sqlite3


def create_table():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS products
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_title TEXT NOT NULL,
                price NUMERIC(10, 2) NOT NULL DEFAULT 0.0,
                quantity INTEGER NOT NULL DEFAULT 0)''')

    conn.commit()
    conn.close()


def add_products():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    products = [('Товар 1', 99.99, 10), ('Товар 2', 49.99, 20), ('Товар 3', 9.99, 30),
                ('Товар 4', 29.99, 5), ('Товар 5', 19.99, 0), ('Товар 6', 49.99, 15),
                ('Товар 7', 9.99, 25), ('Товар 8', 59.99, 3), ('Товар 9', 79.99, 7),
                ('Товар 10', 99.99, 2), ('Товар 11', 39.99, 5), ('Товар 12', 29.99, 10),
                ('Товар 13', 89.99, 8), ('Товар 14', 9.99, 100), ('Товар 15', 49.99, 0)]

    cursor.executemany('''INSERT INTO products (product_title, price, quantity)
                        VALUES (?, ?, ?)''', products)

    conn.commit()
    conn.close()


def update_quantity_by_id(product_id, new_quantity):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('''UPDATE products SET quantity = ? WHERE id = ?''', (new_quantity, product_id))

    conn.commit()
    conn.close()


def update_price_by_id(product_id, new_price):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('''UPDATE products SET price = ? WHERE id = ?''', (new_price, product_id))

    conn.commit()
    conn.close()


def delete_product_by_id(product_id):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('''DELETE FROM products WHERE id = ?''', (product_id,))

    conn.commit()
    conn.close()


def select_all_products():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('''SELECT * FROM products''')

    products = cursor.fetchall()

    for product in products:
        print(product)

    conn.close()


def select_products_by_price_and_quantity():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('''SELECT * FROM products WHERE price < 100.0 AND quantity > 5''')

    products = cursor.fetchall()

    for product in products:
        print(product)

    conn.close()


def search_products_by_title(search_term):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('''SELECT * FROM products WHERE product_title LIKE ?''', ('%' + search_term + '%',))

    products = cursor.fetchall()

    for product in products:
        print(product)

    conn.close()


if __name__ == '__main__':
    create_table()
    add_products()

