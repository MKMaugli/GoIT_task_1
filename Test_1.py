import json

def write_contacts_to_file(filename, contacts):
    with open(filename, "w") as fw:
        json.dump({'contacts' : (contacts)}, fw)

def read_contacts_from_file(filename):
    with open(filename, "r") as fr:
        res = json.load(fr)
    return res['contacts']