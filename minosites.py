def beker():
    print("I/A:")
    str(input("Múzeum neve: "))
    str(input("Latogató neve: "))


def ertekel():
    ertekeles = int(input("Értékelés (1-20):"))
    print(f"I/B:")
    if ertekeles <= 0:
        print("Az értékelés nem lehet negatív vagy 0!")
    elif ertekeles > 20:
        print("20 pont feletti értékelés nem elfogadható")
    else:
        print("Köszönjük az értékelést!")
