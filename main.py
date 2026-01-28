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
        print("Obsah čtverce je" + result)
        return





select_and_use_function()