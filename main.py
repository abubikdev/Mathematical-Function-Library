def select_and_use_function():
    print("1. Obsah čtverce")
    print("2. Obsah obdélníku")
    print("3. Obsah koule")
    print("4. Obsah krychle")
    print("5. Obsah kvádru")

    selected_function = input("> ")

    if selected_function == "1":
        side_a: str = input("Zadejte délku jedné strany > ")

        result = int(side_a) * int(side_a)
        print("Obsah čtverce je " + str(result))
        return

    elif selected_function == "2":
        side_a: str = input("Zadejte délku strany a > ")
        side_b: str = input("Zadejte délku strany b > ")

        result = int(side_a) * int(side_b)
        print("Obsah obdélníku je " + str(result))
        return



select_and_use_function()