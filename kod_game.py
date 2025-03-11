from random import choice

print("Hi!")
print("Ваше слово:")
with open("russian_dict", "r", encoding="utf-8") as f:
    print(choice(f.readlines()))
