import random

def get_random_winners(quantity, participants):
    res = []
    if quantity > len(participants):
        return res
    keys = []
    for key in participants.keys():
        keys.append(key)

    random.shuffle(keys)
    res = random.sample(keys, k=quantity)
    return res

# Приклад використання:
participants = {
    "603d2cec9993c627f0982404": "test@test.com",
    "603f79022922882d30dd7bb6": "test11@test.com",
    "60577ce4b536f8259cc225d2": "test2@test.com",
    "605884760742316c07eae603": "vitanlhouse@gmail.com",
    "605b89080c318d66862db390": "elhe2013@gmail.com",
}

quantity = 2
result = get_random_winners(quantity, participants)
print(result)
