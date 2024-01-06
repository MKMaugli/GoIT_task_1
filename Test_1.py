class IDException(Exception):
    pass


def add_id(id_list, employee_id):
    if employee_id.find("01", 0, 2) != -1:
        id_list.append(employee_id)
        return id_list
    else:
        raise IDException