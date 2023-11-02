def get_fullname (first_name, last_name, middle_name=''):
    if middle_name == '':
        f'{first_name} {middle_name} {last_name}'
    else:
        f'{first_name} {last_name}'


print(get_fullname ("Petro", "Zaliznyak"))