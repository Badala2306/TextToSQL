
import sqlite3

DATABASE = "ecommerce.db"


def create_database():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

    # 1. Customers
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY,
            customer_name TEXT NOT NULL,
            city TEXT NOT NULL,
            state TEXT NOT NULL,
            signup_date TEXT NOT NULL
        )
    """)

    # 2. Products
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY,
            product_name TEXT NOT NULL,
            category TEXT NOT NULL,
            unit_price REAL NOT NULL
        )
    """)

    # 3. Orders
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY,
            customer_id INTEGER NOT NULL,
            order_date TEXT NOT NULL,
            order_status TEXT NOT NULL,
            payment_method TEXT NOT NULL,
            FOREIGN KEY (customer_id)
                REFERENCES customers(customer_id)
        )
    """)

    # 4. Order Items
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS order_items (
            order_item_id INTEGER PRIMARY KEY,
            order_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            selling_price REAL NOT NULL,
            FOREIGN KEY (order_id)
                REFERENCES orders(order_id),
            FOREIGN KEY (product_id)
                REFERENCES products(product_id)
        )
    """)

    customers = [
        (1, "Aarav Mehta", "Delhi", "Delhi", "2023-01-10"),
        (2, "Diya Sharma", "Mumbai", "Maharashtra", "2023-02-14"),
        (3, "Kabir Singh", "Jaipur", "Rajasthan", "2023-03-05"),
        (4, "Ananya Gupta", "Pune", "Maharashtra", "2023-04-20"),
        (5, "Rohan Verma", "Bengaluru", "Karnataka", "2023-05-11"),
        (6, "Meera Patel", "Ahmedabad", "Gujarat", "2023-06-18"),
        (7, "Ishaan Kapoor", "Chandigarh", "Chandigarh", "2023-07-02"),
        (8, "Saanvi Joshi", "Hyderabad", "Telangana", "2023-08-25"),
        (9, "Arjun Reddy", "Hyderabad", "Telangana", "2023-09-15"),
        (10, "Kiara Malhotra", "Delhi", "Delhi", "2023-10-01"),
    ]

    products = [
        (1, "Laptop", "Electronics", 75000),
        (2, "Smartphone", "Electronics", 30000),
        (3, "Headphones", "Accessories", 2500),
        (4, "Mechanical Keyboard", "Accessories", 3500),
        (5, "Wireless Mouse", "Accessories", 1000),
        (6, "Monitor", "Electronics", 18000),
        (7, "Smartwatch", "Wearables", 8000),
        (8, "Tablet", "Electronics", 22000),
        (9, "Office Chair", "Furniture", 12000),
        (10, "Desk Lamp", "Furniture", 1800),
        (11, "Webcam", "Electronics", 4500),
        (12, "USB Hub", "Accessories", 1200),
    ]

    orders = [
        (101, 1, "2024-01-05", "Completed", "UPI"),
        (102, 2, "2024-01-12", "Completed", "Card"),
        (103, 3, "2024-01-20", "Completed", "UPI"),
        (104, 4, "2024-02-03", "Completed", "Net Banking"),
        (105, 5, "2024-02-15", "Completed", "Card"),
        (106, 6, "2024-02-22", "Cancelled", "UPI"),
        (107, 7, "2024-03-04", "Completed", "UPI"),
        (108, 8, "2024-03-16", "Completed", "Card"),
        (109, 9, "2024-03-21", "Completed", "Cash"),
        (110, 10, "2024-04-02", "Completed", "Card"),
        (111, 1, "2024-04-11", "Completed", "UPI"),
        (112, 2, "2024-04-19", "Returned", "Card"),
        (113, 3, "2024-05-06", "Completed", "Net Banking"),
        (114, 4, "2024-05-17", "Completed", "UPI"),
        (115, 5, "2024-06-08", "Completed", "Card"),
        (116, 6, "2024-06-21", "Completed", "UPI"),
        (117, 7, "2024-07-03", "Completed", "Cash"),
        (118, 8, "2024-07-14", "Cancelled", "Card"),
        (119, 9, "2024-08-09", "Completed", "UPI"),
        (120, 10, "2024-08-25", "Completed", "Net Banking"),
    ]

    order_items = [
        (1, 101, 1, 1, 73000),
        (2, 101, 3, 2, 2300),
        (3, 102, 2, 1, 29000),
        (4, 102, 7, 1, 7800),
        (5, 103, 4, 1, 3300),
        (6, 103, 5, 2, 950),
        (7, 104, 6, 1, 17500),
        (8, 104, 12, 2, 1100),
        (9, 105, 9, 1, 11500),
        (10, 105, 10, 2, 1700),
        (11, 106, 1, 1, 75000),
        (12, 106, 3, 1, 2500),
        (13, 107, 8, 1, 21500),
        (14, 107, 5, 1, 950),
        (15, 108, 2, 2, 28500),
        (16, 108, 11, 1, 4300),
        (17, 109, 7, 2, 7700),
        (18, 109, 3, 1, 2300),
        (19, 110, 1, 1, 74000),
        (20, 110, 6, 1, 17500),
        (21, 111, 2, 1, 29500),
        (22, 111, 4, 2, 3300),
        (23, 112, 8, 1, 22000),
        (24, 112, 12, 1, 1200),
        (25, 113, 9, 2, 11500),
        (26, 113, 10, 1, 1700),
        (27, 114, 6, 1, 18000),
        (28, 114, 11, 2, 4300),
        (29, 115, 3, 3, 2300),
        (30, 115, 5, 2, 950),
        (31, 116, 8, 1, 21500),
        (32, 116, 7, 1, 7800),
        (33, 117, 4, 2, 3300),
        (34, 117, 12, 3, 1100),
        (35, 118, 1, 1, 75000),
        (36, 118, 2, 1, 30000),
        (37, 119, 2, 1, 29000),
        (38, 119, 11, 1, 4300),
        (39, 120, 9, 1, 11500),
        (40, 120, 10, 2, 1700),
    ]

    cursor.executemany(
        "INSERT OR IGNORE INTO customers VALUES (?, ?, ?, ?, ?)",
        customers
    )

    cursor.executemany(
        "INSERT OR IGNORE INTO products VALUES (?, ?, ?, ?)",
        products
    )

    cursor.executemany(
        "INSERT OR IGNORE INTO orders VALUES (?, ?, ?, ?, ?)",
        orders
    )

    cursor.executemany(
        "INSERT OR IGNORE INTO order_items VALUES (?, ?, ?, ?, ?)",
        order_items
    )

    connection.commit()
    connection.close()


def execute_query(sql_query):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute(sql_query)
    result = cursor.fetchall()

    connection.commit()
    connection.close()

    return result
