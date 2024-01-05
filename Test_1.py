import re

def find_all_links(text):
    pattern = r'https?://(?:www\.)?[a-zA-Z][a-zA-Z0-9]+\.[a-zA-Z]{2,}(?=\s|$)'
    result = [match.group() for match in re.finditer(pattern, text)]
    return result


# Приклад використання
text = "The main search site in the world is https://www.google.com The main social network for people in the world is https://www.facebook.com But programmers have their own social network http://github.com There they share their code. some url to check https://www..facebook.com www.facebook.com "
links = find_all_links(text)
print(links)
