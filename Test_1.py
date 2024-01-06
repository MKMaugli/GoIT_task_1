def normal_name(list_name):
    res = []
    for i in map(lambda v: v.capitalize(), list_name):
        res.append(i)
    return res