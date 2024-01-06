from setuptools import setup

def do_setup(args_dict, requires):
    setup(
        name=args_dict['name'],
        version=args_dict['version'],
        description=args_dict['description'],
        url=args_dict['url'],
        author=args_dict['author'],
        author_email=args_dict['author_email'],
        license=args_dict['license'],
        packages=args_dict['packages'],
        install_requires=requires  # Добавлен новый параметр
    )

# Пример использования:
my_args_dict = {
    "name": "useful",
    "version": "1",
    "description": "Very useful code",
    "url": "http://github.com/dummy_user/useful",
    "author": "Flying Circus",
    "author_email": "flyingcircus@example.com",
    "license": "MIT",
    "packages": ["useful"],
}

my_requires = ["dependency1", "dependency2"]

do_setup(my_args_dict, my_requires)
