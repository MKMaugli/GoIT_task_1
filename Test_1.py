DEFAULT_DISCOUNT = 0.05


def get_discount_price_customer(price, customer):
    if "discount" in customer:
        cust_dis = customer.get("discount")
        return price * (1-cust_dis)
    return price * (1-DEFAULT_DISCOUNT)