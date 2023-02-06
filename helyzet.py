from Gepek import Gepek


def beolvas():
    gepek = []
    file = open("gep.txt", "r", encoding="UTF=8")
    file.readline()
    pc = file.readlines()
    file.close()
    i = 0
    while i < len(pc):
        sor = pc[i].strip().split("!")
        gepek.append(Gepek(sor))
        i += 1
    return gepek


def gepek_szama(gepek):
    print(f"III/A, B:\n\tA gépek száma: {len(gepek)}")


def atlag(gepek):
    i = 0
    azon = 0
    db = 0
    while i < len(gepek):

        if int(gepek[i].hely.strip("T")) % 2 == 0:
            azon += gepek[i].id
            db += 1
        i += 1
    print(f"III/C:\n\tA páros teremszámú termek azonosító átlaga: {int(azon/db)}")


def legkisebb(gepek):
    i = 0
    azon = gepek[0].id
    t = gepek[0].hely
    while i < len(gepek):
        if gepek[i].id < azon:
            azon = gepek[i].id
            t = gepek[i].hely
        i += 1
    print(f"III/D:\n\tA legkisebb asztali gép azonosítója: {azon}, helye: {t}.")
