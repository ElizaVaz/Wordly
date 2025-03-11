from random import choise

print("Hi!")
print("Ваше слово:")
with open("russian_dict.json") as f:
    print(choise(list(json.load(f))))
