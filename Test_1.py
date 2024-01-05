def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
    sanitized_numbers = [sanitize_phone_number(phone) for phone in list_phones]
    
    phone_dict = {"UA": [], "JP": [], "TW": [], "SG": []}
    
    for phone in sanitized_numbers:
        if phone.startswith("380") or phone.startswith("0"):
            phone_dict["UA"].append(phone)
        elif phone.startswith("81"):
            phone_dict["JP"].append(phone)
        elif phone.startswith("886"):
            phone_dict["TW"].append(phone)
        elif phone.startswith("65"):
            phone_dict["SG"].append(phone)
    
    return phone_dict

# Виклик функції з вхідними даними
#input_numbers = ['', '818765347', '8867658976', '657658976']
input_numbers = ['0658759411', '380998759405', '818765347', '818765344', '8867658976', '657658976']
result_dict = get_phone_numbers_for_countries(input_numbers)
print(result_dict)

