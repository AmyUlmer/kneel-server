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
    return ORDERS

def get_single_order(id):
    # Variable to hold the found order, if it exists
    requested_order = None

    # Iterate the ORDERS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for order in ORDERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if order["id"] == id:
            requested_order = order

    return requested_order

def create_order(order):
    """function--take new dictionary representation sent by the client
        and append it to the LOCATIONS list"""
    # Get the id value of the last order in the list
    max_id = ORDERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the order dictionary
    order["id"] = new_id

    # Add the order dictionary to the list
    ORDERS.append(order)

    # Return the dictionary with `id` property added
    return order

def delete_order(id):
    """DELETE order"""
    # Initial -1 value for order index, in case one isn't found
    order_index = -1

    # Iterate the ORDERS list, but use enumerate() so that you
    # can access the index value of each item
    # enumerate allows you to loop thru element and index at same time
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            # Found the animal. Store the current index.
            order_index = index

    # If the animal was found, use pop(int) to remove it from list
    if order_index >= 0:
        ORDERS.pop(order_index)

def update_order(id, new_order):
    """UPDATE order"""
    #function iterates list of orders until it finds right one
    #then, replaces it with what the client sent as the replacement"""
    # Iterate the ORDERS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            # Found the animal. Update the value.
            ORDERS[index] = new_order
            break