unit = "cm"

def square_area(a):
    return a * a

def rectangle_area(a, b):
    return a * b

def circle_area(r):
    return 3.14 * r * r

def triangle_area(a, h):
    return (a * h) / 2

def cube_volume(a):
    return a * a * a

def choose_unit():
    global unit

    print("1. mm")
    print("2. cm")
    print("3. dm")
    print("4. m")
    print("5. km")

    choice = int(input("Zadejte jednotku ve které chcete počítat > "))

    if choice == 1:
        unit = "mm"
    elif choice == 2:
        unit = "cm"
    elif choice == 3:
        unit = "dm"
    elif choice == 4:
        unit = "m"
    elif choice == 5:
        unit = "km"
    else:
        print("Neplatná volba, nastavena výchozí jednotka cm")
        unit = "cm"


def select_and_use_function():
    print("Vyberte tvar:")
    print("1. Čtverec")
    print("2. Obdelník")
    print("3. Kruh")
    print("4. Trojúhelník")
    print("5. Krychle (objem)")

    choice = int(input("Zadejte číslo tvaru > "))

    if choice == 1:
        side = float(input("Zadejte délku strany čtverce > "))
        result = square_area(side)
        print("Obsah čtverce je " + str(result) + " " + unit + "²")
    elif choice == 2:
        width = float(input("Zadejte šířku obdelníku > "))
        height = float(input("Zadejte výšku obdelníku > "))
        result = rectangle_area(width, height)
        print("Obsah obdelníku je " + str(result) + " " + unit + "²")
    elif choice == 3:
        radius = float(input("Zadejte poloměr kruhu > "))
        result = circle_area(radius)
        print("Obsah kruhu je " + str(result) + " " + unit + "²")
    elif choice == 4:
        base = float(input("Zadejte délku základny trojúhelníku > "))
        height = float(input("Zadejte výšku trojúhelníku > "))
        result = triangle_area(base, height)
        print("Obsah trojúhelníku je " + str(result) + " " + unit + "²")
    elif choice == 5:
        side = float(input("Zadejte délku hrany krychle > "))
        result = cube_volume(side)
        print("Objem krychle je " + str(result) + " " + unit + "³")
    else:
        print("Neplatná volba")
    menu()


def menu():
    print("1. Vybrat jednotku a spočítat")
    print("2. Konec")

    choice = int(input("Zadejte volbu > "))

    if choice == 1:
        choose_unit()
        select_and_use_function()
    elif choice == 2:
        print("Konec programu")
    else:
        print("Neplatná volba")
        menu()


menu()