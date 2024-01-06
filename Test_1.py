def format_phone_number(func):
    def wrapper (phone):
        res = func(phone)
        lenres = len(res)
        if lenres == 12:
            return '+' + res
        elif lenres < 12:
            return '+38' + res
    return wrapper
     

@format_phone_number
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