def get_emails(list_contacts):
    res = []
    for i in map(lambda e: e['email'], list_contacts):
        res.append(i)
    return res