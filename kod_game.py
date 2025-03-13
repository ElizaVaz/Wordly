from random import choice

print("Hi!")
print("Ваше слово:")



def word_regen1():
    global word
    with open("russian_dict", "r", encoding="utf-8") as f:
        word = choice(f.readlines()).strip("\n")


def word_regen2():
    global word
    with open("english_dict", "r", encoding="utf-8") as f:
        word = choice(f.readlines()).strip("\n")


glasn = ["а", "у", "о", "и", "э", "ы", "я", "ю", "е", "ё"]
soglasn = ["б", "в", "г", "д", "ж", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х"]
soglasn.extend(["ц", "ч", "ш", "щ", "ъ", "ь"])
bil = list()
print("Слово из каких letters you want gues? (введите 1, если на русском, 2 - на английском)")
language = input().strip()
while language != "1" and language != "2":
    print("У вас нет другого выбора, введите 1 или 2")
    language = input().strip("")


def help1():  # Инструкция что делать и как.
    print("Ваша цель угадать слово.")
    print("Для этого вам нужно ввести цыфру 4 и ввести предпологаемую букву.")
    print("Если вы забыли что вы вводили, то можете нажать 2 или 3.")
    print("Если вы догадываетесь что это за слово, то можете ввести 5 и")
    print("       попробовать угадать слово (без потери жизни)")
    print("(в остальных случаях вы теряете жизнь (даже если вы ввели не букву)).")
    print("И так вам необходимо вводить из раза в раз эти буквы пока не умрёте")
    print("        или выиграете.")
    print("Надеюсь вы всё поняли!\n")


def help2():  # Инструкция что делать и как.
    print("Your goal is to guess the word.")
    print("To do this, you need to enter the number 4 and enter the expected letter.")
    print("If you forget what you entered, you can press 2 or 3.")
    print("If you can guess what the word is, you can enter 5 and")
    print("                try to guess the word (without losing a life).")
    print("(in other cases, you lose a life (even if you entered a non-letter)).")
    print("And so you need to enter these letters over and over again until you die")
    print("        or you will win.")
    print("I hope you understood everything!\n")



if language == "1":
    da = "да"
    help1()
else:
    da = "yes"
    help2()




def win():  # Если человек выиграл, то выведеться такое поздравлние (график).
    print("Вы выйграли! Ураааааааа!")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠛⢉⣉⣁⣀⣀⣈⣉⡉⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⠿⠋⣀⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣀⠙⠿⣿⣿⣿⣿⣿\n⣿⣿⣿⡟⠁⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠈⢻⣿⣿⣿")
    print("⣿⣿⠋⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠙⣿⣿\n⣿⣿⠋⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠙⣿⣿")
    print("⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠉⠉⠛⠿⠿⠿⠿⠛⠉⠉⠄⠄⠄⠄⠄⠄⠄⠄⠘⣿\n⡟⢀⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣴⣦⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⡀⢻")
    print("⠇⢸⣇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣸⣿⣿⣇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣸⡇⠘\n⠄⢸⣿⡄⠄⠄⠄⠄⠄⠄⠄⠄⣰⣿⣿⣿⣿⣆⠄⠄⠄⠄⠄⠄⠄⠄⢠⣿⡇⠄")
    print("⡆⢸⣿⣿⣷⣦⣤⣀⣀⣤⣤⣾⣿⣿⣿⣿⣿⣿⣷⣤⣤⣀⣀⣤⣴⣶⣿⣿⡇⢠\n⣧⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⣼")
    print("⣿⡄⠸⣿⣿⣿⣿⣿⡈⠙⠻⠿⣿⣿⣿⣿⣿⣿⠿⠟⠋⢁⣿⣿⣿⣿⣿⠇⢠⣿\n⣿⣿⣄⠘⢿⣿⣿⣿⣿⣦⣄⡀⠄⠄⠈⠁⠄⠄⢀⣠⣴⣿⣿⣿⣿⡿⠃⣠⣿⣿")
    print("⣿⣿⣿⣧⡀⠙⢿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⡿⠋⢀⣴⣿⣿⣿\n⣿⣿⣿⣿⣿⣶⣄⠉⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠉⣠⣴⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣤⣈⣉⠉⠉⠉⠉⣉⣁⣠⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")


def end():  # Выведеться когда человек проиграет.
    print("Вы проиграли!")
    print("____________________________________________\n_________$$$$$$$$$$$$$$$$$$$________________")
    print("________$$_________________$$$______________\n_______$_____________________$$$$___________")
    print("______$______$$$$$$_____________$$__________\n_____$____$$$$____$$$___$$$$$$$$_$$_________")
    print("____$$___$$_________$__$$_______$_$$________\n____$____$__________$__$________$__$________")
    print("____$____$_____$___$$__$____$___$__$________\n____$____$$________$____$______$$__$________")
    print("____$_____$$$$$$$$$______$$$$$$$___$________\n____$______________________________$________")
    print("____$$_____________________________$________\n_____$____________________________$$________")
    print("_____$$___________$$$$$$$$$_______$_________\n______$$________________________$$__________")
    print("________$$____________________$$$___________\n_________$$$$$$$$$$$$$$$$$$$$$$_____________")
    print("____________________________________________")


def dad1():  # Сделано для того чтобы под окончание первой игры человек мог сыграть ещё раз не перезапуская.
    word_regen1()
    print("Вам дано 10 жизней. Если вы ввели не букву, то у вас всё равно отниметься жизнь (да, жестоко),")
    print("НО зато вы можете предпологать что это за слово сколько угодно!")
    print("В слове:", len(word), "букв.")
    print("Чтобы выбрать один из вариантов введите соответсвующую ему цыфру.")
    x = ["_" for i in range(len(word))]
    lives = 10
    print("1. Правила игры (help()).")
    print("2. Вывести все гласные, которые вы ещё не вводили.")
    print("3. Вывести все согласные, которые вы ещё не вводили.")
    print("4. Ввести букву.")
    print("5. Ввести слово.")
    print("6. Выход (вы проиграете и узнаете слово).")
    otvet = input().strip()
    bil = list()
    while x != list(word):    # цикл в котором вы либо угодаете слово либо потратите все жизни
        if otvet == "4":
            a = (input("Введите предпологаемую букву: ").strip()).lower()
            if len(a) != 1:
                print("- ты уверен что это одна буква?")
            chance = 0
            stuped_n = 1
            while a in bil:  # Цикл в котором нужно ввести букву которая ещё не была введена.
                print(f"Это буква уже была. Даю тебе {stuped_n} шанс.")
                stuped_n += 1
                a = input("Введите предпологаемую букву: ").strip().lower()
            if a in glasn:  # Проверка (если буква гласная)
                bil.append(a)
                glasn.remove(a)
            elif a in soglasn:  # Проверка (если буква согласная)
                bil.append(a)
                soglasn.remove(a)
            else:
                print("Это вообще буква?")
                print("Мдэ...")
            ii = list()
            for i in range(len(word)):  # Проверка есть ли в слове эта буква.
                if word[i] == a:
                    ii.append(i)
                    chance = 1
            for j in range(len(word)):
                if j in ii:
                    x[j] = word[j]
            print(".".join(x))  # Вывод извесных букв.
            if chance == 0:  # Отнятие жизни...
                lives -= 1
                print("Такой буквы нет....")
                print("У вас осталось:", lives)
            if lives == 0:  # Проверка что человек ещё жив.
                end()
                break
            if x == word:  # А может слово уже угадано?
                win()
                print(f"Вы затратили {25 - lives} lives.")
        elif otvet == "2":
            print(f"Вы ещё не называли гласные: {str(glasn)[1:-1]}.")
        elif otvet == "3":
            print(f"Вы ещё не называли согласные: {str(soglasn)[1:-1]}.")
        elif otvet == "5":
            a = input("Введите предпологаемое слово: ").strip()
            if a == word:  # Если человек угадал сразу всё слово, то...
                print("Правильно!!!")
                win()
                print(f"Вы затратили {10 - lives} lives.")
                break
            else:
                print("Нет ._.")
        elif otvet == "6":
            print(f"Это было слово '{word}'...")  # Если человек сдался.
            break
        else:
            print("Это ещё что-такое?")  # Если нет такого действия.
            print("Такого варианта нет...")
        print("1. Правила игры (help()).")
        print("2. Вывести все гласные, которые вы ещё не вводили.")
        print("3. Вывести все согласные, которые вы ещё не вводили.")
        print("4. Ввести букву.")
        print("5. Ввести слово.")
        print("6. Выход (вы проиграете и узнаете слово).")
        otvet = input().strip()



def dad2():  # Сделано для того чтобы под окончание первой игры человек мог сыграть ещё раз не перезапуская.
    word_regen2()
    print("You are given 10 lives. If you enter a non-letter, your life will still be taken away (yes, cruel),")
    print("BUT you can guess what this word is as much as you like!")
    print("In word:", len(word), "letters.")
    print("To select one of the options, enter the corresponding number.")
    x = ["_" for i in range(len(word))]
    lives = 10
    print("1. Rules of the game (help()).")
    print("4. Enter a letter.")
    print("5. Enter a word.")
    print("6. Exit (you lose and learn the word).")
    otvet = input().strip()
    bil = list()
    while x != list(word):    # цикл в котором вы либо угодаете слово либо потратите все жизни
        if otvet == "4":
            a = (input("Enter the expected letter: ").strip()).lower()
            if len(a) != 1:
                print("- Are you sure it's one letter?")
            chance = 0
            stuped_n = 1
            while a in bil:  # Цикл в котором нужно ввести букву которая ещё не была введена.
                print(f"This letter has already been. I'm giving you {stuped_n} a chance.")
                stuped_n += 1
                a = input("Enter the expected letter: ").strip().lower()
            if a in glasn:  # Проверка (если буква гласная)
                bil.append(a)
                glasn.remove(a)
            elif a in soglasn:  # Проверка (если буква согласная)
                bil.append(a)
                soglasn.remove(a)
            else:
                print("Is this even a letter?")
            ii = list()
            for i in range(len(word)):  # Проверка есть ли в слове эта буква.
                if word[i] == a:
                    ii.append(i)
                    chance = 1
            for j in range(len(word)):
                if j in ii:
                    x[j] = word[j]
            print(".".join(x))  # Вывод извесных букв.
            if chance == 0:  # Отнятие жизни...
                lives -= 1
                print("There is no such letter....")
                print("You are left with:", lives)
            if lives == 0:  # Проверка что человек ещё жив.
                end()
                break
            if x == word:  # А может слово уже угадано?
                win()
                print(f"You have spent {10 - lives} lives.")
        elif otvet == "5":
            a = input("Enter the expected word: ").strip()
            if a == word:  # Если человек угадал сразу всё слово, то...
                print("Right!!!")
                win()
                print(f"You have spent {10 - lives} lives.")
                break
            else:
                print("No ._.")
        elif otvet == "6":
            print(f"It was the word '{word}'...")  # Если человек сдался.
            break
        else:
            print("What the ... is this?")  # Если нет такого действия.
            print("There is no such option...")
        print("1. Game rules (help()).")
        print("4. Enter a letter.")
        print("5. Enter a word.")
        print("6. Exit (you lose and learn the word).")
        otvet = input().strip()


while da == "да" or da == "yes":
    if language == "1":
        dad1()
    else:
        dad2()
    if da == "yes":
        print("Do you want to play again?") # Выбор сыграть ещё раз.
        print("If yes, enter 'yes'")
        da = (input("Your answer: ").strip()).lower()
    else:
        print("Хотите сыграть в ещё раз?") # Выбор сыграть ещё раз.
        print("Если да, то введите 'да'")
        da = (input("Ваш ответ: ").strip()).lower()
    
print('До свидания.')
input()
