from menu import products

# #    print(products)


def get_product_by_id(product_id: int) -> dict:
    for product in products:
        if product['_id'] == product_id:
            return product
    return {}


def get_products_by_type(product_type: str) -> list:
    result = []
    for product in products:
        if product['type'] == product_type:
            result.append(product)
    return result


def add_product(menu: list, **product_data):

    new_id = max((item["_id"] for item in menu), default=0) + 1

    product_data["_id"] = new_id

    menu.append(product_data)

    return product_data


def calculate_tab(consumption: list):
    from menu import products 
    product_dict = {item["_id"]: item for item in products}
    subtotal = sum(product_dict[item["_id"]]["price"]
                   * item["amount"] for item in consumption)

    return {"subtotal": f"${round(subtotal, 2)}"}
