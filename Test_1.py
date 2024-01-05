articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
    result_articles = []

    for article in articles_dict:
        author_names = article['author'].split()
        title = article['title']

        if not letter_case:
            key = key.lower()
            author_names = [name.lower() for name in author_names]
            title = title.lower()

        if any(key in name for name in author_names) or key in title:
            result_articles.append({
                'author': article['author'],
                'title': article['title'],
                'year': article['year']
            })

    return result_articles


# Пример вызова
articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]

key_to_find = "Ocean"
found_articles = find_articles(key_to_find, letter_case=True)
print(found_articles)