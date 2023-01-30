import sqlite3
import json
# import the Orders class so that you can create instances of it for each row of data that gets returned from the database.
from models import Orders, Metal, Size, Style

ORDERS = [
    {
        "id": 1,
        "metalId": 3,
        "sizeId": 2,
        "styleId": 3,
        "timestamp": 1614659931693
    },
    {
        "id": 2,
        "metalId": 1,
        "sizeId": 3,
        "styleId": 2,
        "timestamp": 1614659931693
    }
]


def get_all_orders():
    """Returns list of dictionaries stored in ORDERS variable"""
    # Open a connection to the database
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

    # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            o.id,
            o.metal_id,
            o.size_id,
            o.style_id,
            o.timestamp
            m.metal metals_metal,
            m.price metals_price,
            s.carets sizes_carets,
            s.price sizes_price,
            t.style styles_style,
            t.price styles_price
        FROM orders o
        JOIN Metals m 
        ON m.id = o.metal_id
        JOIN Sizes s 
        ON s.id = o.size_id
        JOIN Styles t
        ON t.id = o.style_id
        """)

        # Initialize an empty list to hold all order representations
        orders = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an order instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Order class above.
            order = Orders(row['id'], row['metal_id'], row['size_id'], 
                            row['style_id'], row['timestamp'])
            
            metal = Metal(row['id'], row['metals_metal'], row['metals_price'])
            
            del metal.id

            size = Size(row['id'], row['sizes_carets'], row['sizes_price'])

            del size.id

            style = Style(row['id'], row['styles_style'], row['styles_price'])

            del style.id

            order.metal = metal.__dict__

            order.size = size.__dict__

            order.style = style.__dict__


            orders.append(order.__dict__)
                            

            orders.append(order.__dict__)

    return orders

def get_single_order(id):
    """Returns dictionary of single order from list stored in ORDERS"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            o.id,
            o.metal_id,
            o.size_id,
            o.style_id,
            o.timestamp
        FROM orders o
        WHERE o.id = ?
        """, (id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        order = Orders(data['id'], data['metal_id'], data['size_id'], 
                            data['style_id'], data['timestamp'])

        return order.__dict__

def create_order(new_order):
    """Returns new dictionary with id property added"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Orders
            ( metal_id, size_id, style_id, timestamp )
        VALUES
            ( ?, ?, ?, ?);
        """, (new_order['metalId'], new_order['sizeId'], new_order['styleId'], new_order['timestamp']))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the order dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_order['id'] = id

    return new_order

def delete_order(id):
    """Deletes a single order by id."""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM orders
        WHERE id = ?
        """, (id, ))

def update_order(id, new_order):
    """UPDATE order"""
    #function iterates list of orders until it finds right one
    #then, replaces it with what the client sent as the replacement"""
    # Iterate the ORDERS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            # Found the order. Update the value.
            ORDERS[index] = new_order
            break