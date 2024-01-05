import re

def find_all_emails(text):
    pattern = r"[a-zA-Z]{1}[\w\.]+@[a-zA-z]+\.[a-zA-z]{2,}"

    result = re.findall(pattern, text)
    return result


# Приклад використання
text = "Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net"
emails = find_all_emails(text)
print(emails)
