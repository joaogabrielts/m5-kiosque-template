from menu import products
from collections import Counter


def get_product_by_id(product_id: int) -> dict:
    if not isinstance(product_id, int):
        raise TypeError("product id must be an int")
    
    for product in products:
        if product['_id'] == product_id:
            return product
    return {} 


def get_products_by_type(product_type: str) -> list:
    if not isinstance(product_type, str):
        raise TypeError("product type must be a str")
    
    return [product for product in products if product['type'] == product_type]


def add_product(menu: list, **product_data):
    new_id = max((item["_id"] for item in menu), default=0) + 1
    product_data["_id"] = new_id
    menu.append(product_data)
    return product_data


def calculate_tab(consumption: list):
    product_dict = {item["_id"]: item for item in products}
    subtotal = sum(product_dict[item["_id"]]
                   ["price"] * item["amount"] for item in consumption)
    return {"subtotal": f"${round(subtotal, 2)}"}


def menu_report():
    product_count = len(products)
    average_price = round(
        sum(item["price"] for item in products) / product_count, 2
    ) if product_count else 0
    most_common_type = Counter(
        item["type"] for item in products
    ).most_common(1)
    most_common_type = most_common_type[0][0] if most_common_type else "N/A"
    
    return (
        f"Products Count: {product_count}\n"
        f"Average Price: ${average_price}\n"
        f"Most Common Type: {most_common_type}"
    )
