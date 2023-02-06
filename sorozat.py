import random


def veletlen_szamok():
    szamok = []
    i = 0
    while i < 15:
        szamok.append(int(random.random()*591)-90)
        i += 1
    return szamok


def szamok_csillag(szamok):
    i = 0
    szoveg = ""
    while i < len(szamok):
        if i == len(szamok)-1:
            szoveg += str(szamok[i])
        else:
            szoveg += str(szamok[i]) + "*"
        i += 1
    print("II/A, B, C:")
    print(szoveg)


def oszthatok_szama(szamok):
    i = 0
    db = 0
    while i < len(szamok):
        if szamok[i] % 10 == 0:
            db += 1
        i += 1
    return db


def konzolra_ir(db):
    print(f"\nII/D, E:\nTízzel oszthatóak száma: {db}.")


def fajl_ir(db):
    file = open("kimutatas.txt", "w", encoding="UTF-8")
    file.write(f"Tízzel oszthatóak száma: {db}.")
    file.close()
    print(f"\nII/F:\nA fájl kiírása megtörtént!")
