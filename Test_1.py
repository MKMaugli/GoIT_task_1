def positive_values(list_payment):
    res = []
    for i in filter(lambda p: p > 0, list_payment):
        res.append(i)
    return res