def update_stock(stock, product_id, quantity):
    stock[product_id] = stock.get(product_id, 0) + quantity

def check_stock(stock, product_id):
    return stock.get(product_id, 0)
