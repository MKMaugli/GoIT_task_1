import csv


def write_contacts_to_file(filename, contacts):
    print(contacts)
    with open(filename, 'w', newline='') as cw:
        titles = []
        for title in contacts[0].keys():
            titles.append(title)
        field_title = titles
        writer = csv.DictWriter(cw, fieldnames = field_title)
        writer.writeheader()
        for element in contacts:
            writer.writerow(element)
    

def read_contacts_from_file(filename):
    result = []
    with open(filename, 'r', newline='') as cr:
        reader = csv.DictReader(cr)
        for row in reader:
            dict_item = {}
            for key, val in row.items():
                if val == 'True':
                    val = True
                elif val == 'False':
                    val = False
                dict_item.update({key: val})
            result.append(dict_item)
    return result