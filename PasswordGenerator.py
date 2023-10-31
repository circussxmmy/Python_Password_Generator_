import random
import string
import secrets

upper = string.ascii_uppercase
lower = string.ascii_lowercase
special = string.punctuation
digits = string.digits

upper_count, lower_count, digits_count, special_count = 100, 100, 100, 100
length = 20
all_characters = (upper * upper_count) + (lower * lower_count) + (special * special_count) + (digits * digits_count)

PasswordGen = "" .join(random.choice(all_characters) for _ in range(length))
print(PasswordGen)
