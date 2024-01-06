import pickle


def write_contacts_to_file(filename, contacts):
    with open(filename, "wb") as fw:
        pickle.dump(contacts, fw)
        


def read_contacts_from_file(filename):
    with open(filename, "rb") as fr:
        unp = pickle.load(fr)
    return unp