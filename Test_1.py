def cost_delivery(quantity, *numbers, discount=0):
    """Функция возвращает общую сумму доставки.

        Первый параметр &mdash; количество товаров в заказе.
        Параметр скидки discount, передаваемый только по ключу, по умолчанию имеет значение 0."""

    if discount == 0:
        result = 5+((quantity-1)*2)
        return result
    else:
        result = (5+((quantity-1)*2))*discount
        return result

print(cost_delivery.__doc__)
print(cost_delivery(2, 1, 2, 3, discount=0.5))



