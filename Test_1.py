def get_favorites(contacts):
    res = []
    for i in filter(lambda c: c["favorite"] == True, contacts):
        res.append(i)
    return res