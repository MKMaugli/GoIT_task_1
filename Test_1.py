def discount_price(price, discount):
    float(price)
    float(discount)         #= float(input("Enter the discount: "))
    
    def apply_discount():
        nonlocal price
        price = (price*(1-discount))

    apply_discount()
    return price

discount_price(100, 0.1)
print(discount_price)