def add_product(products, product_id, name, price):
    products.append({"id": product_id, "name": name, "price": price})

def list_products(products):
    for p in products:
        print(p)
