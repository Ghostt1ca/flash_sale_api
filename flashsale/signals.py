from django.dispatch import Signal, receiver

stock_zero = Signal()  # signal custom

@receiver(stock_zero)
def alertStock(sender, product_name, **kwargs):
    print(f"ALERT: Product {product_name} has reached 0 stock!")
