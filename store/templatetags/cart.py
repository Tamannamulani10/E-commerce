from django import template

register= template.Library()

@register.filter(name='is_in_cart')

def is_in_cart(product,cart):
    if hasattr(product, 'id'):
        try:
            product_id = str(int(product.id))  # Ensure product_id is a string of an integer
        except (ValueError, TypeError):
            print(f"Invalid product id: {product.id}")
            return False
    for id in cart.keys():
        try:
            if id == product_id:  # Compare string to string
                return True
        except (ValueError, TypeError):
            print(f"Invalid cart id: {id}")
            continue

    print(f"Product: {product}, Cart: {cart}")
    return False


@register.filter(name= 'cart_quantity')
def cart_quantity(product,cart):
        return cart.get(str(product.id), 0)



@register.filter(name= 'price_total')
def price_total(product,cart):
     return product.price * cart_quantity(product,cart)


@register.filter(name='total_cart_price')
def total_cart_price(products,cart):
    sum= 0 ;
    for p in products:
        sum += price_total(p, cart)
    return sum